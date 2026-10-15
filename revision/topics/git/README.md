# Git

**Status:** 🟡 basics done · **Sessions:** 10 Oct (no day folder; summary in [LEARNED.md](../../LEARNED.md#12-git-basics--10-oct)) · **Practice:** `D:/portfolio/git-sandbox` (outside this repo)
**Interview Qs:** [short answers](../../INTERVIEW-QA.md#git)
**Resources:** Corey Schafer *Git Tutorial for Beginners* (whole) · Pro Git ch. 2, 3.1–3.2, 6.2 (reference only)

## Must know
- edit → `add` (stage) → `commit` (local snapshot) → `push` (upload). Commit never uploads.
- `fetch` downloads only; `pull` = fetch + merge.
- Push rejected ("fetch first") → `git pull`, fix any conflict, push again.
- `.gitignore`: `.venv`, `.env`, data files, logs.
- Branches: `switch -c feature` → commits → push → pull request → review → merge → `branch -d`. `branch --merged` shows what's safe to delete.
- `reset` to unstage. Commit messages: Conventional Commits (`type(scope): summary`).

## Mistakes I made
- None recorded yet.

## Gaps
- [ ] A real merge conflict, resolved by hand (lab 01).
- [ ] A real pull request → merge (lab 01).
- [ ] **Shell basics** never studied: `cd`, `ls`, pipes `|`, `>` redirect, env vars, `which` (SKILLS-CHECKLIST ★★★ "Git + shell"; plan: Missing Semester lectures 1–2).
- [ ] No cheat sheet yet.
- [ ] Parked for the buffer week: stash, revert vs reset, rebase.
