## Hero Sheet

One page to track a hero. Use your browser's **Print** (or Save as PDF) — the site menus are hidden automatically, so you get just the sheet.

<style>
.af-sheet {
  border: 2px solid #d35400;
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  max-width: 720px;
  font-family: inherit;
}
.af-sheet h3 { margin: 1.1rem 0 0.4rem; border-bottom: 2px solid #d35400; padding-bottom: 0.2rem; }
.af-sheet .af-title { text-align: center; font-size: 1.5rem; font-weight: 700; letter-spacing: 0.04em; margin: 0; }
.af-sheet .af-sub { text-align: center; font-size: 0.85rem; opacity: 0.7; margin: 0.1rem 0 0.6rem; }
.af-line { display: flex; align-items: flex-end; gap: 0.5rem; margin: 0.5rem 0; }
.af-line label { font-weight: 700; white-space: nowrap; }
.af-fill { flex: 1; border-bottom: 1.5px solid #888; min-height: 1.4rem; }
.af-hint { font-size: 0.8rem; opacity: 0.7; font-style: italic; }
.af-stats { display: flex; flex-wrap: wrap; gap: 0.5rem 1rem; font-weight: 700; }
.af-stats .af-stat { border: 1.5px solid #555; border-radius: 999px; padding: 0.2rem 0.85rem; font-size: 0.9rem; }
.af-assets { display: grid; grid-template-columns: 1fr; gap: 0.6rem; }
.af-asset { border: 1px solid #bbb; border-radius: 6px; padding: 0.5rem 0.6rem; }
.af-asset .af-fill { min-height: 1.5rem; }
.af-asset .af-boon { display: flex; gap: 0.4rem; align-items: center; margin-top: 0.35rem; font-size: 0.8rem; }
.af-asset .af-boon .af-fill { min-height: 1.1rem; }
.af-asset .af-boon .af-box { width: 0.9rem; height: 0.9rem; }
.af-asset .af-broken { display: flex; gap: 0.3rem; align-items: center; margin-top: 0.3rem; font-size: 0.72rem; opacity: 0.6; }
.af-asset .af-broken .af-box { width: 0.9rem; height: 0.9rem; }
.af-box { display: inline-block; width: 1.6rem; height: 1.6rem; border: 1.5px solid #555; border-radius: 4px; text-align: center; line-height: 1.6rem; font-size: 0.8rem; }
.af-track { display: flex; flex-wrap: wrap; gap: 0.3rem; align-items: center; }
.af-readiness .af-box.af-start { border-color: #d35400; border-width: 2.5px; font-weight: 700; }
.af-notes { border: 1px solid #bbb; border-radius: 6px; min-height: 4.5rem; margin-top: 0.3rem; }
.af-ref { font-size: 0.8rem; opacity: 0.85; border-top: 1px dashed #aaa; margin-top: 1rem; padding-top: 0.6rem; }
.af-ref b { color: #d35400; }

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
  .af-sheet .af-title { font-size: 1.3rem; }
  .af-sheet .af-sub { margin-bottom: 0.4rem; }
  .af-sheet h3 { margin: 0.55rem 0 0.2rem; font-size: 1.02rem; }
  .af-hint { font-size: 0.7rem; line-height: 1.3; margin: 0.15rem 0 0.3rem; }
  .af-line { margin: 0.3rem 0; }
  .af-assets { gap: 0.4rem 1rem; }
  .af-asset { padding: 0.35rem 0.5rem; }
  .af-asset .af-boon { margin-top: 0.25rem; }
  .af-notes { min-height: 2.6rem; }
  .af-ref { margin-top: 0.5rem; padding-top: 0.4rem; font-size: 0.72rem; }
}
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">LIGHTS, CAMERA, ACTION!</p>
  <p class="af-sub">Hero Sheet</p>

  <div class="af-line"><label>Hero Name</label><span class="af-fill"></span><label>Player</label><span class="af-fill"></span></div>

  <h3>Concept</h3>
  <div class="af-line"><span class="af-fill"></span></div>
  <p class="af-hint">Your one-line movie-poster pitch.</p>

  <h3>Stats</h3>
  <p class="af-hint">Circle <b>two.</b></p>
  <div class="af-stats">
    <span class="af-stat">Strong</span><span class="af-stat">Quick</span><span class="af-stat">Clever</span><span class="af-stat">Sneaky</span><span class="af-stat">Charming</span>
  </div>

  <h3>Assets</h3>
  <p class="af-hint">Three things your hero is great at. Note any <b>Boons</b> on the lines below each; check <b>Broken</b> if one gets knocked out.</p>
  <div class="af-assets">
    <div class="af-asset">
      <span class="af-hint" style="display:block;margin-bottom:0.2rem;">1. Skill or expertise</span>
      <div class="af-fill"></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
    <div class="af-asset">
      <span class="af-hint" style="display:block;margin-bottom:0.2rem;">2. Item, companion, or connection</span>
      <div class="af-fill"></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
    <div class="af-asset">
      <span class="af-hint" style="display:block;margin-bottom:0.2rem;">3. Their other side</span>
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
  <p class="af-hint">Fill one box per Growth earned.</p>
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
