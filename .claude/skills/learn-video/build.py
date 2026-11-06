#!/usr/bin/env python3
"""Build a narrated slide video from a segments file (see SKILL.md › Segments file).

    python3 .claude/skills/learn-video/build.py artifacts/media/<name>.segments.py artifacts/media/<name>.mp4

macOS only: narration by `say`, slides by headless Google Chrome, assembly by ffmpeg/ffprobe.
Slides and audio are cached in artifacts/media/.video-cache/<name>/ — delete a segment's files
there (or the whole folder) after editing its text or slide.
"""
import html, importlib.util, platform, shutil, subprocess, sys
from pathlib import Path

if len(sys.argv) != 3:
    sys.exit(__doc__)
SRC, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
if platform.system() != "Darwin":
    sys.exit("learn-video: the build needs macOS (`say`); the segments file is ready — build it on a Mac.")
for tool in ("say", "ffmpeg", "ffprobe"):
    if not shutil.which(tool):
        sys.exit(f"learn-video: `{tool}` not found (ffmpeg: `brew install ffmpeg`).")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if not Path(CHROME).exists():
    sys.exit(f"learn-video: Google Chrome not found at {CHROME}.")

spec = importlib.util.spec_from_file_location("segments", SRC)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
S, VOICE, FOOT = M.S, M.VOICE, getattr(M, "FOOT", "")
RATE, KICKER = str(getattr(M, "RATE", 140)), getattr(M, "KICKER", "")
PAUSE_AFTER = getattr(M, "PAUSE_AFTER", 1500)       # ms of silence after each theory slide
THINK = getattr(M, "THINK_LABEL", "… think and answer aloud")
ANSWER_WORD = getattr(M, "ANSWER_WORD", "Answer.")  # splits a question's text into question / answer
SUMMARY = getattr(M, "SUMMARY_LABEL", "Summary")
voices = subprocess.run(["say", "-v", "?"], capture_output=True, text=True).stdout
if VOICE not in voices:
    sys.exit(f"learn-video: voice '{VOICE}' is not installed (System Settings › Accessibility › Spoken Content).")

D = SRC.parent / ".video-cache" / SRC.name.removesuffix(".segments.py"); D.mkdir(parents=True, exist_ok=True)

CSS = """body{margin:0;width:1280px;height:720px;background:#14213d;color:#f4f1ea;font-family:-apple-system,Helvetica,Arial,sans-serif;
display:flex;align-items:center;padding:0 80px;box-sizing:border-box;gap:40px}
.t{flex:1}.k{font-size:22px;letter-spacing:2px;text-transform:uppercase;color:#fca311;margin-bottom:16px}
h1{font-size:50px;margin:0 0 30px;line-height:1.15}li{font-size:31px;line-height:1.45;margin-bottom:8px}
.q h1{font-size:46px}.a{margin-top:28px;font-size:34px;color:#9ee6a8;line-height:1.4}
.q.long h1{font-size:36px}.q.long .a{font-size:29px}
svg{max-width:520px;max-height:560px}
.foot{position:absolute;bottom:24px;left:80px;font-size:19px;color:#8d99ae}"""


def slide(name, s, show_answer=False):
    kind = s["kind"]
    kicker = {"q": s["title"], "title": KICKER, "summary": SUMMARY}.get(kind, KICKER)
    if kind == "q":
        answer = s.get("answer") or ""
        a = (f'<div class="a">✓ {html.escape(answer)}</div>' if show_answer
             else f'<div class="a" style="color:#8d99ae">{html.escape(THINK)}</div>')
        cls = "t q long" if len(s["bullets"][0]) + len(answer) > 170 else "t q"
        body = f'<div class="{cls}"><div class="k">{html.escape(kicker)}</div><h1>{html.escape(s["bullets"][0])}</h1>{a}</div>'
    else:
        lis = "".join(f"<li>{html.escape(b)}</li>" for b in s["bullets"])
        body = f'<div class="t"><div class="k">{html.escape(kicker)}</div><h1>{html.escape(s["title"])}</h1><ul>{lis}</ul></div>'
    if s.get("svg"):
        body += f'<div>{s["svg"]}</div>'
    hp = D / f"{name}.html"
    page = f"<!doctype html><meta charset=utf-8><style>{CSS}</style><body>{body}<div class=foot>{html.escape(FOOT)}</div>"
    png = D / f"{name}.png"
    if not png.exists() or not hp.exists() or hp.read_text() != page:
        hp.write_text(page)
        subprocess.run([CHROME, "--headless=new", f"--user-data-dir={D / 'chrome'}", "--no-first-run", "--disable-gpu",
                        f"--screenshot={png}", "--window-size=1280,720", "--hide-scrollbars", hp.as_uri()],
                       check=True, capture_output=True, timeout=60)
    return png


def audio(name, text):
    a, t = D / f"{name}.aiff", D / f"{name}.txt"
    if a.exists() and a.stat().st_size > 10000 and t.exists() and t.read_text() == text:
        return a
    t.write_text(text)
    subprocess.run(["say", "-v", VOICE, "-r", RATE, "-o", str(a), text], check=True)
    return a


items = []  # (png, aiff)
for i, s in enumerate(S):
    n = f"{i:02d}"
    if s["kind"] == "q":
        q, _, a = s["text"].partition(f" {ANSWER_WORD} ")
        if bool(a) != bool(s.get("answer")):
            sys.exit(f"learn-video: segment {n} ({s['title']}): `answer` and the ' {ANSWER_WORD} ' part go together.")
        items.append((slide(n + "a", s), audio(n + "a", q)))
        if a:  # lecture question: the answer follows the pause
            items.append((slide(n + "b", s, True), audio(n + "b", f"{ANSWER_WORD} {a} [[slnc 2000]]")))
    else:
        items.append((slide(n, s), audio(n, f"{s['text']} [[slnc {PAUSE_AFTER}]]")))

il, al = [], []
for png, aif in items:
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                       "-of", "csv=p=0", str(aif)]).decode())
    il.append(f"file '{png}'\nduration {d:.3f}\n"); al.append(f"file '{aif}'\n")
il.append(f"file '{items[-1][0]}'\n")
(D / "img.txt").write_text("".join(il)); (D / "aud.txt").write_text("".join(al))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(D / "aud.txt"),
                "-c:a", "pcm_s16le", str(D / "all.wav")], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(D / "img.txt"),
                "-i", str(D / "all.wav"), "-c:v", "libx264", "-tune", "stillimage", "-r", "10", "-pix_fmt", "yuv420p",
                "-vsync", "cfr", "-c:a", "aac", "-b:a", "96k", "-shortest", str(OUT)], check=True)
total = sum(float(l.split()[1]) for l in "".join(il).splitlines() if l.startswith("duration"))
print(f"{OUT}  ({total / 60:.1f} min, {len(items)} slides)")
