// Lights, Camera, Action! — shared-campaign backend (Cloudflare Worker + KV).
//
// No accounts. A campaign lives under a short game code; anyone with the code
// reads and writes it. A monotonically increasing `version` lets clients poll
// cheaply and only pull the full campaign when something actually changed.
//
// Routes:
//   POST /new                 -> { code, version }      create a game (body: { campaign })
//   GET  /c/:code             -> { version, updated, campaign }
//   GET  /c/:code/version     -> { version, updated }   cheap poll
//   PUT  /c/:code             -> { version, updated }   overwrite (body: { campaign })

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,PUT,POST,OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Max-Age": "86400",
};

// 120-day self-cleanup: every write refreshes it, so live games never expire,
// but abandoned ones drop out of KV on their own.
const TTL_SECONDS = 60 * 60 * 24 * 120;

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
        const rec = { version: 1, updated: Date.now(), campaign: body.campaign || {} };
        await env.CAMPAIGNS.put("c:" + code, JSON.stringify(rec), { expirationTtl: TTL_SECONDS });
        return json({ code, version: rec.version, updated: rec.updated });
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
          rec.campaign = body.campaign;
          await env.CAMPAIGNS.put(key, JSON.stringify(rec), { expirationTtl: TTL_SECONDS });
          return json({ version: rec.version, updated: rec.updated });
        }
      }

      return json({ error: "bad_request" }, 400);
    } catch (e) {
      return json({ error: String(e && e.message || e) }, 500);
    }
  },
};
