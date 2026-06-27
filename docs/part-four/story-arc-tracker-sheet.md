## Story Arc Tracker Sheet

One sheet per Story Arc. It holds the **Goal**, the **size**, the **Story Arc Track** with its **Antagonist Track** (the antagonist's odd boxes are Closing In beats; the last box is their victory), room to name your **antagonist**, and numbered lines to jot each **Milestone**.

> **Printing tip:** use your browser's **Print** command (or Save as PDF) on this page. The site menus are hidden automatically, so you'll get just the sheet.

<style>
.af-sheet {
  border: 2px solid #d35400;
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  max-width: 760px;
  font-family: inherit;
}
.af-sheet h3 { margin: 1.1rem 0 0.4rem; border-bottom: 2px solid #d35400; padding-bottom: 0.2rem; }
.af-sheet .af-title { text-align: center; font-size: 1.5rem; font-weight: 700; letter-spacing: 0.04em; margin: 0; }
.af-sheet .af-sub { text-align: center; font-size: 0.85rem; opacity: 0.7; margin: 0.1rem 0 0.6rem; }
.af-line { display: flex; align-items: flex-end; gap: 0.5rem; margin: 0.5rem 0; }
.af-line label { font-weight: 700; white-space: nowrap; }
.af-fill { flex: 1; border-bottom: 1.5px solid #888; min-height: 1.4rem; }
.af-hint { font-size: 0.8rem; opacity: 0.7; font-style: italic; }
.af-scale { display: flex; gap: 1.4rem; flex-wrap: wrap; font-weight: 600; }
.af-scale span { display: flex; align-items: center; gap: 0.4rem; }
.af-scale .af-chk { width: 1rem; height: 1rem; border: 1.5px solid #555; border-radius: 3px; display: inline-block; }
.af-trackgrid { display: grid; grid-template-columns: max-content 1fr; gap: 0.35rem 0.6rem; align-items: center; }
.af-trackgrid .af-rowlabel { font-weight: 700; font-size: 0.8rem; white-space: nowrap; }
.af-row { display: flex; gap: 0.3rem; flex-wrap: nowrap; }
.af-box { display: inline-block; width: 1.55rem; height: 1.55rem; border: 1.5px solid #555; border-radius: 4px; text-align: center; line-height: 1.55rem; font-size: 0.72rem; flex: 0 0 auto; }
.af-quest .af-box { border-color: #2e7d32; }
.af-anta .af-box { border-color: #c0392b; }
.af-scalebar { display: flex; gap: 0.3rem; font-size: 0.6rem; font-weight: 700; opacity: 0.8; margin-left: 0; }
.af-scalebar span { width: 1.55rem; text-align: center; flex: 0 0 auto; white-space: nowrap; overflow: visible; }
.af-ms { display: flex; align-items: flex-end; gap: 0.45rem; margin: 0.3rem 0; font-size: 0.85rem; }
.af-ms .af-mschk { width: 1.05rem; height: 1.05rem; border: 1.5px solid #555; border-radius: 3px; display: inline-block; flex: 0 0 auto; margin-bottom: 0.1rem; }
.af-ms .af-num { font-weight: 700; width: 1.1rem; }
.af-ms .af-fill { min-height: 1.2rem; }
.af-mscols { display: grid; grid-template-columns: 1fr 1fr; gap: 0 1.4rem; }
.af-notes { border: 1px solid #bbb; border-radius: 6px; min-height: 3.5rem; margin-top: 0.3rem; }
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
  <p class="af-hint">Chain Stories like this one into a Season or Series &mdash; see Ch.10.</p>

  <h3>The Tracks</h3>
  <p class="af-hint">Heroes win by filling the Story Arc Track (completing the last Milestone); they lose if the Antagonist Track fills first. The antagonist's <strong>odd boxes (&#9650;) are Closing In beats</strong> &mdash; stop and play out the bad guys gaining ground &mdash; and the <strong>last box is their victory</strong>.</p>
  <div class="af-trackgrid">
    <span class="af-rowlabel">Story Arc</span>
    <div class="af-row af-quest">
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
  <p class="af-hint">Episode: 3 Story Arc / 5 Antagonist boxes (Closing In on 1&middot;3&middot;5; box&nbsp;5 = the antagonist's win). Movie: 6 Story Arc / 9 Antagonist (Closing In on 1&middot;3&middot;5&middot;7&middot;9; box&nbsp;9 = the win). Cross out the boxes you don't use. An antagonist box fills three ways &mdash; and no other: a hero takes the <strong>Devil's Bargain</strong>, a <strong>Miss shows doubles</strong>, or a hero goes <strong>Out of Action</strong>.</p>

  <h3 class="af-break">The Antagonist</h3>
  <div class="af-line"><label>Who / what</label><span class="af-fill"></span></div>
  <div class="af-line"><label>What it wants</label><span class="af-fill"></span></div>
  <p class="af-hint">Give it a face &mdash; even a force (a desert, a plague, a deadline) counts. When a Closing In box (&#9650;) fills, play it out: the antagonist just hit a milestone of their own.</p>

  <h3>Milestones</h3>
  <p class="af-hint">A concrete, pointable step toward the Goal. Number them to match the Story Arc Track boxes above. (Episode uses 1&ndash;3; Movie 1&ndash;6.)</p>
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

  <p class="af-ref"><b>Win:</b> complete the last Milestone (Story Arc Track full) &mdash; then Downtime resets the party to full Readiness. &nbsp; <b>Lose:</b> the Antagonist Track fills (a hero going Out of Action near the end can fill its last box), or you Quit the Story Arc &mdash; no penalty; ask "how did the world change?" and seed the next Story Arc. &nbsp; <b>Antagonist advances</b> one box three ways: a <b>Devil's Bargain</b>, a <b>Miss on doubles</b>, or a hero going <b>Out of Action</b> &mdash; and no other way.</p>
</div>
