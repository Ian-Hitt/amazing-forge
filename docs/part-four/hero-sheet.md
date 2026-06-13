## Hero Sheet

Everything a hero needs fits on one page. Print or photocopy this sheet, or just copy the layout onto a scrap of paper — a Concept, four Assets, your Readiness, and a Growth Track is the whole character.

> **Printing tip:** use your browser's **Print** command (or Save as PDF) on this page. The site menus and navigation are hidden automatically, so you'll get just the sheet. One sheet per hero.

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
.af-assets { display: grid; grid-template-columns: 1fr 1fr; gap: 0.6rem 1.2rem; }
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
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">LIGHTS, CAMERA, ACTION!</p>
  <p class="af-sub">Hero Sheet</p>

  <div class="af-line"><label>Hero Name</label><span class="af-fill"></span><label>Player</label><span class="af-fill"></span></div>

  <h3>Concept</h3>
  <div class="af-line"><span class="af-fill"></span></div>
  <p class="af-hint">[An Adjective, Species, or Twist] + [a Class, Job, or Role] — your hero's one-line movie-poster pitch.</p>

  <h3>Assets</h3>
  <p class="af-hint">Four things your hero is amazing at. An Asset that fits a roll adds +2. Build a hero by answering four questions in order: your <b>Attribute</b> (the one broad pick — <b>Strong · Quick · Clever · Sneaky · Charming</b>, max one), a <b>Skill</b>, a signature <b>Item/Companion</b>, and a <b>Wild</b> pick. Swap 2&ndash;4 freely if your concept wants. Spend 2 Growth on a Boon (a signature move on an Asset, max 2 each). Check <b>Broken</b> when an Asset is knocked out at 0 Readiness — it gives no +2 until Downtime restores it.</p>
  <div class="af-assets">
    <div class="af-asset">
      <span class="af-hint" style="display:block;margin-bottom:0.2rem;">1. Attribute (circle one): Strong · Quick · Clever · Sneaky · Charming</span>
      <span class="af-fill"></span>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
    <div class="af-asset">
      <span class="af-hint" style="display:block;margin-bottom:0.2rem;">2. Skill or Expertise</span>
      <span class="af-fill"></span>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
    <div class="af-asset">
      <span class="af-hint" style="display:block;margin-bottom:0.2rem;">3. Item, Companion, or Connection</span>
      <span class="af-fill"></span>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
    <div class="af-asset">
      <span class="af-hint" style="display:block;margin-bottom:0.2rem;">4. Wild (your call — not a 2nd Attribute)</span>
      <span class="af-fill"></span>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-boon"><span class="af-box"></span><span class="af-fill"></span></div>
      <div class="af-broken"><span class="af-box"></span> Broken</div>
    </div>
  </div>

  <h3>Readiness</h3>
  <p class="af-hint">Start at 9. Cross off as it drops — Weak Hit &minus;1, Miss &minus;2. At 0 you're Out of Action and one Asset breaks. <b>Mend</b> (in a Challenge, self or ally): Strong +3 / Weak +2 / Miss &minus;1; no villain surge, can't revive a downed hero. <b>Recovery Scene</b> (fall back to regroup): recover up to your current max — but the villain surges one box, <b>and your max drops by 1</b>. <b>Your max starts at 9 and drops 1 each Recovery Scene</b> (floor 4) — circle it and slide it down; it resets to 9 at <b>Downtime</b> (between Story Arcs), which also restores Broken Assets.</p>
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
  <p class="af-hint">Every 3rd Milestone the party marks (on any Story Arc), each hero fills one box (1 Growth). Spend 2 on a Boon, 5 on a New Asset (ceiling 6 — Trade In to exceed).</p>
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

  <p class="af-ref"><b>The Roll:</b> 2d6, +2 if an Asset fits / +1 otherwise. &nbsp; <b>10+</b> Strong Hit &middot; <b>7&ndash;9</b> Weak Hit &middot; <b>6&minus;</b> Miss. &nbsp; Doubles upgrade one tier (Oracle's Blessing). A Hit means you narrate the change.</p>
</div>
