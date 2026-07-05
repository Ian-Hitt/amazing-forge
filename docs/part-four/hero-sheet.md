## Hero Sheet

One page to track a hero. Use your browser's **Print** (or Save as PDF) — the site menus are hidden automatically, so you get just the sheet.

<style>
.af-sheet {
  --af-ink: #1a1a1a;
  --af-muted: #6b6b6b;
  --af-line: #b9b3aa;
  --af-paper: #f3f0ec;
  max-width: 720px;
  margin: 1rem 0;
  padding: 1.5rem 1.75rem;
  border: 2.5px solid var(--af-ink);
  border-radius: 10px;
  background: #fff;
  color: var(--af-ink);
  box-shadow: 0 1px 6px rgba(0,0,0,0.12);
  font-family: inherit;
}
/* Masthead */
.af-sheet .af-title {
  margin: 0;
  font-size: 1.7rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  line-height: 1.05;
}
.af-sheet .af-sub {
  margin: 0.2rem 0 1.1rem;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--md-primary-fg-color);
}
/* Section headers: LABEL ───────────── */
.af-sheet h3 {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  margin: 1.15rem 0 0.4rem;
  font-size: 0.95rem;
  font-weight: 800;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  border: 0;
  padding: 0;
}
.af-sheet h3::after {
  content: "";
  flex: 1;
  height: 2px;
  background: var(--af-ink);
}
.af-hint { font-size: 0.8rem; color: var(--af-muted); font-style: normal; margin: 0.15rem 0 0.5rem; }
.af-hint b { color: var(--af-ink); }
/* Write-in lines */
.af-line { display: flex; align-items: flex-end; gap: 0.6rem; margin: 0.55rem 0; }
.af-line label { font-weight: 700; white-space: nowrap; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }
.af-fill { flex: 1; border-bottom: 1.5px solid var(--af-line); min-height: 1.4rem; }
/* Stats — pills */
.af-stats { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.af-stats .af-stat {
  border: 2px solid var(--af-ink);
  border-radius: 999px;
  padding: 0.28rem 1.1rem;
  font-size: 0.9rem;
  font-weight: 700;
}
/* Assets — cards */
.af-assets { display: grid; grid-template-columns: 1fr; gap: 0.65rem; }
.af-asset {
  border: 1.5px solid var(--af-ink);
  border-radius: 8px;
  padding: 0.55rem 0.7rem;
  background: #fff;
}
.af-asset .af-cap {
  display: block;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--af-muted);
  margin-bottom: 0.3rem;
}
.af-asset .af-fill { min-height: 1.5rem; }
.af-asset .af-boon { display: flex; gap: 0.45rem; align-items: center; margin-top: 0.4rem; }
.af-asset .af-boon .af-fill { min-height: 1.1rem; }
.af-asset .af-boon .af-box { width: 0.95rem; height: 0.95rem; }
.af-asset .af-broken { display: flex; gap: 0.4rem; align-items: center; margin-top: 0.35rem; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--af-muted); }
.af-asset .af-broken .af-box { width: 0.95rem; height: 0.95rem; }
/* Boxes + tracks */
.af-box {
  display: inline-flex; align-items: center; justify-content: center;
  width: 1.7rem; height: 1.7rem;
  border: 1.8px solid var(--af-ink);
  border-radius: 5px;
  font-size: 0.8rem; font-weight: 700;
}
.af-track { display: flex; flex-wrap: wrap; gap: 0.35rem; align-items: center; }
.af-readiness .af-box.af-start { border-color: var(--md-primary-fg-color); border-width: 2.6px; color: var(--md-primary-fg-color); }
.af-notes { border: 1.5px solid var(--af-ink); border-radius: 8px; min-height: 4.5rem; margin-top: 0.35rem; }
.af-ref { font-size: 0.8rem; color: var(--af-muted); border-top: 2px solid var(--af-ink); margin-top: 1.1rem; padding-top: 0.6rem; }
.af-ref b { color: var(--md-primary-fg-color); }

