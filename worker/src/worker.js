// Lights, Camera, Action! — shared-campaign backend (Cloudflare Worker + KV).
//
// No accounts. A campaign lives under a short game code; anyone with the code
// reads and writes it. A monotonically increasing `version` lets clients poll
// cheaply and only pull the full campaign when something actually changed.
//
// Routes:
//   POST /new                 -> { code, version }                create a game (body: { campaign })
//   GET  /c/:code             -> { version, updated, campaign }
//   GET  /c/:code/version     -> { version, updated }             cheap poll
//   PUT  /c/:code             -> { version, updated, campaign }   field-level merge (body: { campaign })
//
// Writes are MERGED, not overwritten: the campaign wire is { content, meta } where `meta`
// carries a last-modified timestamp per item (keyed by stable id), per world-cell, and for
// the name, plus tombstones for deletes. Two players editing different heroes / world cells
// never clobber each other (last-writer-wins only on the same item). The merged campaign is
// echoed back so the writer immediately sees everyone else's concurrent edits. Kept in sync
// with the matching code in docs/play/campaign.html.

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,PUT,POST,OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Max-Age": "86400",
};

// 120-day self-cleanup: every write refreshes it, so live games never expire,
// but abandoned ones drop out of KV on their own.
const TTL_SECONDS = 60 * 60 * 24 * 120;

// Uploaded images (hero/place/cast portraits) go to R2, never into the campaign JSON.
// The client downscales to a small thumbnail first, so this cap is just a sanity guard.
const MAX_IMG_BYTES = 3 * 1024 * 1024;
const IMG_TYPES = { "image/jpeg": "jpg", "image/png": "png", "image/webp": "webp" };

// Unambiguous alphabet (no 0/O/1/I/L) for friendly, readable codes.
const ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", ...CORS },
  });
}

function makeCode() {
  let s = "";
  for (let i = 0; i < 6; i++) s += ALPHABET[Math.floor(Math.random() * ALPHABET.length)];
  return s;
}

