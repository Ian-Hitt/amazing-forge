## Story Arc Tracker Sheet

One sheet per Story Arc. It holds the **Goal**, the **scale**, the paired **Story Arc Track** and **Antagonist Track**, room to name your **antagonist**, and numbered lines to jot each **Milestone**. Running several Story Arcs at once? Print one of these for each — keep every race on its own page.

> **Printing tip:** use your browser's **Print** command (or Save as PDF) on this page. The site menus are hidden automatically, so you'll get just the sheet.

<style>
@media print {
  .md-header, .md-tabs, .md-sidebar, .md-footer, .md-content__button, .md-nav { display: none !important; }
  .md-main__inner, .md-content { margin: 0 !important; }
  .af-sheet { box-shadow: none !important; border-color: #000 !important; }
}
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
.af-scalebar { display: flex; gap: 0.3rem; font-size: 0.65rem; opacity: 0.7; margin-left: 0; }
.af-scalebar span { width: 1.55rem; text-align: center; flex: 0 0 auto; }
.af-ms { display: flex; align-items: flex-end; gap: 0.5rem; margin: 0.3rem 0; font-size: 0.85rem; }
.af-ms .af-num { font-weight: 700; width: 1.4rem; }
.af-ms .af-fill { min-height: 1.2rem; }
.af-mscols { display: grid; grid-template-columns: 1fr 1fr; gap: 0 1.4rem; }
.af-notes { border: 1px solid #bbb; border-radius: 6px; min-height: 3.5rem; margin-top: 0.3rem; }
.af-ref { font-size: 0.8rem; opacity: 0.85; border-top: 1px dashed #aaa; margin-top: 1rem; padding-top: 0.6rem; }
.af-ref b { color: #d35400; }
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">LIGHTS, CAMERA, ACTION!</p>
  <p class="af-sub">Story Arc Tracker</p>

  <h3>The Goal</h3>
  <div class="af-line"><span class="af-fill"></span></div>
  <p class="af-hint">The single, clear victory condition, in one sentence ("Recover the stolen Sun Crystal").</p>

  <h3>Scale</h3>
  <div class="af-scale">
    <span><span class="af-chk"></span> Episode &mdash; 3 boxes (one sitting)</span>
    <span><span class="af-chk"></span> Movie &mdash; 8 boxes (one story, 2&ndash;3 sessions)</span>
    <span><span class="af-chk"></span> Season &mdash; 8 boxes</span>
    <span><span class="af-chk"></span> Series &mdash; 12 boxes</span>
  </div>
  <div class="af-line"><label>Also advances</label><span class="af-fill"></span></div>
  <p class="af-hint">Any larger Story Arc a big beat here might <em>also</em> move &mdash; when it does, mark a box on both. (Leave blank for a standalone adventure.)</p>

  <h3>Role <span style="font-weight:400;font-size:0.8rem;opacity:0.7;">(optional &mdash; how to play it, not a rule)</span></h3>
  <div class="af-scale">
    <span><span class="af-chk"></span> Main plot</span>
    <span><span class="af-chk"></span> Side plot</span>
    <span><span class="af-chk"></span> Character arc</span>
  </div>
  <div class="af-line"><label>If a character arc, for whom</label><span class="af-fill"></span></div>
  <p class="af-hint">Main = return most sessions; Side = touch periodically; Character arc = surface in that hero's spotlight beats.</p>

  <h3>The Tracks</h3>
  <p class="af-hint">Use as many boxes as your scale. Heroes win by filling the Story Arc Track first; they lose if the Antagonist Track fills first. Both rows are the same length.</p>
  <div class="af-trackgrid">
    <span class="af-rowlabel">Story Arc</span>
    <div class="af-row af-quest">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span>
      <span class="af-box">4</span><span class="af-box">5</span><span class="af-box">6</span>
      <span class="af-box">7</span><span class="af-box">8</span><span class="af-box">9</span>
      <span class="af-box">10</span><span class="af-box">11</span><span class="af-box">12</span>
    </div>
    <span class="af-rowlabel">Antagonist</span>
    <div class="af-row af-anta">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span>
      <span class="af-box">4</span><span class="af-box">5</span><span class="af-box">6</span>
      <span class="af-box">7</span><span class="af-box">8</span><span class="af-box">9</span>
      <span class="af-box">10</span><span class="af-box">11</span><span class="af-box">12</span>
    </div>
    <span class="af-rowlabel"></span>
    <div class="af-scalebar">
      <span></span><span></span><span>&#8593;Ep</span>
      <span></span><span></span><span></span>
      <span></span><span>&#8593;M&middot;S</span><span></span>
      <span></span><span></span><span>&#8593;Sr</span>
    </div>
  </div>

  <h3>The Antagonist</h3>
  <div class="af-line"><label>Who / what</label><span class="af-fill"></span></div>
  <div class="af-line"><label>What it wants</label><span class="af-fill"></span></div>
  <p class="af-hint">Give it a face &mdash; even a force (a desert, a plague, a deadline) counts. When an Antagonist box fills, play out the Surge: the villain just hit a milestone of their own.</p>

  <h3>Milestones</h3>
  <p class="af-hint">A concrete, pointable step toward the Goal. Number them to match the Story Arc Track boxes above. (Episode uses 1&ndash;3; longer types fill more slowly.)</p>
  <div class="af-mscols">
    <div class="af-ms"><span class="af-num">1.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">7.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">2.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">8.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">3.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">9.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">4.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">10.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">5.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">11.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">6.</span><span class="af-fill"></span></div>
    <div class="af-ms"><span class="af-num">12.</span><span class="af-fill"></span></div>
  </div>

  <h3>Notes</h3>
  <div class="af-notes"></div>

  <p class="af-ref"><b>Win:</b> fill the Story Arc Track first &mdash; each hero takes +6 Readiness (cap 9). &nbsp; <b>Lose:</b> Antagonist Track fills first, or Quit the Story Arc &mdash; no penalty; ask "how did the world change?" and seed the next Story Arc. &nbsp; <b>Antagonist advances:</b> when heroes Flee a Challenge (always), or a telling failure via Pay the Price (table's call) &mdash; never automatic, never on Recovery.</p>
</div>
