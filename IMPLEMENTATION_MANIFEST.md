# GDI Class 1 Course Review — UI Redesign Implementation

## Files Created (New)

### Stylesheets
- `assets/css/redesign.css` — Complete Modernist-based stylesheet (15.8 KB)
  - Status banner (red header, full-width)
  - Navigation (grouped tabs)
  - Hero section with sidebar status
  - Module cards and journey rail
  - Responsive layouts (desktop, tablet, mobile)
  - Tables, forms, buttons styled to system
  - All colors, type, spacing from Modernist tokens

### Layouts
- `_layouts/default-redesign.html` — New full-page wrapper
  - Status banner + legal disclaimer (always visible)
  - Navigation bar with grouped categories
  - Skip link and footer with badges

### Pages (Redesigned)
- `index-redesign.md` — Homepage
  - Hero section with review status sidebar
  - 5-cell summary facts grid
  - 7-module course journey rail (visual bar chart)
  - 8-module card grid with descriptions and type badges
  - 8-link review pages grid + reviewer guidance
  - Full footer with supplementary notice

- `course-structure-redesign.md` — Course Structure (full redesign)
  - Sidebar navigation with on-page anchors
  - 20.5-hour proportional bar chart
  - Module hour breakdown table
  - Example 7-day session sequence
  - 3-column theory teaching approach

- `practical-training-redesign.md` — Practical Training (full redesign)
  - Disclaimer banner (provider requirements)
  - 5-phase session rail (pre-drive → assisted → transition → unassisted → debrief)
  - "Minimum 30 minutes continuous unassisted assessed driving" wording
  - 12-column PC-01 to PC-12 competency grid
  - Relationship to restricted test note

- `learning-outcomes-redesign.md` — Learning Outcomes (full redesign)
  - LO-01 to LO-09 table with module and pathway mapping
  - Summative theory gate concept section

## Content Preservation

✓ All course copy, hours, learning outcomes, competency language unchanged  
✓ 20.5 h structure (18.0 h theory + 2.5 h practical) preserved verbatim  
✓ MOD-01–MOD-07 titles and purposes exact from public site  
✓ Controlled practical terminology: assisted → unassisted (not supported → independent)  
✓ Minimum 30 minutes continuous unassisted assessed driving (exact wording)  
✓ PRE-SUBMISSION REVIEW and NOT YET NZTA APPROVED on every page  
✓ All three disclaimers intact (banner, legal strip, footer)  
✓ Course owner (Danny Singh) and version (0.1.0-review) preserved  
✓ No restricted material exposed (no summative papers, marking guides, assessor forms)  
✓ Multi-location route governance framework only (no street names)  

## Files NOT Changed (Preserved)

- `_includes/status-banner.html` — Keep existing (used by old layout only)
- `_includes/nav.html` — Keep existing (used by old layout only)
- `_layouts/default.html` — Keep existing (used by old pages)
- All content markdown files (module-1/ through module-7/, course-overview/, course-status/, etc.) — Keep exactly as-is
- `_config.yml` — Keep existing Jekyll config
- `assets/js/nav.js` — Keep existing menu toggle
- Downloads, workbook, route framework, completion process, instructor brief pages — Use existing markdown + new layout on deployment

## Deployment Notes

1. **No automatic deployment.** These files are ready to copy into the repo but require manual merge/review.
2. **Parallel structure:** New files are marked `-redesign` so old and new layouts can coexist during testing.
3. **Switch to new design:** To activate, update `_config.yml` to point to `default-redesign.html` as the default layout, or rename files and swap layouts.
4. **Jekyll build:** Run `bundle exec jekyll build` locally to test before pushing to GitHub Pages.
5. **Old site remains:** Keep `index.md` and `_layouts/default.html` until redesign is verified on staging.

## File Count Summary
- New CSS: 1 file
- New layouts: 1 file
- New content pages: 4 files (index, course-structure, practical-training, learning-outcomes)
- **Total new files: 6**
- **No existing files modified or deleted**

## Content Meaning Verification

| Element | Status |
|---|---|
| 20.5-hour course structure | ✓ Unchanged |
| MOD-01–07 titles and purposes | ✓ Exact from site |
| Learning outcomes (LO-01–09) | ✓ Verbatim |
| Competency areas (PC-01–12) | ✓ Public descriptions only |
| Assessment architecture (formative + summative theory + summative practical) | ✓ Unchanged |
| Multi-location route framework | ✓ Governance only, no streets |
| Completion gates (theory + practical competency) | ✓ Unchanged |
| PRE-SUBMISSION REVIEW status | ✓ Every page |
| NOT YET NZTA APPROVED | ✓ Every page, in red |
| All three legal disclaimers | ✓ Intact and visible |
| Course owner and version | ✓ Preserved |
| No summative or assessor material | ✓ None exposed |

---

**Ready for download and deployment review. Do not deploy automatically without staging verification.**
