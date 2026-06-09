## Moves Cheatsheet

Every move in *Amazing Forge* on a single card. Print it and drop it in the middle of the table so nobody has to flip back through a chapter mid-scene.

Moves come in three families. **Action Moves** *resolve a hero's attempt* — you roll and read Strong / Weak / Miss. **Progress Moves** *open or close a track* — a Quest or a Challenge. **Frame Moves** *shift the fiction in the moment* — the dice point you in a direction, so you can never "fail" one.

> **Printing tip:** use your browser's **Print** command (or Save as PDF) on this page. The site menus are hidden automatically, so you'll get just the card.

<style>
@media print {
  .md-header, .md-tabs, .md-sidebar, .md-footer, .md-content__button, .md-nav { display: none !important; }
  .md-main__inner, .md-content { margin: 0 !important; }
  .af-sheet { box-shadow: none !important; border-color: #000 !important; }
}
.af-sheet {
  border: 2px solid #d35400;
  border-radius: 8px;
  padding: 1.1rem 1.3rem;
  max-width: 880px;
  font-family: inherit;
}
.af-sheet .af-title { text-align: center; font-size: 1.5rem; font-weight: 700; letter-spacing: 0.04em; margin: 0; }
.af-sheet .af-sub { text-align: center; font-size: 0.85rem; opacity: 0.7; margin: 0.1rem 0 0.7rem; }
.af-legend { border: 1.5px solid #d35400; border-radius: 6px; padding: 0.5rem 0.75rem; font-size: 0.82rem; line-height: 1.55; background: rgba(211,84,0,0.05); }
.af-legend b { color: #d35400; }
.af-moves { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.9rem; }
.af-fam h3 { margin: 0 0 0.1rem; padding-bottom: 0.2rem; border-bottom: 2px solid; font-size: 1.05rem; }
.af-fam .af-famsub { font-size: 0.74rem; font-style: italic; opacity: 0.75; margin: 0 0 0.55rem; }
.af-action h3 { border-color: #d35400; color: #d35400; }
.af-progress h3 { border-color: #2e7d32; color: #2e7d32; }
.af-frame h3 { border-color: #2c6e8f; color: #2c6e8f; }
.af-rightcol .af-fam.af-frame { margin-top: 0.9rem; }
.af-move { font-size: 0.8rem; line-height: 1.42; padding: 0.4rem 0.55rem; margin-bottom: 0.45rem; border: 1px solid #ccc; border-radius: 6px; border-left-width: 4px; }
.af-action .af-move { border-left-color: #d35400; }
.af-progress .af-move { border-left-color: #2e7d32; }
.af-frame .af-move { border-left-color: #2c6e8f; }
.af-mname { font-weight: 700; }
.af-tier { font-size: 0.76rem; margin: 0.25rem 0 0 0.5rem; }
.af-tier b { display: inline-block; min-width: 2.6rem; }
.af-ref { font-size: 0.78rem; opacity: 0.85; border-top: 1px dashed #aaa; margin-top: 0.9rem; padding-top: 0.55rem; }
.af-ref b { color: #d35400; }
@media (max-width: 640px) { .af-moves { grid-template-columns: 1fr; } }
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">AMAZING FORGE</p>
  <p class="af-sub">Moves Cheatsheet</p>

  <div class="af-legend">
    <b>THE ROLL:</b> 2d6 &mdash; <b>+2</b> if an Asset fits, <b>+1</b> otherwise.
    &nbsp;&middot;&nbsp; <b>10+</b> Strong Hit &nbsp; <b>7&ndash;9</b> Weak Hit &nbsp; <b>6&minus;</b> Miss.
    &nbsp;&middot;&nbsp; <b>Doubles</b> upgrade one tier (Oracle's Blessing).
    &nbsp;&middot;&nbsp; A Hit means you <b>narrate the change</b>.
    <br>
    <b>READINESS</b> (max 9): Weak Hit <b>&minus;1</b>, Miss <b>&minus;2</b> &mdash; always. At <b>0</b> you're Out of Action and one Asset breaks until Downtime.
  </div>

  <div class="af-moves">
    <div class="af-fam af-action">
      <h3>Action Moves</h3>
      <p class="af-famsub">Resolve a hero's attempt &mdash; roll 2d6 +2/+1, read Strong / Weak / Miss.</p>

      <div class="af-move"><span class="af-mname">The Roll.</span> The core move &mdash; any risky action. Run it with <b>no track</b> (a Regular Roll) or to <b>mark a track</b> (a Challenge Roll). Every other move grows from it.</div>

      <div class="af-move"><span class="af-mname">Aid Your Ally.</span> Point the roll at a teammate. <b>Strong:</b> ally gets +2. <b>Weak:</b> ally +1, you &minus;1. <b>Miss:</b> nothing, you &minus;2.</div>

      <div class="af-move"><span class="af-mname">Mend.</span> Short rest, in a lull &mdash; self or an ally, once per hero per Milestone. <b>Strong</b> +3 &middot; <b>Weak</b> +2 &middot; <b>Miss</b> no heal + a complication.</div>

      <div class="af-move"><span class="af-mname">Downtime.</span> Long rest between adventures, one group roll. <b>Strong</b> +7 &middot; <b>Weak</b> +6 &middot; <b>Miss</b> +6 + you owe a Quest. Restores Broken Assets. Finishing a Quest prompts one.</div>

      <div class="af-move"><span class="af-mname">Showdown</span> <i>(optional).</i> A climactic last-box roll on a Challenge or Quest Track. A <b>Miss</b> escalates the story instead of ending it &mdash; never an outright loss, never advances the Antagonist Track.</div>
    </div>

    <div class="af-rightcol">
    <div class="af-fam af-progress">
      <h3>Progress Moves</h3>
      <p class="af-famsub">Open or close a track &mdash; a Quest or a Challenge.</p>

      <div class="af-move"><span class="af-mname">Start a Quest.</span> One <b>2d6 + 1</b> roll when a Quest begins (no Asset; generative). It sets how the adventure opens:
        <div class="af-tier"><b>10+</b> <i>Clear purpose</i> &mdash; you're in control and move first.</div>
        <div class="af-tier"><b>7&ndash;9</b> <i>More questions than answers</i> &mdash; open with one complication already in play.</div>
        <div class="af-tier"><b>6&minus;</b> <i>Trouble finds you first</i> &mdash; open in the thick of it, likely mid-Challenge.</div>
      </div>

      <div class="af-move"><span class="af-mname">Start a Challenge.</span> When you <i>choose</i> to open a Challenge, one <b>2d6 + 1</b> roll (no Asset; generative) sets the jump &mdash; a one-time edge on the <b>first roll</b> only. <b>10+</b> +1 (you got the drop) &middot; <b>7&ndash;9</b> 0 (even) &middot; <b>6&minus;</b> &minus;1 (they beat you to it). Skip it if trouble is thrust on you.</div>

      <div class="af-move"><span class="af-mname">Flee.</span> Abandon a Challenge (lose its progress) to stop the Readiness bleed and mark <b>one</b> Antagonist box. The stay-alive valve.</div>

      <div class="af-move"><span class="af-mname">Quit the Quest.</span> The terminal Flee &mdash; give up the whole Quest. No penalty and no bonus; the loss seeds your next Quest.</div>
    </div>

    <div class="af-fam af-frame">
      <h3>Frame Moves</h3>
      <p class="af-famsub">Shift the fiction in the moment &mdash; the dice point a direction. You can't fail a Frame Move.</p>

      <div class="af-move"><span class="af-mname">Ask the Oracle.</span> Stuck on what's next? Name the next Milestone &rarr; do the obvious thing, or roll the <b>Story Spark</b> (d6 idea table) or <b>Ask the Dice</b> (1d6 yes/no).</div>

      <div class="af-move"><span class="af-mname">Pay the Price.</span> Turn a Weak Hit or Miss into a fiction complication. On a telling failure it <i>may</i> tick the Antagonist Track &mdash; the table's call, never automatic, never on a recovery move.</div>
    </div>
    </div>
  </div>

  <p class="af-ref"><b>Full rules:</b> The Roll &amp; Aid Your Ally &mdash; Ch.7. &nbsp; Challenges, Start a Challenge, Flee &amp; Showdown &mdash; Ch.8. &nbsp; Readiness, Mend, Downtime &amp; Pay the Price &mdash; Ch.9. &nbsp; Quests, Start a Quest &amp; Quit the Quest &mdash; Ch.10. &nbsp; Ask the Oracle &mdash; Ch.11.</p>
</div>
