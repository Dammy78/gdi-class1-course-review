#!/usr/bin/env python3
"""Build PUBLIC review PDFs only. Maintainer script — not a site page."""
from pathlib import Path

try:
    from fpdf import FPDF
except ImportError:
    raise SystemExit("Install fpdf2 in a local venv")

ROOT = Path(__file__).resolve().parents[1]
DOWN = ROOT / "downloads"
DOWN.mkdir(exist_ok=True)

BANNER = (
    "PRE-SUBMISSION REVIEW | NOT YET NZTA APPROVED | "
    "Independent review site — not an NZTA website | "
    "Course version 0.1.0-review | Owner: Danny Singh"
)


def ascii_safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def md_to_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        raw = parts[2] if len(parts) > 2 else raw
    return raw


def write_pdf(name: str, md_path: Path) -> None:
    pdf = FPDF()
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    w = pdf.w - pdf.l_margin - pdf.r_margin
    pdf.set_font("Helvetica", size=9)
    pdf.multi_cell(w, 5, ascii_safe(BANNER))
    pdf.ln(4)
    pdf.set_font("Helvetica", size=10)
    for line in md_to_text(md_path).splitlines():
        line = line.strip()
        if not line or line.startswith("|--"):
            continue
        if line.startswith("|"):
            line = "  ".join(c.strip() for c in line.strip("|").split("|") if c.strip())
        if line.startswith("{{"):
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            pdf.set_font("Helvetica", "B", 14 - min(level, 2))
            pdf.multi_cell(w, 6, ascii_safe(line.lstrip("# ").strip()))
            pdf.set_font("Helvetica", size=10)
            continue
        pdf.multi_cell(w, 5, ascii_safe(line))
    out = DOWN / name
    pdf.output(str(out))
    print("Wrote", out)


JOBS = [
    ("GDI-C1-REVIEW-001-course-overview.pdf", "course-overview/index.md"),
    ("GDI-C1-REVIEW-002-learning-outcomes.pdf", "learning-outcomes/index.md"),
    ("GDI-C1-REVIEW-003-course-structure.pdf", "course-structure/index.md"),
    ("GDI-C1-REVIEW-004-instructor-brief.pdf", "instructor-brief/index.md"),
]

if __name__ == "__main__":
    for pdf_name, rel in JOBS:
        write_pdf(pdf_name, ROOT / rel)
