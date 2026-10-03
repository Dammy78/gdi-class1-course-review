# Redesign staging routes (temporary)

**Branch:** `cursor/redesign-staging-qa-c28a`  
**Purpose:** Build and review the Claude redesign **in parallel** with production GitHub Pages URLs. Production pages are **not** overwritten until owner cutover.

## Staging URLs (temporary only)

| Redesign source file | Staging permalink | Production URL (unchanged until cutover) |
|----------------------|-------------------|------------------------------------------|
| `index-redesign.md` | `/staging/redesign/` | `/` (`index.md`) |
| `course-structure-redesign.md` | `/staging/redesign/course-structure/` | `/course-structure/` |
| `learning-outcomes-redesign.md` | `/staging/redesign/learning-outcomes/` | `/learning-outcomes/` |
| `practical-training-redesign.md` | `/staging/redesign/practical-training/` | `/practical-training/` |

All other pages (modules, downloads, etc.) remain on existing production paths. Redesign layout links to staging home and staging practical overview where noted in `_layouts/default-redesign.html`.

## Build behaviour

With staging permalinks, `bundle exec jekyll build` includes **both** production and redesign pages with **no duplicate-permalink warnings**.

## Final cutover (not executed in staging QA)

When approved (see `DEPLOYMENT_GATE.md`):

1. Point the four production URLs at redesign content (e.g. replace body/layout of production pages or swap filenames and permalinks to the **existing** production paths above).
2. Remove or archive `*-redesign.md` staging permalinks and delete `/staging/redesign/` routes from the public site map if no longer needed.
3. Update `_layouts/default-redesign.html` title/home and nav links from `/staging/redesign/…` back to production paths (`/`, `/practical-training/`, etc.).
4. Run full QA on production URLs; do **not** introduce new public route names at cutover—only the four URLs in the table.

**Do not merge or deploy automatically.**
