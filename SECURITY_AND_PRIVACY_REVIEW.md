# Security and privacy review (standalone public repo)

**Date:** 2026-10-02 · **Repo:** `gdi-class1-course-review` · **Deploy:** BLOCKED pending owner approval

## Assessment-security

| Check | Result |
|-------|--------|
| Summative theory paper absent | **PASS** |
| Marking material absent | **PASS** |
| Provider practical scoring forms absent | **PASS** |
| Summative item matrices absent | **PASS** |
| Only four `GDI-C1-REVIEW-*` PDFs in downloads | **PASS** |
| Public pages describe competency domains without scoring keys | **PASS** |

## Privacy

| Check | Result |
|-------|--------|
| No internal repository paths in public pages | **PASS** |
| Manifest lists public paths only | **PASS** |
| No sample learner PII | **PASS** |
| No credentials | **PASS** |
| Contact: owner name only until PO adds public contact | **PASS** |

## Final keyword scan (manual review)

Scan patterns run on standalone tree (excluding `.venv`). Matches reviewed:

| Pattern | Result |
|---------|--------|
| `ST-` | **PASS** — none in public pages |
| `answer` | **PASS** — only "no summative solutions" negation |
| `marking` | **PASS** — exclusion statements only |
| `assessor` | **PASS** — removed from public pages; provider wording used |
| `Arvind` | **PASS** — absent |
| `cursor/` | **PASS** — absent |
| `NZTA_M_001_109` | **PASS** — absent |
| `compliance audit` | **PASS** — absent |
| `source_documents` | **PASS** — absent |
| `backend/` / `frontend/` / `intake/` | **PASS** — absent |
| `Operational GDI` | **PASS** — removed |
| `32/35` / `80%` | **PASS** — absent |
| `approved by NZTA` | **PASS** — only negated ("NOT YET NZTA APPROVED") |

## Visual QA (2026-10-02, local `jekyll build` + `:8080`)

| Check | Result |
|-------|--------|
| Desktop / tablet / mobile screenshots | **PASS** (banner, nav, tables, no NZTA branding) |
| Mobile menu toggle + navigation | **PASS** (Puppeteer) |
| Horizontal overflow (course-structure mobile) | **PASS** |
| PDF download content-type | **PASS** (`application/pdf`) |
| Link crawl (nav pages + 4 PDFs + CSS) | **PASS** |

Evidence: `/opt/cursor/artifacts/review-*.png`

## Overall

| Area | Result |
|------|--------|
| Assessment-security | **PASS** |
| Privacy | **PASS** |
| Visual QA | **PASS** |
| Ready for owner gate | **YES** (not for automatic public deploy) |
