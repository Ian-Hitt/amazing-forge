## Challenge Tracker Sheet

A scratch sheet for the Challenges you draw mid-Story — a fight, a chase, an infiltration, a tense scene of words. Each block is one Challenge: name it, pick its size, and fill the boxes roll by roll. When the track fills the Challenge is won — cross it out and reuse the sheet, or start a fresh one. Challenges are disposable; this just saves you scribbling a row of boxes on scrap paper.

> **Printing tip:** use your browser's **Print** command (or Save as PDF) on this page. The site menus are hidden automatically, so you'll get just the sheet. Print several for a Challenge-heavy session.

See **Challenges** ([Chapter 8](../part-two/08-challenges.md)) for the full procedure.

<style>
.af-sheet {
  border: 2px solid #d35400;
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  max-width: 760px;
  font-family: inherit;
}
.af-sheet .af-title { text-align: center; font-size: 1.5rem; font-weight: 700; letter-spacing: 0.04em; margin: 0; }
.af-sheet .af-sub { text-align: center; font-size: 0.85rem; opacity: 0.7; margin: 0.1rem 0 0.7rem; }
.af-legend { border: 1.5px solid #d35400; border-radius: 6px; padding: 0.5rem 0.75rem; font-size: 0.82rem; line-height: 1.55; background: rgba(211,84,0,0.05); }
.af-legend b { color: #d35400; }
.af-fill { flex: 1; border-bottom: 1.5px solid #888; min-height: 1.3rem; }
.af-hint { font-size: 0.8rem; opacity: 0.7; font-style: italic; }
.af-chal { border: 1px solid #bbb; border-radius: 6px; padding: 0.55rem 0.7rem; margin-top: 0.7rem; }
.af-chal-head { display: flex; align-items: flex-end; gap: 0.5rem; flex-wrap: wrap; }
.af-chal-num { font-weight: 700; color: #d35400; font-size: 1rem; }
.af-chal-head label { font-weight: 700; white-space: nowrap; }
.af-chal-head .af-fill { min-width: 8rem; }
.af-diff { font-size: 0.78rem; font-weight: 600; white-space: nowrap; }
.af-diff .af-chk { width: 0.85rem; height: 0.85rem; border: 1.5px solid #555; border-radius: 3px; display: inline-block; vertical-align: -1px; margin: 0 0.1rem 0 0.45rem; }
.af-chal-track { display: flex; align-items: center; gap: 0.3rem; flex-wrap: nowrap; margin: 0.5rem 0 0.2rem; }
.af-boxlabel { font-weight: 700; white-space: nowrap; margin-left: 0.6rem; flex: 0 0 auto; }
.af-box { display: inline-block; width: 1.55rem; height: 1.55rem; border: 1.5px solid #555; border-radius: 4px; text-align: center; line-height: 1.55rem; font-size: 0.72rem; flex: 0 0 auto; }
.af-chal-track .af-show { border-color: #d35400; border-width: 2px; color: #d35400; }
.af-chal-track .af-arrow { font-size: 0.75rem; opacity: 0.7; margin-left: 0.1rem; }
.af-ref { font-size: 0.8rem; opacity: 0.85; border-top: 1px dashed #aaa; margin-top: 1rem; padding-top: 0.6rem; }
.af-ref b { color: #d35400; }

@media print {
  .md-header, .md-tabs, .md-sidebar, .md-footer, .md-content__button, .md-nav { display: none !important; }
  .md-main__inner, .md-content { margin: 0 !important; }
  /* Print just the sheet: drop the page heading, intro prose, chapter link, and printing tip. */
  .md-content__inner { margin: 0 !important; padding: 0 !important; }
  .md-content__inner > *:not(.af-sheet) { display: none !important; }
  .af-sheet { box-shadow: none !important; border-color: #000 !important; }
  /* Never split a legend, a Challenge block, or the footer across a page. */
  .af-legend, .af-chal, .af-ref { break-inside: avoid; page-break-inside: avoid; }
  /* Compact so the whole sheet fits on one printed page. */
  .af-sheet { padding: 0.65rem 0.9rem; max-width: none; }
  .af-sheet .af-title { font-size: 1.3rem; }
  .af-sheet .af-sub { margin-bottom: 0.4rem; }
  .af-legend { font-size: 0.7rem; line-height: 1.32; padding: 0.35rem 0.55rem; }
  .af-chal { padding: 0.28rem 0.55rem; margin-top: 0.3rem; }
  .af-chal-head { font-size: 0.92rem; }
  .af-chal-track { margin: 0.26rem 0 0.22rem; }
  .af-box { width: 1.35rem; height: 1.35rem; line-height: 1.35rem; font-size: 0.7rem; }
  .af-boxlabel { font-size: 0.78rem; }
  .af-fill { min-height: 1.1rem; }
}
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">LIGHTS, CAMERA, ACTION!</p>
  <p class="af-sub">Challenge Tracker</p>

  <div class="af-legend">
    <b>START A CHALLENGE</b> (only when you pick the fight): roll <b>2d6 + 1</b> &rarr; <b>10+</b> +1 &middot; <b>7&ndash;9</b> 0 &middot; <b>6&minus;</b> &minus;1 &mdash; a one-time edge on your <b>first roll</b> only.
    <br>
    <b>EACH ROLL:</b> <b>Strong</b> fill 1 box &middot; <b>Weak</b> fill 1 box, &minus;1 Readiness &middot; <b>Miss</b> no box, &minus;2 Readiness <i>or</i> take the <b>Devil's Bargain</b> (upgrade to a Strong Hit, refuse the loss &rarr; antagonist +1 box; not if it would knock you Out of Action). A <b>Miss on doubles</b> also advances the antagonist.
    <br>
    <b>SIZE</b> (the same at any party size): Easy = <b>2</b> &middot; Medium = <b>3</b> &middot; Hard = <b>4</b> &middot; Very Hard = <b>5</b> (climaxes only) boxes &mdash; cross out the ones you don't use. The last box can be a <b>Showdown (&#9733;)</b>. Track fills &rarr; Challenge won &mdash; wipe it. A Challenge is <i>not</i> a Milestone. Fall back = a Recovery Scene (lose progress; recovery is <b>free</b>).
    <br>
    <b>TYPES:</b> Combat &middot; Journey &middot; Stealth &middot; Investigation &middot; Social &mdash; same boxes-and-rolls, only the fiction changes. For each, ask: <i>what's one box, which Assets fit, what's the price on a Weak Hit or Miss?</i>
  </div>

  <div class="af-chal">
    <div class="af-chal-head">
      <span class="af-chal-num">1.</span><label>Challenge</label><span class="af-fill"></span>
      <span class="af-diff">Size:<span class="af-chk"></span>Easy<span class="af-chk"></span>Med<span class="af-chk"></span>Hard</span>
    </div>
    <div class="af-chal-track">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span><span class="af-box">4</span><span class="af-box">5</span><span class="af-box af-show">&#9733;</span>
      <label class="af-boxlabel">A box =</label><span class="af-fill"></span>
    </div>
  </div>

  <div class="af-chal">
    <div class="af-chal-head">
      <span class="af-chal-num">2.</span><label>Challenge</label><span class="af-fill"></span>
      <span class="af-diff">Size:<span class="af-chk"></span>Easy<span class="af-chk"></span>Med<span class="af-chk"></span>Hard</span>
    </div>
    <div class="af-chal-track">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span><span class="af-box">4</span><span class="af-box">5</span><span class="af-box af-show">&#9733;</span>
      <label class="af-boxlabel">A box =</label><span class="af-fill"></span>
    </div>
  </div>

  <div class="af-chal">
    <div class="af-chal-head">
      <span class="af-chal-num">3.</span><label>Challenge</label><span class="af-fill"></span>
      <span class="af-diff">Size:<span class="af-chk"></span>Easy<span class="af-chk"></span>Med<span class="af-chk"></span>Hard</span>
    </div>
    <div class="af-chal-track">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span><span class="af-box">4</span><span class="af-box">5</span><span class="af-box af-show">&#9733;</span>
      <label class="af-boxlabel">A box =</label><span class="af-fill"></span>
    </div>
  </div>

  <div class="af-chal">
    <div class="af-chal-head">
      <span class="af-chal-num">4.</span><label>Challenge</label><span class="af-fill"></span>
      <span class="af-diff">Size:<span class="af-chk"></span>Easy<span class="af-chk"></span>Med<span class="af-chk"></span>Hard</span>
    </div>
    <div class="af-chal-track">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span><span class="af-box">4</span><span class="af-box">5</span><span class="af-box af-show">&#9733;</span>
      <label class="af-boxlabel">A box =</label><span class="af-fill"></span>
    </div>
  </div>

  <div class="af-chal">
    <div class="af-chal-head">
      <span class="af-chal-num">5.</span><label>Challenge</label><span class="af-fill"></span>
      <span class="af-diff">Size:<span class="af-chk"></span>Easy<span class="af-chk"></span>Med<span class="af-chk"></span>Hard</span>
    </div>
    <div class="af-chal-track">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span><span class="af-box">4</span><span class="af-box">5</span><span class="af-box af-show">&#9733;</span>
      <label class="af-boxlabel">A box =</label><span class="af-fill"></span>
    </div>
  </div>

  <div class="af-chal">
    <div class="af-chal-head">
      <span class="af-chal-num">6.</span><label>Challenge</label><span class="af-fill"></span>
      <span class="af-diff">Size:<span class="af-chk"></span>Easy<span class="af-chk"></span>Med<span class="af-chk"></span>Hard</span>
    </div>
    <div class="af-chal-track">
      <span class="af-box">1</span><span class="af-box">2</span><span class="af-box">3</span><span class="af-box">4</span><span class="af-box">5</span><span class="af-box af-show">&#9733;</span>
      <label class="af-boxlabel">A box =</label><span class="af-fill"></span>
    </div>
  </div>
</div>
