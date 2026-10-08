"""Maintenance for this knowledge base. Python 3.9+, no dependencies.

  python tools/notes.py index              rebuild index.md from the notes
  python tools/notes.py check [-v]         report problems; exit code 1 if any (read-only)
  python tools/notes.py compact-log [--keep N]   move all but the last N log entries to log.archive.md

check: every note has frontmatter (title, type, updated as YYYY-MM-DD), every relative markdown
link [text](path) points to a file in this repo, index.md matches the notes; every relative
href/src in the HTML pages points to a file in this repo; no [[wikilinks]] and no stray tool tags
(</invoke>, </content>, <parameter …>) left in notes or pages.
"""
import datetime
import re
from urllib.parse import unquote
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(<?([^)<>\s]+)>?(?:\s+\"[^\"]*\")?\)")   # [text](target)
REQUIRED = ("title", "type", "updated")
SKIP_DIRS = {"node_modules", "__pycache__", "tools", "media"}   # and every hidden folder
NOT_NOTES = {"index.md", "log.md", "log.archive.md", "README.md", "AGENTS.md", "CLAUDE.md"}
INDEX_HEADER = "<!-- auto-generated index — regenerate after adding/removing notes; do not edit by hand -->"
TAG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ENTRY = re.compile(r"^\d{4}-\d{2}-\d{2}\b")
HTML_REF = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)
WIKILINK = re.compile(r"\[\[[^\]\n]+\]\]")
STRAY = re.compile(r"</invoke>|</content>|<parameter\s+name=|</parameter>")


def _skipped(parts, skip):
    return any(x in skip or x.startswith(".") for x in parts)


def notes(root=ROOT):
    out = []
    for p in sorted(root.rglob("*.md"), key=lambda p: p.relative_to(root).as_posix()):   # same order on every OS
        rel = p.relative_to(root)
        if _skipped(rel.parts[:-1], SKIP_DIRS) or p.name in NOT_NOTES:
            continue
        out.append(p)
    return out


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    kv = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            kv[m.group(1)] = m.group(2).strip().strip("\"'")
    return kv


def summary_line(text):
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        body = text[end + 4:] if end >= 0 else text
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", ">", "|", "```", "<", "---")):
            continue
        s = re.sub(r"^(\*\*)?TL;DR(\*\*)?\s*[—:-]?\s*", "", s)
        s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = s.replace("**", "").replace("`", "")
        return (s[:157] + "…") if len(s) > 160 else s
    return ""


def render_index(root=ROOT):
    groups = defaultdict(list)
    for p in notes(root):
        r = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        title = (frontmatter(text) or {}).get("title") or p.stem
        s = summary_line(text)
        groups[str(PurePosixPath(r).parent)].append(f"- [{title}]({r})" + (f" — {s}" if s else ""))
    lines = [INDEX_HEADER, "", "# Index", ""]
    for g in sorted(groups, key=lambda x: (x != ".", x)):
        lines += [f'## {"(root)" if g == "." else g}', ""] + groups[g] + [""]
    return "\n".join(lines)


def cmd_index(root=ROOT):
    new, out = render_index(root), root / "index.md"
    if not out.exists() or out.read_text(encoding="utf-8") != new:
        out.write_text(new, encoding="utf-8", newline="\n")
        print("index: updated")
    else:
        print("index: up to date")
    return 0


def _norm(path):
    out = []
    for x in path.split("/"):
        if x in ("", "."):
            continue
        if x == "..":
            if not out:
                return None
            out.pop()
        else:
            out.append(x)
    return "/".join(out)