// ---------- field-level merge (mirrors docs/play/campaign.html) ----------
const SYNC_COLS = ["h", "k", "c", "p", "e"];
function freshContent() { return { n: "", h: [], k: [], c: [], w: ["", "", "", "", "", "", "", "", "", ""], p: [], e: [] }; }
function freshMeta() { return { u: { h: {}, k: {}, c: {}, p: {}, e: {} }, o: {}, name: 0, world: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], tomb: {} }; }
function mUid(p) { return (p || "x") + Math.random().toString(36).slice(2, 8) + Date.now().toString(36).slice(-3); }
function fingerprint(it) { const o = {}; for (const k in it) { if (k !== "i") o[k] = it[k]; } return JSON.stringify(o); }
function indexById(arr) { const m = {}; (arr || []).forEach((it) => { if (it && it.i != null) m[it.i] = it; }); return m; }
function normContent(c) {
  c = c || {};
  const out = { n: c.n || "", h: c.h || [], k: c.k || [], c: c.c || [], w: Array.isArray(c.w) ? c.w.slice(0, 10) : [], p: c.p || [], e: c.e || [] };
  while (out.w.length < 10) out.w.push("");
  SYNC_COLS.forEach((ck) => { out[ck] = (out[ck] || []).map((it) => { if (it.i == null) it = { ...it, i: mUid(ck) }; return it; }); });
  return out;
}
function splitWire(wire) {
  wire = wire || {};
  if (wire.content) {
    const m = wire.meta || freshMeta();
    m.u = m.u || { h: {}, k: {}, c: {}, p: {}, e: {} }; m.o = m.o || {}; m.tomb = m.tomb || {};
    m.world = m.world || [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; m.name = m.name || 0;
    SYNC_COLS.forEach((ck) => { m.u[ck] = m.u[ck] || {}; });
    return { content: normContent(wire.content), meta: m };
  }
  const c = normContent(wire), meta = freshMeta();
  SYNC_COLS.forEach((ck) => { (c[ck] || []).forEach((it, idx) => { meta.u[ck][it.i] = 1; meta.o[it.i] = idx + 1; }); });
  meta.name = 1; for (let i = 0; i < 10; i++) meta.world[i] = 1;
  return { content: c, meta };
}
function mergeWire(a, b) {
  a = splitWire(a); b = splitWire(b);
  const out = { content: freshContent(), meta: freshMeta() };
  SYNC_COLS.forEach((ck) => {
    const ai = indexById(a.content[ck]), bi = indexById(b.content[ck]);
    const au = a.meta.u[ck] || {}, bu = b.meta.u[ck] || {};
    const ids = {};
    Object.keys(ai).forEach((k) => { ids[k] = 1; }); Object.keys(bi).forEach((k) => { ids[k] = 1; });
    Object.keys(a.meta.tomb).forEach((k) => { ids[k] = 1; }); Object.keys(b.meta.tomb).forEach((k) => { ids[k] = 1; });
    Object.keys(ids).forEach((id) => {
      const ua = au[id] != null ? au[id] : -1, ub = bu[id] != null ? bu[id] : -1;
      const tomb = Math.max(a.meta.tomb[id] || 0, b.meta.tomb[id] || 0);
      const live = Math.max(ua, ub);
      if (live < 0) { if (tomb > 0) out.meta.tomb[id] = tomb; return; }
      if (tomb >= live) { out.meta.tomb[id] = tomb; return; }
      let item, uts;
      if (ua > ub) { item = ai[id]; uts = ua; }
      else if (ub > ua) { item = bi[id]; uts = ub; }
      else { const ia = ai[id], ib = bi[id]; item = (ia && ib) ? (fingerprint(ia) >= fingerprint(ib) ? ia : ib) : (ia || ib); uts = ua; }
      if (!item) return;
      out.content[ck].push(item);
      out.meta.u[ck][id] = uts;
      out.meta.o[id] = a.meta.o[id] != null ? a.meta.o[id] : (b.meta.o[id] != null ? b.meta.o[id] : uts);
    });
    out.content[ck].sort((x, y) => { const ox = out.meta.o[x.i] || 0, oy = out.meta.o[y.i] || 0; if (ox !== oy) return ox - oy; return (x.i < y.i ? -1 : x.i > y.i ? 1 : 0); });
  });
  if ((a.meta.name || 0) >= (b.meta.name || 0)) { out.content.n = a.content.n; out.meta.name = a.meta.name || 0; }
  else { out.content.n = b.content.n; out.meta.name = b.meta.name; }
  for (let i = 0; i < 10; i++) { const wa = a.meta.world[i] || 0, wb = b.meta.world[i] || 0; if (wa >= wb) { out.content.w[i] = a.content.w[i] || ""; out.meta.world[i] = wa; } else { out.content.w[i] = b.content.w[i] || ""; out.meta.world[i] = wb; } }
  return out;
}

export default {
  async fetch(req, env) {
    if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

    const url = new URL(req.url);
    const parts = url.pathname.split("/").filter(Boolean); // e.g. ["c","K7QM2X","version"]

    try {
      // POST /new
      if (req.method === "POST" && parts[0] === "new") {
        const body = await req.json().catch(() => ({}));
        let code;
        for (let tries = 0; tries < 6; tries++) {
          code = makeCode();
          if (!(await env.CAMPAIGNS.get("c:" + code))) break;
        }
        const rec = { version: 1, updated: Date.now(), campaign: splitWire(body.campaign || {}) };
        await env.CAMPAIGNS.put("c:" + code, JSON.stringify(rec), { expirationTtl: TTL_SECONDS });
        return json({ code, version: rec.version, updated: rec.updated });
      }

      // POST /img  -> { url }   store an uploaded thumbnail in R2
      if (req.method === "POST" && parts[0] === "img") {
        const type = (req.headers.get("Content-Type") || "").split(";")[0].trim();
        const ext = IMG_TYPES[type];
        if (!ext) return json({ error: "bad_type" }, 415);
        const buf = await req.arrayBuffer();
        if (!buf.byteLength) return json({ error: "empty" }, 400);
        if (buf.byteLength > MAX_IMG_BYTES) return json({ error: "too_large" }, 413);
        const key = crypto.randomUUID() + "." + ext;
        await env.IMAGES.put(key, buf, { httpMetadata: { contentType: type } });
        return json({ url: url.origin + "/img/" + key });
      }

      // GET /img/:key  -> the stored image bytes
      if (req.method === "GET" && parts[0] === "img" && parts[1]) {
        const obj = await env.IMAGES.get(parts[1]);
        if (!obj) return json({ error: "not_found" }, 404);
        const headers = new Headers(CORS);
        headers.set("Content-Type", obj.httpMetadata?.contentType || "application/octet-stream");
        headers.set("Cache-Control", "public, max-age=31536000, immutable");
        headers.set("ETag", obj.httpEtag);
        return new Response(obj.body, { headers });
      }

      // /c/:code[/version]
      if (parts[0] === "c" && parts[1]) {
        const key = "c:" + parts[1].toUpperCase();

        if (parts[2] === "version" && req.method === "GET") {
          const raw = await env.CAMPAIGNS.get(key);
          if (!raw) return json({ error: "not_found" }, 404);
          const rec = JSON.parse(raw);
          return json({ version: rec.version, updated: rec.updated });
        }

        if (req.method === "GET") {
          const raw = await env.CAMPAIGNS.get(key);
          if (!raw) return json({ error: "not_found" }, 404);
          return json(JSON.parse(raw));
        }

        if (req.method === "PUT") {
          const body = await req.json().catch(() => null);
          if (!body || typeof body.campaign === "undefined") return json({ error: "bad_body" }, 400);
          const raw = await env.CAMPAIGNS.get(key);
          if (!raw) return json({ error: "not_found" }, 404);
          const rec = JSON.parse(raw);
          rec.version = (rec.version || 0) + 1;
          rec.updated = Date.now();
          rec.campaign = mergeWire(rec.campaign || {}, body.campaign);
          await env.CAMPAIGNS.put(key, JSON.stringify(rec), { expirationTtl: TTL_SECONDS });
          return json({ version: rec.version, updated: rec.updated, campaign: rec.campaign });
        }
      }

      return json({ error: "bad_request" }, 400);
    } catch (e) {
      return json({ error: String(e && e.message || e) }, 500);
    }
  },
};
