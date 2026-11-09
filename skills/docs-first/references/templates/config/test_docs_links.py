"""Documentation link and index integrity checks (unit suite, runs in seconds).

Rules:
1. Every relative markdown link target must exist, and each ``#anchor`` must
   resolve to a heading in the target file (GitHub slug rules).
2. Every docs markdown file must be linked from the master index ``docs/README.md``,
   except the index itself, ``design/changes/`` and ``design/archive/``
   (active changes are listed separately; archived docs stay reachable by date).
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs"
MASTER_INDEX = DOCS_ROOT / "README.md"
EXCLUDED_FROM_INDEX = ("design/changes/", "design/archive/")

_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
_EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "#", "/")


def _github_slug(header: str) -> str:
    """Apply GitHub heading anchor rules: lowercase, keep letters/digits (incl. CJK),
    spaces become hyphens, punctuation is dropped."""
    text = header.strip().lower()
    out = []
    for ch in text:
        if ch in (" ", "\t"):
            out.append("-")
        elif ch in ("-", "_"):
            out.append(ch)
        elif unicodedata.category(ch).startswith(("L", "N")):
            out.append(ch)
    return "".join(out)


def _anchors_of(path: Path) -> set[str]:
    anchors: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.*)$", line)
        if match:
            anchors.add(_github_slug(match.group(1)))
    return anchors


def _iter_md_files() -> list[Path]:
    files = [REPO_ROOT / "README.md", REPO_ROOT / "AGENTS.md"]
    files.extend(sorted(DOCS_ROOT.rglob("*.md")))
    return [path for path in files if path.exists()]


def _check_links() -> list[str]:
    errors: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    for md in _iter_md_files():
        text = md.read_text(encoding="utf-8")
        for raw in _LINK_RE.findall(text):
            target = raw.strip()
            if target.startswith(_EXTERNAL_PREFIXES):
                file_part, _, anchor = "", target.lstrip("#")
                dest = md
            else:
                file_part, _, anchor = target.partition("#")
                dest = (md.parent / file_part).resolve() if file_part else md
                if file_part and not dest.exists():
                    errors.append(f"{md.relative_to(REPO_ROOT)}: dead link {raw}")
                    continue
            if anchor:
                if not dest.is_file() or dest.suffix != ".md":
                    errors.append(f"{md.relative_to(REPO_ROOT)}: anchor on non-markdown {raw}")
                    continue
                if dest not in anchor_cache:
                    anchor_cache[dest] = _anchors_of(dest)
                if anchor not in anchor_cache[dest]:
                    errors.append(f"{md.relative_to(REPO_ROOT)}: missing anchor {raw}")
    return errors


def test_docs_have_no_dead_links() -> None:
    errors = _check_links()
    assert not errors, "dead links / missing anchors:\n" + "\n".join(errors)


def test_master_index_covers_all_docs() -> None:
    index_text = MASTER_INDEX.read_text(encoding="utf-8")
    missing: list[str] = []
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        if path == MASTER_INDEX:
            continue
        rel = path.relative_to(DOCS_ROOT).as_posix()
        if rel.startswith(EXCLUDED_FROM_INDEX):
            continue
        if f"({rel})" not in index_text and f"({rel}#" not in index_text:
            missing.append(rel)
    assert not missing, "docs/README.md does not index:\n" + "\n".join(missing)