def cmd_check(root=ROOT, verbose=False):
    files = notes(root)
    skip = SKIP_DIRS - {"media"}          # links may point at media files and transcripts
    all_files = {p.relative_to(root).as_posix() for p in root.rglob("*")
                 if p.is_file() and not _skipped(p.relative_to(root).parts[:-1], skip)}
    problems = []
    for p in files:
        r = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = frontmatter(text)
        if fm is None:
            problems.append((r, "no frontmatter"))
        else:
            for k in REQUIRED:
                if not fm.get(k):
                    problems.append((r, f"frontmatter: missing {k}"))
            if fm.get("updated") and not re.match(r"^\d{4}-\d{2}-\d{2}$", fm["updated"]):
                problems.append((r, f"frontmatter: bad updated {fm['updated']!r}"))
            tags = fm.get("tags")
            if tags:
                items = [x.strip().strip("\"'") for x in tags.strip("[]").split(",") if x.strip()]
                if not tags.startswith("[") or any(not TAG.match(x) for x in items):
                    problems.append((r, f"frontmatter: tags must be a [kebab-case, list], got {tags!r}"))
        body = re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", text, flags=re.S | re.M)   # fenced code
        body = re.sub(r"(?m)^(?: {4}|\t).*$", "", body)                         # indented code
        body = re.sub(r"`[^`\n]*`", "", body)                                   # inline code
        d = str(PurePosixPath(r).parent)
        if WIKILINK.search(body):
            problems.append((r, f"wikilink {WIKILINK.search(body).group(0)} — use a markdown link"))
        if STRAY.search(text):
            problems.append((r, f"stray tool tag {STRAY.search(text).group(0)!r}"))
        for m in LINK.finditer(body):
            tg = m.group(1).split("#", 1)[0]
            if not tg or (re.match(r"^[a-z][a-z0-9+.-]*:", tg, re.I) and not re.match(r"^[a-z]:[\\/]", tg, re.I)):
                continue                                      # anchor, http:, mailto:
            tg = unquote(tg)
            target = _norm(tg[1:]) if tg.startswith("/") else _norm(d + "/" + tg)
            if not target or (target not in all_files and not (root / target).is_dir()):
                problems.append((r, f"broken link ({m.group(1)})"))
    for p in sorted(root.rglob("*.html"), key=lambda p: p.relative_to(root).as_posix()):
        rel = p.relative_to(root)
        if _skipped(rel.parts[:-1], SKIP_DIRS - {"media"}):
            continue
        r = rel.as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"(?is)<(script|style)\b[^>]*>.*?</\1>", lambda m: m.group(0) if "src=" in m.group(0)[:200] else "", text)
        d = str(PurePosixPath(r).parent)
        if WIKILINK.search(text):
            problems.append((r, f"wikilink {WIKILINK.search(text).group(0)}"))
        if STRAY.search(text):
            problems.append((r, f"stray tool tag {STRAY.search(text).group(0)!r}"))
        for m in HTML_REF.finditer(text):
            tg = m.group(1).split("#", 1)[0].split("?", 1)[0]
            if not tg or re.match(r"^[a-z][a-z0-9+.-]*:", tg, re.I) or tg.startswith("//"):
                continue                                      # anchor, http:, data:, mailto:, file:
            tg = unquote(tg)
            target = _norm(tg[1:]) if tg.startswith("/") else _norm(d + "/" + tg)
            if not target or (target not in all_files and not (root / target).is_dir()):
                problems.append((r, f"broken href/src ({m.group(1)})"))
    idx = root / "index.md"
    if not idx.exists():
        problems.append(("index.md", "missing — run: python tools/notes.py index"))
    elif idx.read_text(encoding="utf-8") != render_index(root):
        problems.append(("index.md", "out of date — run: python tools/notes.py index"))
    if not problems:
        print("check: ok")
        return 0
    print(f"check: {len(problems)} problem(s)" + ("" if verbose else " — add -v for details"))
    if verbose:
        for r, msg in problems:
            print(f"  {r}: {msg}")
    return 1


def cmd_compact_log(root=ROOT, keep=50):
    """Move all but the last `keep` dated entries ("YYYY-MM-DD — …", with any continuation
    lines) to log.archive.md. Summarizing the archive is a judgment task — see AGENTS.md."""
    log = root / "log.md"
    if not log.exists():
        print("compact-log: no log.md")
        return 0
    lines = log.read_text(encoding="utf-8").splitlines()
    starts = [i for i, s in enumerate(lines) if ENTRY.match(s.lstrip("-* ").strip())]
    if len(starts) <= keep:
        print(f"compact-log: {len(starts)} entries ≤ {keep} — nothing to do")
        return 0
    cut = starts[-keep]
    header = [s for s in lines[:starts[0]] if not s.startswith("<!-- archived:")]
    old = lines[starts[0]:cut]
    today = datetime.date.today().isoformat()
    archive = root / "log.archive.md"
    with archive.open("a", encoding="utf-8", newline="\n") as f:
        f.write(f"\n## Archived {today} ({len(starts) - keep} entries)\n\n" + "\n".join(old) + "\n")
    marker = f"<!-- archived: {len(starts) - keep} older entries moved to log.archive.md on {today} -->"
    log.write_text("\n".join(header + [marker, ""] + lines[cut:]) + "\n", encoding="utf-8", newline="\n")
    print(f"compact-log: archived {len(starts) - keep} entries, kept {keep}")
    return 0


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "index":
        return cmd_index()
    if cmd == "check":
        return cmd_check(verbose="-v" in rest)
    if cmd == "compact-log":
        keep = 50
        if "--keep" in rest:
            i = rest.index("--keep")
            if i + 1 >= len(rest) or not rest[i + 1].isdigit() or int(rest[i + 1]) < 1:
                print("compact-log: --keep needs a number ≥ 1")
                return 2
            keep = int(rest[i + 1])
        return cmd_compact_log(keep=keep)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
