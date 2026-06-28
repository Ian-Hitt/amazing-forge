# Editing from your phone (GitJournal)

Quick reference for editing the book on Android via GitJournal. The git repo is the
source of truth and the backup — every push to `main` auto-builds and deploys the live
site in ~1 minute.

## Setup (one time)

1. Install **GitJournal** from the Play Store (free git-sync is enough).
2. Connect to **GitHub** → authorize → select the **`Ian-Hitt/amazing-forge`** repo.
3. **Settings → Root Folder → `docs`** so the file list opens into the chapters.
4. **Settings → Editor → Markdown / Raw** (not the journal-style note editor).
5. **Settings → Sort Order → File Name, Ascending** so chapters sort `00-`, `01-`, `02-`…
6. **Turn OFF auto-sync.** Sync manually instead (see below).
7. **Turn OFF swipe gestures** (swipe-to-delete + auto-sync once deleted a whole chapter).

## Daily workflow

1. **Pull first** — tap sync when you open the app, before editing. This avoids merge
   conflicts with edits made on the computer.
2. Edit text.
3. **Glance at what changed, then tap sync** to push. With auto-sync off, an accidental
   change stays on your phone until you choose to push it.

## Safety notes

- **Manual sync is the safeguard.** Nothing reaches GitHub (or the live site) until you
  sync, so you get a chance to catch mistakes first.
- **GitHub is the undo button.** Anything pushed is recoverable from git history — a bad
  push is a scare, not a loss. Restore a deleted/changed file from the computer with git.
- **Don't edit the same file on phone and computer without syncing between** — pull first,
  every time.

## Expected quirks (not bugs)

- `!!!` admonitions and `.lca-move` move cards show as **raw text** in the editor. That's
  correct — don't "fix" them.
- The **genre files** (`adventure.md`, `mystery.md`, …) have no number prefixes, so they
  sort alphabetically instead of in book order. Expected.
