#!/usr/bin/env python3
"""Preflight for ad-campaign-runbook: validate the required blog post and
report the facts the runbook is built from.

Usage: preflight.py <path/to/post.md> [--cta /brief] [--site https://example.com]

Exit codes: 0 ok, 2 missing or unusable post (the skill must stop and ask).
Stdlib only, so it runs in any host without an install step.
"""

import json
import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(json.dumps({"ok": False, "error": message}, indent=2))
    sys.exit(2)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not match:
        return {}, text
    meta = {}
    for line in match.group(1).splitlines():
        # Flat keys only. Nested YAML is rare in post frontmatter and the
        # runbook needs title, slug, date and excerpt, nothing deeper.
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if kv:
            meta[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return meta, match.group(2)


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = dict(zip(sys.argv[1:], sys.argv[2:]))
    if not args:
        fail("No blog post given. Pass the path to the post's .md file; "
             "this skill never picks a post on its own.")

    path = Path(args[0]).expanduser()
    if not path.is_file():
        fail(f"Not a file: {path}")
    if path.suffix.lower() not in {".md", ".mdx"}:
        fail(f"Expected a .md or .mdx blog post, got: {path.name}")

    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    words = re.findall(r"\b[\w'’-]+\b", re.sub(r"```.*?```", "", body, flags=re.S))
    if len(words) < 300:
        fail(f"Post body has {len(words)} words. Under 300 there is too little "
             "to derive five distinct, traceable ad angles from.")

    cta = flags.get("--cta")
    links = [(m.start(), m.group(1), m.group(2))
             for m in re.finditer(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)", body)]
    cta_links = [l for l in links if cta and l[2].split("?")[0].rstrip("/") == cta.rstrip("/")]
    first_cta_word = None
    if cta_links:
        first_cta_word = len(re.findall(r"\b[\w'’-]+\b", body[: cta_links[0][0]]))

    slug = meta.get("slug") or path.stem
    site = flags.get("--site", "").rstrip("/")
    report = {
        "ok": True,
        "path": str(path),
        "title": meta.get("title"),
        "slug": slug,
        "short_slug_suggestion": "-".join(slug.split("-")[:4]),
        "date": meta.get("date"),
        "excerpt": meta.get("excerpt"),
        "url": f"{site}/blog/{slug}" if site else None,
        "word_count": len(words),
        "h2_sections": re.findall(r"^##\s+(.+)$", body, re.M),
        "images": len(re.findall(r"!\[[^\]]*\]\(", body)),
        "internal_links": sorted({l[2] for l in links if l[2].startswith("/")}),
        "cta_path": cta,
        "cta_link_count": len(cta_links),
        "first_cta_at_word": first_cta_word,
        "warnings": [],
    }
    if not meta:
        report["warnings"].append("No YAML frontmatter: title, slug and date must be confirmed by hand.")
    if len(report["h2_sections"]) < 3:
        report["warnings"].append("Fewer than 3 H2 sections: angles map to sections, so expect fewer than five angles.")
    if cta and not cta_links:
        report["warnings"].append(f"The post never links to {cta}. Paid readers have no path to the conversion.")
    elif first_cta_word and first_cta_word > 200:
        report["warnings"].append(
            f"First {cta} link comes after {first_cta_word} words. Add one near the top before spending on traffic.")
    if report["images"] == 0:
        report["warnings"].append("No images in the post. If the offer is visual, show it on the page.")
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
