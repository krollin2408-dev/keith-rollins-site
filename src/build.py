"""Build keithrrollins.com from src/content.py. Run from the repo root: python3 src/build.py

While LIVE is False (content.py), the full site builds to preview/ (git-ignored) and docs/ holds a
coming-soon page. When LIVE is True, the full site builds straight into docs/ (what GitHub Pages serves).
"""
import html, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DOCS = os.path.join(ROOT, "docs")
OUT = sys.argv[1] if len(sys.argv) > 1 else (DOCS if LIVE else os.path.join(ROOT, "preview"))
WBY = {w["slug"]: w for w in WORK}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=JetBrains+Mono:wght@500&display=swap">')
NAV = [("story.html", "My story"), ("work.html", "Work"), ("resume.html", "Resume"), ("contact.html", "Let's talk")]

def e(s): return html.escape(s, quote=True)

def page(path, title, desc, body, current=None, head_extra=""):
    r = "../" * path.count("/")
    canon = SITE + "/" + ("" if path == "index.html" else path)
    nav = "".join(f'<li><a href="{r}{h}"{" class=\"talk\"" if h == "contact.html" else ""}{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t in NAV)
    foot = "".join(f'<li><a href="{r}{h}">{t}</a></li>' for h, t in [("index.html", "Home")] + NAV + [("dungeon-crawler-fitness.html", "What I'm building"), ("how-i-built-this-site.html", "How I built this site")])
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/images/keith-rollins-headshot.jpg">
<link rel="canonical" href="{canon}">
{FONTS}
<link rel="stylesheet" href="{r}assets/site.css">
{head_extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
<a class="brand" href="{r}index.html">Keith Rollins</a>
<nav aria-label="Main"><ul class="nav">{nav}</ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="wrap">
<div style="display:grid;gap:10px"><h2>Let's talk.</h2><span class="addr">{EMAIL}</span></div>
<div class="btns"><button class="btn solid" type="button" data-copy="{EMAIL}">Copy email address</button><span class="toast" aria-live="polite"></span></div>
<nav aria-label="Footer" style="flex-basis:100%"><ul>{foot}</ul></nav>
</div></footer>
<script src="{r}assets/site.js"></script>
</body>
</html>
"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(doc)

def card(w, r=""):
    if w["kind"] == "image":
        top = f'<div class="pic"><img src="{r}{w["image"]}" alt="{e(w["image_alt"])}" loading="lazy"></div>'
    else:
        top = f'<div class="plate" aria-hidden="true"><b>{e(w["stat"])}</b><span>{e(w["stat_note"])}</span></div>'
    return f'<a class="card" href="{r}work/{w["slug"]}.html">{top}<div class="txt"><span class="label">{e(w["label"])}</span><h3>{e(w["title"])}</h3><p>{e(w["summary"])}</p></div></a>'

if os.path.isdir(OUT) and os.path.abspath(OUT) != os.path.abspath(DOCS):
    shutil.rmtree(OUT)
os.makedirs(OUT, exist_ok=True)

# ---------------- HOME
chap = "".join(f'<a href="story.html"><span class="label">{d}</span><h3>{t}</h3><p>{e(s)}</p></a>' for d, t, s in CHAPTERS)
feat = "".join(card(WBY[s]) for s in FEATURED)
person = json.dumps({"@context": "https://schema.org", "@type": "Person", "name": "Keith Rollins", "jobTitle": "Marketing Communications Lead",
                     "worksFor": {"@type": "Organization", "name": "APMEX"}, "url": SITE, "image": SITE + "/images/keith-rollins-headshot.jpg",
                     "address": {"@type": "PostalAddress", "addressLocality": "Edmond", "addressRegion": "OK"},
                     "knowsAbout": ["Email marketing", "Marketing strategy", "Copywriting", "Social media", "Public relations", "SEO"]})
home = f"""
<div class="wrap">
<section class="hero">
<div class="hero-copy">
<span class="label">{e(HERO['label'])}</span>
<h1 class="display h-xl">{e(HERO['headline'])}</h1>
<p class="lede">{e(HERO['lede'])}</p>
<div class="btns"><a class="btn solid" href="story.html">Read my story</a><a class="btn" href="work.html">See the work</a></div>
</div>
<figure class="portrait" style="margin:0">
<img src="images/keith-rollins-headshot.jpg" alt="Keith Rollins, smiling, arms crossed, in a blue shirt and black tie">
<figcaption class="caption">↑ That's me, in Edmond</figcaption>
</figure>
</section>
<section class="sec">
<div class="sec-head"><h2 class="display h-md">How I got here</h2><a class="more" href="story.html">The whole story →</a></div>
<div class="chapters">{chap}</div>
</section>
</div>
<section class="band"><div class="wrap">
<span class="label">How I work</span>
<p class="big">{e(QUOTE[0])}</p>
<p>{e(QUOTE[1])}</p>
</div></section>
<div class="wrap">
<section class="sec" style="border-top:0">
<div class="sec-head"><h2 class="display h-md">Stuff I've made</h2><a class="more" href="work.html">All of it →</a></div>
<div class="cards">{feat}</div>
</section>
</div>
"""
page("index.html", "Keith Rollins | Marketing Strategist and Communications Leader",
     "Keith Rollins went from running an auto repair shop to leading marketing communications at APMEX. His story, and the work.",
     home, None, f'<script type="application/ld+json">{person}</script>')

# ---------------- STORY
story = "".join(f'<section class="chapter"><div><span class="label">{e(lab)}</span><h2>{e(h)}</h2></div><div class="prose">{"".join(f"<p>{e(p)}</p>" for p in ps)}</div></section>' for lab, h, ps in STORY)
storypage = f"""
<div class="wrap">
<header class="page-head"><span class="label">My story</span><h1 class="display h-xl">From the shop floor to the inbox.</h1>
<p class="lede">It starts where I am today, then goes back to how I got here.</p></header>
<div class="story">{story}</div>
<div class="btns" style="border-top:3px solid var(--rule);padding-top:32px"><a class="btn solid" href="work.html">See the work</a><a class="btn" href="resume.html">Read my resume</a></div>
</div>
"""
page("story.html", "My Story | Keith Rollins", "How Keith Rollins went from managing an auto repair shop to leading marketing communications at APMEX.", storypage, "story.html")

# ---------------- WORK
cards = "".join(card(w) for w in WORK)
also = "".join(f"<li><b>{e(t)}</b><span>{e(d)}</span></li>" for t, d in ALSO)
workpage = f"""
<div class="wrap">
<header class="page-head"><span class="label">Work</span><h1 class="display h-xl">Stuff I've made.</h1>
<p class="lede">A hand-picked set, from APMEX and my freelance years. Each page shows the work first, then how it came together.</p></header>
<section class="sec"><div class="cards">{cards}</div></section>
<section class="sec">
<div class="sec-head"><h2 class="display h-md">Also on my plate</h2></div>
<ul class="also">{also}</ul>
</section>
</div>
"""
page("work.html", "Work | Keith Rollins", "Print, email, campaigns, social video, PR and writing by Keith Rollins.", workpage, "work.html")

# ---------------- PROJECT PAGES
SERIES = [("01-kickoff", "Kickoff", "60 days left. Announce the bonus."),
          ("02-flash", "Flash push", "72-hour offer to drive the first purchase."),
          ("03-midpoint", "Midpoint", "Progress bar plus a cross-sell."),
          ("04-last-call", "Last call", "5 days left. Close the gap."),
          ("05-reward", "Reward", "Confirm the bonus. Say thanks.")]
for i, w in enumerate(WORK):
    r = "../"
    if w.get("show") == "ad":
        show = f'<img class="ad" src="{r}{w["image"]}" alt="{e(w["image_alt"])}">'
    elif w.get("show") == "series":
        figs = "".join(f'<figure><div class="phone" tabindex="0" aria-label="{t} email. Scroll to read."><img src="{r}emails/{f}.jpg" alt="{t} email in the Bullion Card series" loading="lazy"></div><figcaption><b>{n}. {t}</b>{d}</figcaption></figure>' for n, (f, t, d) in enumerate(SERIES, 1))
        show = f'<div class="series">{figs}</div><p class="note" style="margin-top:12px">Scroll inside each email to read the whole send.</p>'
    elif w.get("show") == "fixd":
        items = "".join(f'<li><a href="https://www.fixdapp.com/car-reviews/best-worst-years-of-{m}-graphs-owner-surveys/" target="_blank" rel="noopener">{m.replace("-", " ").title().replace("Gmc", "GMC").replace("Rx300", "RX300").replace("Cts", "CTS").replace("Srx", "SRX")}</a></li>' for m in FIXD)
        show = f'<div style="display:grid;gap:18px"><div class="statbig"><b>{e(w["stat"])}</b><span>{e(w["stat_note"])}. Every one is live on fixdapp.com:</span></div><ul class="fixd">{items}</ul></div>'
    else:
        show = f'<div class="statbig"><b>{e(w["stat"])}</b><span>{e(w["stat_note"])}</span></div>'
    body = "".join(f'<section><h2>{e(h)}</h2><div class="prose">{c}</div></section>' for h, c in w["body"])
    prev_w, next_w = WORK[i - 1], WORK[(i + 1) % len(WORK)]
    proj = f"""
<div class="wrap">
<header class="project-hero">
<div class="crumb"><a href="{r}work.html">Work</a> / {e(w['label'])}</div>
<h1 class="display h-lg">{e(w['title'])}</h1>
<p class="lede">{e(w['summary'])}</p>
<div class="facts"><span>My role: <b>{e(w['role'])}</b></span></div>
</header>
</div>
<section class="showcase"><div class="wrap">{show}</div></section>
<div class="wrap">
<div class="project-body">{body}</div>
<nav class="pager" aria-label="More work"><a href="{prev_w['slug']}.html"><span>← Previous</span><b>{e(prev_w['title'])}</b></a><a href="{next_w['slug']}.html"><span>Next →</span><b>{e(next_w['title'])}</b></a></nav>
</div>
"""
    page(f"work/{w['slug']}.html", f"{w['title']} | Keith Rollins", w["summary"], proj, "work.html")

# ---------------- RESUME (one source: src/resume/resume.html)
src = open(os.path.join(HERE, "resume", "resume.html")).read()
inner = src[src.index("<body>") + 6:src.index("</body>")].replace("{{PHONE}}", "")
inner = re.sub(r"<h1>(.*?)</h1>", r'<p class="rname">\1</p>', inner, count=1)
respage = f"""
<div class="wrap">
<header class="page-head"><span class="label">Resume</span><h1 class="display h-xl">The one-page version.</h1>
<div class="btns"><a class="btn solid" href="files/Keith_Rollins_Resume.pdf">Download PDF</a><a class="btn" href="story.html">Read the long version</a></div></header>
<article class="resume-sheet">{inner}</article>
</div>
"""
page("resume.html", "Resume | Keith Rollins", "Keith Rollins' resume: Email & Marketing Communications Lead.", respage, "resume.html")

# ---------------- CONTACT
contact = f"""
<div class="wrap">
<header class="page-head"><span class="label">Let's talk</span><h1 class="display h-xl">Got a team that needs this?</h1>
<p class="lede">I'm looking for a full-time role leading email and lifecycle marketing, remote or in the Oklahoma City area. Email is the fastest way to reach me.</p></header>
<div class="contact-card"><span class="label">Email</span><span class="addr">{EMAIL}</span>
<div class="btns"><button class="btn solid" type="button" data-copy="{EMAIL}">Copy email address</button><span class="toast" aria-live="polite"></span></div>
<span class="caption">Edmond, Oklahoma · <a href="resume.html">Resume</a></span></div>
</div>
"""
page("contact.html", "Let's Talk | Keith Rollins", "Contact Keith Rollins about email and marketing communications roles.", contact, "contact.html")

# ---------------- DUNGEON CRAWLER FITNESS
dcf = """
<div class="wrap">
<header class="page-head"><span class="label">What I'm building</span><h1 class="display h-xl">Dungeon Crawler Fitness</h1>
<p class="lede">A fitness game I designed. It started as a board game and is now becoming an app. I'm building its email program from zero, in public. When there are real numbers, they'll be here.</p></header>
<div class="project-body">
<section><h2>The game</h2><div class="prose"><p>Players finish quest cards made of bodyweight exercises to earn XP and gold, fight floor bosses, keep streaks alive and level up a character across five skills. The design is locked, and a working prototype is being playtested.</p></div></section>
<section><h2>The email plan</h2><div class="prose"><ol><li><b>Waitlist.</b> An honest sign-up page on Kit: no fake scarcity, no invented testimonials, no results claims.</li><li><b>Welcome series.</b> Introduce the game and learn what each subscriber wants.</li><li><b>Build log.</b> Regular updates so the list stays warm until launch.</li><li><b>Launch.</b> A paced sequence that turns the waitlist into first players.</li><li><b>Report.</b> List growth, opens, clicks and conversions, posted here.</li></ol></div></section>
<section><h2>Where it stands</h2><div class="prose"><p>Game designed. Prototype in playtesting. Waitlist page in progress.</p></div></section>
</div>
</div>
"""
page("dungeon-crawler-fitness.html", "Dungeon Crawler Fitness | Keith Rollins", "Keith Rollins is building the email program for Dungeon Crawler Fitness, a fitness game he designed, from zero.", dcf)

# ---------------- HOW I BUILT THIS
col = """
<div class="wrap">
<header class="page-head"><span class="label">How I built this site</span><h1 class="display h-xl">Built with AI. Checked by me.</h1>
<p class="lede">This site is part of my work. I made it with Claude as a working partner, and I made every call about what's true and what goes in.</p></header>
<div class="project-body">
<section><h2>What AI did</h2><div class="prose"><ul><li>Pulled my author pages and counted my published work: 63 APMEX articles and 20 FIXD guides.</li><li>Read public view counts to find which of my video ideas outperformed.</li><li>Drafted pages from my notes and wrote the code: plain HTML and one stylesheet, hosted free on GitHub Pages.</li></ul></div></section>
<section><h2>What I did</h2><div class="prose"><ul><li>Set the rule that every project names my exact role, and that every number has a source.</li><li>Cut what wasn't mine, corrected what was off, and chose the design.</li><li>Approved every word before it went live.</li></ul></div></section>
<section><h2>Why it matters</h2><div class="prose"><p>Using AI well isn't about typing prompts. It's knowing what to hand off, describing it clearly, checking the result and owning what ships. Anthropic calls that AI Fluency, and this site is a working example of it.</p></div></section>
</div>
</div>
"""
page("how-i-built-this-site.html", "How I Built This Site | Keith Rollins", "How Keith Rollins built his portfolio with Claude.", col)

# ---------------- STATIC FILES
for d in ("assets", "emails", "files", "images"):
    shutil.copytree(os.path.join(HERE, d), os.path.join(OUT, d), dirs_exist_ok=True)
print("built", len(WORK) + 7, "pages into", os.path.relpath(OUT, ROOT))

# ---------------- COMING-SOON PAGE (while LIVE is False)
if not LIVE and len(sys.argv) == 1:
    shutil.rmtree(DOCS, ignore_errors=True)
    os.makedirs(DOCS)
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(DOCS, "assets"))
    os.makedirs(os.path.join(DOCS, "images"))
    shutil.copy(os.path.join(HERE, "images", "keith-rollins-headshot.jpg"), os.path.join(DOCS, "images"))
    hold = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Keith Rollins | Marketing Strategist and Communications Leader</title>
<meta name="description" content="Keith Rollins, marketing strategist and communications leader. Full site coming soon.">
<meta name="robots" content="noindex">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<main class="hold"><div class="wrap">
<img src="/images/keith-rollins-headshot.jpg" alt="Keith Rollins">
<span class="label">Coming soon</span>
<h1 class="display h-xl">Hi, I'm Keith.</h1>
<p class="lede">I lead marketing communications at APMEX. My full site is getting a final check and will be here soon.</p>
<div class="btns"><span class="addr">{EMAIL}</span><button class="btn solid" type="button" data-copy="{EMAIL}">Copy email address</button><span class="toast" aria-live="polite"></span></div>
</div></main>
<script src="/assets/site.js"></script>
</body>
</html>
"""
    open(os.path.join(DOCS, "index.html"), "w").write(hold)
    open(os.path.join(DOCS, "404.html"), "w").write(hold)
    open(os.path.join(DOCS, "CNAME"), "w").write("keithrrollins.com\n")
    open(os.path.join(DOCS, ".nojekyll"), "w").write("")
    print("docs/ holds the coming-soon page (LIVE = False)")
