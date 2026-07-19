## Moves Cheatsheet

Every move in *Lights, Camera, Action!* on a single card. Print it and drop it in the middle of the table so nobody has to flip back through a chapter mid-scene.

Moves come in three families. **Action Moves** *resolve a hero's attempt* — you roll and read Strong / Weak / Miss. **Progress Moves** *open or close a track* — a Story Arc or a Challenge. **Frame Moves** *shift the fiction in the moment* — the dice point you in a direction, so you can never "fail" one.

> **Printing tip:** use your browser's **Print** command (or Save as PDF) on this page. The site menus are hidden automatically, so you'll get just the card.

<style>
.af-sheet {
  --af-ink: #1a1a1a;
  --af-muted: #6b6b6b;
  --af-line: #b9b3aa;
  --af-paper: #f3f0ec;
  max-width: 880px;
  margin: 1rem 0;
  padding: 1.4rem 1.6rem;
  border: 2.5px solid var(--af-ink);
  border-radius: 10px;
  background: #fff;
  color: var(--af-ink);
  box-shadow: 0 1px 6px rgba(0,0,0,0.12);
  font-family: inherit;
}
.af-sheet .af-title { margin: 0; font-size: 1.7rem; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; line-height: 1.05; }
.af-sheet .af-sub { margin: 0.2rem 0 1.1rem; font-size: 0.85rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--md-primary-fg-color); }
.af-legend { border: 1.8px solid var(--af-ink); border-radius: 8px; padding: 0.55rem 0.8rem; font-size: 0.82rem; line-height: 1.55; background: var(--af-paper); }
.af-legend b { color: var(--af-ink); }
.af-moves { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.9rem; }
.af-fam h3 { display: flex; align-items: center; gap: 0.6rem; margin: 0 0 0.2rem; padding: 0; border: 0; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; }
.af-fam h3::after { content: ""; flex: 1; height: 2px; background: var(--af-ink); }
.af-fam .af-famsub { font-size: 0.74rem; font-style: italic; color: var(--af-muted); margin: 0 0 0.55rem; }
.af-rightcol .af-fam.af-frame { margin-top: 0.9rem; }
.af-move { font-size: 0.8rem; line-height: 1.42; padding: 0.4rem 0.55rem; margin-bottom: 0.45rem; border: 1px solid #ddd; border-radius: 6px; border-left-width: 4px; border-left-color: var(--md-primary-fg-color); background: #fff; }
.af-mname { font-weight: 800; color: var(--md-primary-fg-color); }
.af-tier { font-size: 0.76rem; margin: 0.25rem 0 0 0.5rem; }
.af-tier b { display: inline-block; min-width: 2.6rem; color: var(--af-ink); }
.af-ref { font-size: 0.78rem; color: var(--af-muted); border-top: 2px solid var(--af-ink); margin-top: 0.9rem; padding-top: 0.55rem; }
.af-ref b { color: var(--md-primary-fg-color); }
@media (max-width: 640px) { .af-moves { grid-template-columns: 1fr; } }

@media print {
  .md-header, .md-tabs, .md-sidebar, .md-footer, .md-content__button, .md-nav { display: none !important; }
  .md-main__inner, .md-content { margin: 0 !important; }
  /* Print just the card: drop the page heading, intro prose, and printing tip. */
  .md-content__inner { margin: 0 !important; padding: 0 !important; }
  .md-content__inner > *:not(.af-sheet) { display: none !important; }
  .af-sheet { box-shadow: none !important; border-color: #000 !important; }
  /* Never split an individual move, the legend, or the footer across a page. */
  .af-move, .af-legend, .af-ref { break-inside: avoid; page-break-inside: avoid; }
  /* Keep a family heading with its first move. */
  .af-fam h3 { break-after: avoid; page-break-after: avoid; }
  /* The screen layout is a 2-column grid of two giant cells (all Action in one,
     Progress+Frame in the other). A grid cell taller than a page fragments
     unreliably and slices move boxes in half; CSS multi-columns paginate no better,
     and flattening the wrappers with display:contents trips a Chrome print bug that
     drops the body text. The robust fix: for print, flow the moves as one linear,
     full-width column — each box paginates as an atomic block, so a move is never
     cut across a page. */
  .af-moves { display: block !important; margin-top: 0.5rem; }
  .af-rightcol { display: contents; }
  .af-fam + .af-fam, .af-rightcol .af-fam { margin-top: 0.7rem; }
  /* Break the card cleanly: Action Moves on page 1, Progress + Frame on page 2. */
  .af-fam.af-progress { break-before: page; page-break-before: always; margin-top: 0; }
  /* Tighten spacing so each half stays on a single page (Progress + Frame + footer
     must not push a move to a third page). */
  .af-sheet { padding: 0.6rem 0.85rem; }
  .af-sheet .af-title { font-size: 1.3rem; }
  .af-legend { font-size: 0.72rem; line-height: 1.34; padding: 0.38rem 0.55rem; }
  .af-fam .af-famsub { font-size: 0.72rem; margin-bottom: 0.3rem; }
  .af-move { font-size: 0.72rem; line-height: 1.3; padding: 0.26rem 0.46rem; margin-bottom: 0.26rem; }
  .af-tier { font-size: 0.71rem; margin-top: 0.16rem; }
  .af-fam h3 { font-size: 0.96rem; margin-bottom: 0.05rem; }
}
</style>

<div class="af-sheet" markdown="0">
  <p class="af-title">LIGHTS, CAMERA, ACTION!</p>
  <p class="af-sub">Moves Cheatsheet</p>

  <div class="af-legend">
    <b>THE ROLL:</b> 2d6 &mdash; <b>+1</b> if a fitting Stat, <b>+1</b> if a fitting Asset (<b>+2</b> both, <b>+0</b> neither).
    &nbsp;&middot;&nbsp; <b>10+</b> Strong Hit &nbsp; <b>7&ndash;9</b> Weak Hit &nbsp; <b>6&minus;</b> Miss.
    &nbsp;&middot;&nbsp; <b>Doubles</b>: upgrade a Hit one tier (a Strong Hit &rarr; Outstanding Success: +1 to your next roll, and <b>fill 2 boxes</b> in a Challenge); a Miss on doubles advances the antagonist.
    &nbsp;&middot;&nbsp; A Hit means you <b>narrate the change</b>.
    <br>
    <b>READINESS</b> (starts at 9, your max all game): Weak Hit <b>&minus;1</b>, Miss <b>&minus;2</b> <i>(at 4&ndash;5 heroes, &minus;2 / &minus;3)</i>. At <b>0</b> you're Out of Action: sit out the rest of the Scene, break one Asset (until Downtime), and the antagonist advances one box.
  </div>

  <div class="af-moves">
    <div class="af-fam af-action">
      <h3>Action Moves</h3>
      <p class="af-famsub">Resolve a hero's attempt &mdash; roll 2d6 +0/+1/+2, read Strong / Weak / Miss.</p>

      <div class="af-move"><span class="af-mname">The Roll.</span> The core move &mdash; any risky action. Run it with <b>no track</b> (a Regular Roll) or to <b>mark a track</b> (a Challenge Roll). Every other move grows from it.</div>

      <div class="af-move"><span class="af-mname">Aid Your Ally.</span> Point the roll at a teammate. <b>Strong:</b> ally gets +2. <b>Weak:</b> ally +1, you &minus;1. <b>Miss:</b> nothing, you &minus;2.</div>

      <div class="af-move"><span class="af-mname">Prepare.</span> Aid aimed at <i>yourself</i> &mdash; scout, study, set a trap. Same roll; the bonus waits and lands on the first roll of the moment you prepped. <b>Strong:</b> +2. <b>Weak:</b> +1, you &minus;1. <b>Miss:</b> nothing, you &minus;2.</div>

      <div class="af-move"><span class="af-mname">Devil's Bargain.</span> On a <b>Miss</b> only: refuse the Readiness loss <i>and</i> upgrade the Miss to a <b>Strong Hit</b> &mdash; in exchange for the <b>Antagonist Track +1 box</b>. Always optional. <b>Not</b> allowed on a Miss that would knock you Out of Action.</div>

      <div class="af-move"><span class="af-mname">Mend.</span> Any scene, on your turn (in a Challenge, instead of a Challenge Roll) &mdash; patch self or an ally. <b>Strong</b> +3 &middot; <b>Weak</b> +2 &middot; <b>Miss</b> &minus;1 Readiness. Capped at 9; can't revive a downed hero.</div>

      <div class="af-move"><span class="af-mname">Recovery Scene.</span> Fall back &amp; regroup at a lull: the party heals fully back to <b>9</b> &mdash; no roll, automatic. Falling back is always safe.</div>

      <div class="af-move"><span class="af-mname">Downtime.</span> Between Story Arcs: everyone heals to full <b>9</b>, Broken Assets restored. Free.</div>
    </div>

    <div class="af-rightcol">
    <div class="af-fam af-progress">
      <h3>Progress Moves</h3>
      <p class="af-famsub">Open or close a track &mdash; a Story Arc or a Challenge.</p>

      <div class="af-move"><span class="af-mname">Lights, Camera, Action.</span> One <b>d6</b> oracle roll when a Story Arc begins (no Stat/Asset; generative &mdash; can't fail). It sets how the adventure opens:
        <div class="af-tier"><b>5&ndash;6</b> <i>Clear purpose</i> &mdash; they know exactly what to do; open <i>in medias res</i> on the first Milestone.</div>
        <div class="af-tier"><b>3&ndash;4</b> <i>A general idea</i> &mdash; they know the goal, not yet how to act on it.</div>
        <div class="af-tier"><b>1&ndash;2</b> <i>Trouble finds you first</i> &mdash; open in the thick of it, likely mid-Challenge.</div>
      </div>

      <div class="af-move"><span class="af-mname">Start a Challenge.</span> Opening any Challenge: name the goal, choose a difficulty (Normal 3 / Hard 6 / Epic 9) &amp; draw the track, then <b>each player rolls a d6</b> (no Stat/Asset; generative) for a one-time nudge to <i>their</i> first roll. <b>5&ndash;6</b> +1 &middot; <b>3&ndash;4</b> 0 &middot; <b>1&ndash;2</b> &minus;1.</div>

      <div class="af-move"><span class="af-mname">Fall back.</span> Retreat from a Challenge (lose its progress) and take a Recovery Scene &mdash; the party heals fully back to 9. The stay-alive valve.</div>

      <div class="af-move"><span class="af-mname">Quit the Story Arc.</span> The terminal fall back &mdash; give up the whole Story Arc. No penalty and no bonus; the loss seeds your next Story Arc.</div>
    </div>

    <div class="af-fam af-frame">
      <h3>Frame Moves</h3>
      <p class="af-famsub">Shift the fiction in the moment &mdash; the dice point a direction. You can't fail a Frame Move.</p>

      <div class="af-move"><span class="af-mname">Ask the Oracle.</span> Stuck on what's next? Name the next Milestone &rarr; do the obvious thing, or roll the <b>Story Spark</b> (d6 idea table) or <b>Ask the Dice</b> (1d6 yes/no).</div>

      <div class="af-move"><span class="af-mname">Pay the Price.</span> Turn a Weak Hit or Miss into a fiction complication + the Readiness loss. The antagonist advances only via a <b>Devil's Bargain</b>, a <b>Miss on doubles</b>, or a hero going <b>Out of Action</b>.</div>
    </div>
    </div>
  </div>

  <p class="af-ref"><b>Full rules:</b> The Roll, Aid Your Ally &amp; Prepare &mdash; Ch.7. &nbsp; Challenges, Start a Challenge &amp; Fall back &mdash; Ch.8. &nbsp; Readiness, Mend, Recovery Scene, Downtime &amp; Pay the Price &mdash; Ch.9. &nbsp; Story Arcs, Lights, Camera, Action &amp; Quit the Story Arc &mdash; Ch.10. &nbsp; Ask the Oracle &mdash; Ch.11.</p>
</div>
