"""Build Keith's resume PDF from src/resume/resume.html.

    python3 src/build_resume.py                      # public copy, no phone -> src/files/Keith_Rollins_Resume.pdf
    python3 src/build_resume.py --phone "(xxx) xxx-xxxx"   # application copy with phone -> private/ (git-ignored)

Then run `python3 src/build.py` so the site picks up the new public PDF.
Needs Playwright: pip install playwright && python3 -m playwright install chromium
"""
import argparse, os, subprocess, tempfile
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "resume", "resume.html")

def render(html, out):
    with tempfile.NamedTemporaryFile("w", suffix=".html", dir=os.path.dirname(SRC), delete=False) as f:
        f.write(html); tmp = f.name
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(); pg = b.new_page()
            pg.goto("file://" + tmp); pg.wait_for_timeout(600)
            pg.pdf(path=out, format="Letter", prefer_css_page_size=True, print_background=True)
            b.close()
    finally:
        os.remove(tmp)
    try:
        pages = subprocess.run(["pdfinfo", out], capture_output=True, text=True).stdout
        n = [l for l in pages.splitlines() if l.startswith("Pages:")]
        if n and n[0].split()[-1] != "1":
            print("WARNING: resume is", n[0].split()[-1], "pages; it must fit on one page.")
    except FileNotFoundError:
        pass
    print("wrote", out)

ap = argparse.ArgumentParser()
ap.add_argument("--phone", help="include this phone number (application copy, never committed)")
a = ap.parse_args()
html = open(SRC).read()
if a.phone:
    os.makedirs(os.path.join(HERE, "..", "private"), exist_ok=True)
    render(html.replace("{{PHONE}}", " · " + a.phone), os.path.join(HERE, "..", "private", "Keith_Rollins_Resume.pdf"))
else:
    os.makedirs(os.path.join(HERE, "files"), exist_ok=True)
    render(html.replace("{{PHONE}}", ""), os.path.join(HERE, "files", "Keith_Rollins_Resume.pdf"))