@media print {
  .md-header, .md-tabs, .md-sidebar, .md-footer, .md-content__button, .md-nav { display: none !important; }
  .md-main__inner, .md-content { margin: 0 !important; }
  /* Print just the sheet: drop the page heading, intro prose, and printing tip. */
  .md-content__inner { margin: 0 !important; padding: 0 !important; }
  .md-content__inner > *:not(.af-sheet) { display: none !important; }
  .af-sheet { box-shadow: none !important; border-color: #000 !important; }
  /* Keep each section heading with its content, and never split a block across a page. */
  .af-sheet h3 { break-after: avoid; page-break-after: avoid; }
  .af-line, .af-asset, .af-track, .af-notes, .af-ref { break-inside: avoid; page-break-inside: avoid; }
  /* Compact the sheet so it stays on a single page. */
  .af-sheet { padding: 0.65rem 0.9rem; max-width: none; }
  .af-sheet .af-title { font-size: 1.4rem; }
  .af-sheet .af-sub { margin-bottom: 0.5rem; }
  .af-sheet h3 { margin: 0.6rem 0 0.2rem; font-size: 0.95rem; }
  .af-hint { font-size: 0.7rem; line-height: 1.3; margin: 0.15rem 0 0.3rem; }
  .af-line { margin: 0.32rem 0; }
  .af-assets { gap: 0.45rem; }
  .af-asset { padding: 0.4rem 0.55rem; }
  .af-asset .af-boon { margin-top: 0.28rem; }
  .af-notes { min-height: 2.6rem; }
  .af-ref { margin-top: 0.5rem; padding-top: 0.4rem; font-size: 0.72rem; }
}
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">Lights, Camera, Action!</p>
  <p class="af-sub">Hero Sheet</p>

  <div class="af-line"><label>Hero Name</label><span class="af-fill"></span><label>Player</label><span class="af-fill"></span></div>

  <h3>Concept</h3>
  <div class="af-line"><span class="af-fill"></span></div>
  <p class="af-hint">Your one-line movie-poster pitch.</p>

  <h3>Stats</h3>
  <p class="af-hint">Circle <b>two.</b> You get <b>+1</b> when the moment calls for one of them.</p>
  <div class="af-stats">
    <span class="af-stat">Strong</span><span class="af-stat">Quick</span><span class="af-stat">Clever</span><span class="af-stat">Sneaky</span><span class="af-stat">Charming</span>
  </div>

  <h3>Assets</h3>
  <p class="af-hint">Three things your hero is great at. Note any <b>Boons</b> on the lines below each; check <b>Broken</b> if one gets knocked out.</p>
  <div class="af-assets">
    <div class="af-asset">
      <span class="af-cap">1 · Skill or expertise</span>
      <div class="af-fill"></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
    <div class="af-asset">
      <span class="af-cap">2 · Item, companion, or connection</span>
      <div class="af-fill"></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
    <div class="af-asset">
      <span class="af-cap">3 · Their other side</span>
      <div class="af-fill"></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
  </div>

  <h3>Readiness</h3>
  <p class="af-hint">Start at 9 (your max). Cross off as it drops; refill when you regroup.</p>
  <div class="af-track af-readiness">
    <span class="af-box">0</span>
    <span class="af-box">1</span>
    <span class="af-box">2</span>
    <span class="af-box">3</span>
    <span class="af-box">4</span>
    <span class="af-box">5</span>
    <span class="af-box">6</span>
    <span class="af-box">7</span>
    <span class="af-box">8</span>
    <span class="af-box af-start">9</span>
  </div>

  <h3>Growth Track</h3>
  <p class="af-hint">Fill one box per Growth earned. Spend <b>2</b> on a Boon or <b>5</b> on a new Asset.</p>
  <div class="af-track">
    <span class="af-box"></span><span class="af-box"></span><span class="af-box"></span>
    <span class="af-box"></span><span class="af-box"></span><span class="af-box"></span>
    <span class="af-box"></span><span class="af-box"></span><span class="af-box"></span>
    <span class="af-box"></span><span class="af-box"></span><span class="af-box"></span>
    <span class="af-box"></span><span class="af-box"></span><span class="af-box"></span>
    <span class="af-box"></span><span class="af-box"></span><span class="af-box"></span>
  </div>

  <h3>Story Arc Notes</h3>
  <div class="af-notes"></div>
</div>
