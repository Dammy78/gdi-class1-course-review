# gdi-class1-course-review

Static, **read-only** public review site for a Class 1 learner licence course (course owner: Danny Singh).

**Not an NZTA website.** **Not NZTA-approved.** Supplementary to the formal NZTA submission package.

## Status

Prepared for deployment — **GitHub Pages not enabled** until `DEPLOYMENT_GATE.md` approval.

## Local preview

```bash
cd gdi-class1-course-review
bundle install
bundle exec jekyll serve --baseurl ""
```

Open `http://127.0.0.1:4000/`

## Review PDFs (maintainers)

```bash
python3 -m venv .venv && .venv/bin/pip install fpdf2
.venv/bin/python scripts/build_review_pdfs.py
```

Do not commit `.venv/`.

## GitHub Pages (after owner approval)

- Repository: `gdi-class1-course-review`
- `baseurl`: `/gdi-class1-course-review`
- URL: `https://dammy78.github.io/gdi-class1-course-review/`
- Settings → Pages → `main` / root → Jekyll

## Governance

| File | Purpose |
|------|---------|
| `PUBLIC_REVIEW_MANIFEST.md` | Public artefact whitelist |
| `PUBLIC_DOWNLOAD_MANIFEST.md` | Allowed PDFs only |
| `SECURITY_AND_PRIVACY_REVIEW.md` | Pre-deploy scan record |
| `DEPLOYMENT_GATE.md` | Owner sign-off required |

Initial publish should be a **new repository** with **no imported history** from private development workspaces.
