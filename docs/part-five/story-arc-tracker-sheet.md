## Story Arc Tracker Sheet

One sheet per Story Arc. It holds the **Goal**, the **size**, the **Hero Track** with its **Antagonist Track** (the antagonist's odd boxes are Closing In beats; the last box is their victory), room to name your **antagonist**, and numbered lines to jot each **Milestone**.

> **Printing tip:** use your browser's **Print** command (or Save as PDF) on this page. The site menus are hidden automatically, so you'll get just the sheet.

<style>
.af-sheet {
  --af-ink: #1a1a1a;
  --af-muted: #6b6b6b;
  --af-line: #b9b3aa;
  --af-paper: #f3f0ec;
  max-width: 760px;
  margin: 1rem 0;
  padding: 1.5rem 1.75rem;
  border: 2.5px solid var(--af-ink);
  border-radius: 10px;
  background: #fff;
  color: var(--af-ink);
  box-shadow: 0 1px 6px rgba(0,0,0,0.12);
  font-family: inherit;
}
.af-sheet h3 { display: flex; align-items: center; gap: 0.7rem; margin: 1.15rem 0 0.4rem; font-size: 0.95rem; font-weight: 800; letter-spacing: 0.09em; text-transform: uppercase; border: 0; padding: 0; }
.af-sheet h3::after { content: ""; flex: 1; height: 2px; background: var(--af-ink); }
.af-sheet .af-title { margin: 0; font-size: 1.7rem; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; line-height: 1.05; }
.af-sheet .af-sub { margin: 0.2rem 0 1.1rem; font-size: 0.85rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--md-primary-fg-color); }
.af-line { display: flex; align-items: flex-end; gap: 0.5rem; margin: 0.5rem 0; }
.af-line label { font-weight: 700; white-space: nowrap; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.04em; }
.af-fill { flex: 1; border-bottom: 1.5px solid var(--af-line); min-height: 1.4rem; }
.af-hint { font-size: 0.8rem; color: var(--af-muted); font-style: normal; }
.af-hint b, .af-hint strong { color: var(--af-ink); }
.af-scale { display: flex; gap: 1.4rem; flex-wrap: wrap; font-weight: 600; font-size: 0.85rem; }
.af-scale span { display: flex; align-items: center; gap: 0.4rem; }
.af-scale .af-chk { width: 1rem; height: 1rem; border: 1.6px solid var(--af-ink); border-radius: 3px; display: inline-block; }
.af-trackgrid { display: grid; grid-template-columns: max-content 1fr; gap: 0.35rem 0.6rem; align-items: center; }
.af-trackgrid .af-rowlabel { font-weight: 800; font-size: 0.78rem; white-space: nowrap; text-transform: uppercase; letter-spacing: 0.04em; }
.af-row { display: flex; gap: 0.3rem; flex-wrap: nowrap; }
.af-box { display: inline-flex; align-items: center; justify-content: center; width: 1.55rem; height: 1.55rem; border: 1.8px solid var(--af-ink); border-radius: 5px; font-size: 0.72rem; font-weight: 700; flex: 0 0 auto; }
.af-hero .af-box { background: #fff; }
.af-anta .af-box { background: var(--af-paper); }
.af-scalebar { display: flex; gap: 0.3rem; font-size: 0.6rem; font-weight: 700; color: var(--af-muted); margin-left: 0; }
.af-scalebar span { width: 1.55rem; text-align: center; flex: 0 0 auto; white-space: nowrap; overflow: visible; }
.af-ms { display: flex; align-items: flex-end; gap: 0.45rem; margin: 0.3rem 0; font-size: 0.85rem; }
.af-ms .af-mschk { width: 1.05rem; height: 1.05rem; border: 1.6px solid var(--af-ink); border-radius: 3px; display: inline-block; flex: 0 0 auto; margin-bottom: 0.1rem; }
.af-ms .af-num { font-weight: 800; width: 1.1rem; }
.af-ms .af-fill { min-height: 1.2rem; }
.af-mscols { display: grid; grid-template-columns: 1fr 1fr; gap: 0 1.4rem; }
.af-notes { border: 1.5px solid var(--af-ink); border-radius: 8px; min-height: 3.5rem; margin-top: 0.35rem; }
.af-ref { font-size: 0.8rem; color: var(--af-muted); border-top: 2px solid var(--af-ink); margin-top: 1rem; padding-top: 0.6rem; }
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
  .af-line, .af-scale, .af-trackgrid, .af-row, .af-ms, .af-notes, .af-ref { break-inside: avoid; page-break-inside: avoid; }
  /* Break the sheet cleanly: Goal + Size + Tracks on page 1, Antagonist +
     Milestones + Notes on page 2. */
  .af-break { break-before: page; page-break-before: always; }
  /* Compact each half so it stays on a single page. */
  .af-sheet { padding: 0.65rem 0.9rem; max-width: none; }
  .af-sheet .af-title { font-size: 1.3rem; }
  .af-sheet .af-sub { margin-bottom: 0.4rem; }
  .af-sheet h3 { margin: 0.5rem 0 0.2rem; font-size: 1.02rem; }
  .af-hint { font-size: 0.7rem; line-height: 1.3; margin: 0.15rem 0 0.3rem; }
  .af-line { margin: 0.3rem 0; }
  .af-scale { gap: 1rem; }
  .af-ms { margin: 0.22rem 0; }
  .af-notes { min-height: 2.6rem; }
  .af-ref { margin-top: 0.5rem; padding-top: 0.4rem; font-size: 0.72rem; }
}
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">LIGHTS, CAMERA, ACTION!</p>
  <p class="af-sub">Story Arc Tracker</p>

  <h3>The Goal</h3>
  <div class="af-line"><span class="af-fill"></span></div>
  <p class="af-hint">The single, clear victory condition, in one sentence ("Recover the stolen Sun Crystal").</p>

  <h3>Size</h3>
  <div class="af-scale">
    <span><span class="af-chk"></span> Episode &mdash; 3 Milestones / 5-box antagonist (one sitting)</span>
    <span><span class="af-chk"></span> Movie &mdash; 6 Milestones / 9-box antagonist (2&ndash;3 sessions)</span>
  </div>

  <h3>The Tracks</h3>
  <div class="af-trackgrid">
    <span class="af-rowlabel">Hero</span>
    <div class="af-row af-hero">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span>
      <span class="af-box">4</span><span class="af-box">5</span><span class="af-box">6</span>
    </div>
    <span class="af-rowlabel"></span>
    <div class="af-scalebar">
      <span></span><span></span><span>&#8593;Ep</span>
      <span></span><span></span><span>&#8593;Movie</span>
    </div>
    <span class="af-rowlabel">Antagonist</span>
    <div class="af-row af-anta">
      <span class="af-box">&#9650;</span><span class="af-box">2</span><span class="af-box">&#9650;</span><span class="af-box">4</span><span class="af-box">&#9650;</span><span class="af-box">6</span><span class="af-box">&#9650;</span><span class="af-box">8</span><span class="af-box">&#9650;</span>
    </div>
    <span class="af-rowlabel"></span>
    <div class="af-scalebar">
      <span></span><span></span><span></span><span></span><span>&#8593;Ep</span><span></span><span></span><span></span><span>&#8593;Movie</span>
    </div>
  </div>
  <p class="af-hint">Cross out the boxes you don't use &mdash; Episode is 3 Hero / 5 antagonist boxes, Movie is 6 / 9. The antagonist's <strong>&#9650; boxes are Closing In beats;</strong> its last box is the antagonist's win.</p>

  <h3 class="af-break">The Antagonist</h3>
  <div class="af-line"><label>Who / what</label><span class="af-fill"></span></div>
  <div class="af-line"><label>What it wants</label><span class="af-fill"></span></div>
  <p class="af-hint">Give it a face &mdash; a person, a faction, or even a force (a desert, a plague, a deadline).</p>

  <h3>Milestones</h3>
  <p class="af-hint">A concrete, pointable step toward the Goal. Number them to match the Hero Track boxes above. (Episode uses 1&ndash;3; Movie 1&ndash;6.)</p>
  <div class="af-mscols">
    <div class="af-ms"><span class="af-mschk"></span><span class="af-num">1.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-mschk"></span><span class="af-num">4.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-mschk"></span><span class="af-num">2.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-mschk"></span><span class="af-num">5.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-mschk"></span><span class="af-num">3.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-mschk"></span><span class="af-num">6.</span><span class="af-fill"></span></div>
  </div>

  <h3>Notes</h3>
  <div class="af-notes"></div>
</div>
