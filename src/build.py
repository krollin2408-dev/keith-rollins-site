import json, os, shutil, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content import *

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DOCS = os.path.join(ROOT, "docs")
# LIVE (in content.py) decides what keithrrollins.com shows. While False, the full site
# builds to preview/ (git-ignored, for fact-checking) and docs/ holds a "coming soon" page.
OUT = sys.argv[1] if len(sys.argv) > 1 else (DOCS if LIVE else os.path.join(ROOT, "preview"))
GBY = {g[0]: g for g in GROUPS}
CBY = {c["slug"]: c for c in CASES}

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;700;800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">'
NAV = [("index.html", "Home"), ("work.html", "Work"), ("about.html", "About"), ("dungeon-crawler-fitness.html", "Building"), ("files/Keith_Rollins_Resume.pdf", "Resume"), ("contact.html", "Contact")]

def e(s): return html.escape(s, quote=True)

def page(path, title, desc, body, current=None, extra_head=""):
    depth = path.count("/")
    r = "../" * depth
    canon = SITE + "/" + ("" if path == "index.html" else path)
    nav = "".join(f'<li><a href="{r}{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t in NAV)
    foot_nav = "".join(f'<li><a href="{r}{h}">{t}</a></li>' for h, t in NAV + [("how-i-built-this-site.html", "How I built this site")])
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
<link rel="canonical" href="{canon}">
{FONTS}
<link rel="stylesheet" href="{r}assets/site.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
<a class="brand" href="{r}index.html">Keith Rollins<small>Marketing strategy &amp; communications</small></a>
<nav class="site-nav" aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="wrap">
<div style="display:grid;gap:8px"><h2>Let's talk.</h2><span class="addr">{EMAIL} · Edmond, OK</span></div>
<div class="btns"><button class="btn primary" type="button" data-copy="{EMAIL}">Copy email address</button><span class="toast" aria-live="polite"></span></div>
<nav aria-label="Footer" style="flex-basis:100%"><ul>{foot_nav}</ul></nav>
</div></footer>
<script src="{r}assets/site.js"></script>
</body>
</html>
"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(doc)

def card(c, r=""):
    g = GBY[c["group"]]
    return f"""<a class="card" href="{r}work/{c['slug']}.html">
<div class="tags"><span class="tag">{e(c['own'])}</span><span class="tag plain">{e(g[1])}</span></div>
<h3>{e(c['title'])}</h3>
<p>{e(c['card'])}</p>
<div class="stat">{e(c['stat'][0])}<small>{e(c['stat'][1])}</small></div>
</a>"""

# ---------------- HOME
readout = [
    ("3 yrs", "leading marketing communications at APMEX, a top U.S. precious metals retailer", "SINCE AUG 2023"),
    ("3 brands", "with social strategy I own, across APMEX and its affiliates", "SOCIAL"),
    ("8+", "platforms unified in Sprout Social, which I selected and rolled out", "SYSTEMS"),
    ("420K", "views on the top video from a short-form format I created", "SHORT FORM"),
    ("~2/3", "of a week's link clicks driven by a campaign I led", "CAMPAIGNS"),
    ("83", "published articles: 63 for APMEX and 20 for FIXD", "CONTENT"),
]
ro = "".join(f"<div><code>{t}</code><b>{n}</b><span>{d}</span></div>" for n, d, t in readout)
disc = "".join(f'<a href="work.html#{k}"><h3>{n}</h3><p>{s}</p><span class="go">{sum(1 for c in CASES if c["group"]==k) + (1 if k=="ai" else 0)} projects →</span></a>' for k, n, s, _ in GROUPS)
feat = "".join(card(CBY[s]) for s in FEATURED)
person = json.dumps({"@context": "https://schema.org", "@type": "Person", "name": "Keith Rollins", "jobTitle": "Marketing Communications Lead", "worksFor": {"@type": "Organization", "name": "APMEX"}, "address": {"@type": "PostalAddress", "addressLocality": "Edmond", "addressRegion": "OK"}, "url": SITE, "email": "mailto:" + EMAIL, "knowsAbout": ["Email marketing", "Marketing strategy", "Social media strategy", "Public relations", "Copywriting", "SEO content"]})
home = f"""
<section class="hero"><div class="wrap">
<div class="hero-grid">
<div>
<span class="eyebrow">Keith Rollins</span>
<h1 style="margin-top:14px">Marketing strategist and <em>communications leader.</em></h1>
<p class="lede">I build marketing programs people trust, then prove they work. For three years I've led communications at APMEX across email, social, PR, content and paid media, for an audience that doesn't buy hype.</p>
<div class="btns"><a class="btn primary" href="work.html">Explore the work</a><a class="btn" href="files/Keith_Rollins_Resume.pdf">Download resume (PDF)</a><a class="textlink" href="about.html">About me →</a></div>
</div>
<aside class="idcard" aria-label="At a glance">
<span class="eyebrow">At a glance</span>
<dl>
<dt>Now</dt><dd>Marketing Communications Lead, APMEX</dd>
<dt>Lead</dt><dd>Strategy, email, social, PR, content, paid media</dd>
<dt>Based</dt><dd>Edmond, OK</dd>
<dt>Next</dt><dd>Email and lifecycle marketing leadership, remote or OKC</dd>
</dl>
</aside>
</div>
<div class="readout" role="group" aria-label="Career numbers">
<div class="readout-head"><span>Diagnostic report · K. Rollins</span><span>Status: open to new roles</span></div>
<div class="readout-grid">{ro}</div>
</div>
</div></section>

<section class="block"><div class="wrap">
<div class="sec-head"><span class="eyebrow">What I lead</span><h2>Eight disciplines, one program</h2><p>Every channel is planned with the others in mind. Pick a discipline to see the work.</p></div>
<div class="disc">{disc}</div>
</div></section>

<section class="block"><div class="wrap">
<div class="sec-head"><div class="row"><div style="display:grid;gap:10px"><span class="eyebrow">Featured work</span><h2>Start here</h2></div><a class="textlink" href="work.html">All {len(CASES)} projects →</a></div></div>
<div class="cards">{feat}</div>
</div></section>

<section class="block"><div class="wrap">
<div class="building">
<div style="display:grid;gap:14px;align-content:start">
<span class="eyebrow">Currently building</span>
<h2>Dungeon Crawler Fitness</h2>
<p>A fitness app that started as a board game I designed. I'm building its email program from zero, in public: waitlist, welcome sequence, build-log newsletter and launch. Every number will be real.</p>
<a class="textlink" href="dungeon-crawler-fitness.html">Follow the build →</a>
</div>
<ul class="checklist">
<li class="done">Game system designed</li>
<li class="now">Prototype in playtesting</li>
<li class="now">Email waitlist page</li>
<li>Welcome sequence</li>
<li>Build-log newsletter</li>
<li>Launch campaign and results</li>
</ul>
</div>
</div></section>

<section class="block"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Before marketing</span><h2>Eight years running an auto repair shop</h2><p>Diagnosing a car and diagnosing a campaign work the same way: find what's actually broken, fix it, then check that the fix held. <a href="about.html">Read the full story</a>.</p></div>
</div></section>
"""
page("index.html", "Keith Rollins | Marketing Strategist and Communications Leader",
     "Keith Rollins leads marketing communications at APMEX across email, social, PR, content and paid media. Explore his strategy and campaign work.",
     home, "index.html", f'<script type="application/ld+json">{person}</script>')

# ---------------- WORK HUB
filters = '<button type="button" data-f="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" data-f="{k}" aria-pressed="false">{n}</button>' for k, n, _, _ in GROUPS)
groups_html = ""
for k, n, s, long in GROUPS:
    cs = [c for c in CASES if c["group"] == k]
    cards = "".join(card(c) for c in cs)
    if k == "ai":
        cards += """<a class="card" href="how-i-built-this-site.html"><div class="tags"><span class="tag">Owned</span><span class="tag plain">AI &amp; operations</span></div><h3>How I built this site</h3><p>This portfolio, researched, written and coded with Claude as a working partner.</p><div class="stat">You're on it<small>Hand-coded, hosted on GitHub Pages</small></div></a>"""
    groups_html += f'<div class="group" id="{k}"><h2>{n}</h2><p>{long}</p><div class="cards">{cards}</div></div>'
work = f"""
<section class="case-hero"><div class="wrap">
<span class="eyebrow">Work</span>
<h1>{len(CASES) + 1} projects across eight disciplines</h1>
<p class="lede">Every project lists my exact role. Where I partnered with a specialist or a production team, I say so.</p>
</div></section>
<section class="block" style="padding-top:28px"><div class="wrap">
<div class="filters" role="group" aria-label="Filter by discipline">{filters}</div>
{groups_html}
</div></section>
"""
page("work.html", "Work | Keith Rollins", "Email, campaigns, social, PR, advertising, strategy, writing and AI projects by Keith Rollins.", work, "work.html")

# ---------------- CASE PAGES
SERIES = [("01-kickoff", "1. Kickoff", "60 days left. Announce the bonus and sell the card."),
          ("02-flash", "2. Flash push", "72-hour offer with a countdown to drive the first spend."),
          ("03-midpoint", "3. Midpoint", "25 days left. Progress bar plus a cross-sell."),
          ("04-last-call", "4. Last call", "5 days left. Loss aversion closes the gap."),
          ("05-reward", "5. Reward", "Confirm the bonus and thank the customer.")]
fixd_rows = "".join(f'<tr><td>{m.replace("-", " ").title().replace("Gmc","GMC").replace("Rx300","RX300").replace("A4","A4").replace("Cts","CTS").replace("Srx","SRX").replace("G6","G6")}</td><td><a href="https://www.fixdapp.com/car-reviews/best-worst-years-of-{m}-graphs-owner-surveys/" target="_blank" rel="noopener">Read the guide</a></td></tr>' for m in FIXD)
fixd_table = f'<div class="tablewrap"><table><thead><tr><th>Vehicle</th><th>Link</th></tr></thead><tbody>{fixd_rows}</tbody></table></div>'

order = [c["slug"] for g in GROUPS for c in CASES if c["group"] == g[0]]
for i, slug in enumerate(order):
    c = CBY[slug]; g = GBY[c["group"]]
    body = ""
    for h, content in c["body"]:
        body += f"<h2>{e(h)}</h2>" + (fixd_table if content == "FIXD_TABLE" else content)
    for t, u in c.get("links", []):
        body += f'<p><a class="textlink" href="{u}" target="_blank" rel="noopener">{e(t)} →</a></p>'
    series = ""
    if c.get("extra") == "series":
        figs = "".join(f'<figure><div class="phone" tabindex="0" aria-label="{e(t)} email, scroll to read"><img src="../emails/{f}.jpg" alt="{e(t)} email in the Bullion Card series" loading="lazy"></div><figcaption><b>{t}</b>{d}</figcaption></figure>' for f, t, d in SERIES)
        series = f'<div class="wrap"><div class="series">{figs}</div><p class="note" style="margin-top:8px">Scroll inside each email to read the full send.</p></div>'
    res = "".join(f"<li>{e(x)}</li>" for x in c["results"])
    prev_c = CBY[order[i - 1]]; next_c = CBY[order[(i + 1) % len(order)]]
    cp = f"""
<section class="case-hero"><div class="wrap">
<div class="crumbs"><a href="../work.html">Work</a><span>/</span><a href="../work.html#{g[0]}">{g[1]}</a></div>
<h1>{e(c['title'])}</h1>
<p class="lede">{e(c['lede'])}</p>
<dl class="factbar">
<div><dt>My role</dt><dd>{e(c['role'])}</dd></div>
<div><dt>Brand</dt><dd>{e(c['brand'])}</dd></div>
<div><dt>Year</dt><dd>{e(c['year'])}</dd></div>
<div><dt>Status</dt><dd>{e(c['status'])}</dd></div>
</dl>
</div></section>
{series}
<div class="wrap"><div class="case-body">
<article class="prose">{body}</article>
<aside class="aside">
<div class="results"><h2>Results</h2><ul>{res}</ul></div>
<p class="note"><b>Tools:</b> {e(c['tools'])}</p>
</aside>
</div>
<nav class="next" aria-label="More work">
<a href="{prev_c['slug']}.html"><span>← Previous</span>{e(prev_c['title'])}</a>
<a href="{next_c['slug']}.html"><span>Next →</span>{e(next_c['title'])}</a>
</nav>
</div>
"""
    page(f"work/{slug}.html", f"{c['title']} | Keith Rollins", c["card"], cp, "work.html")

# ---------------- ABOUT
about = """
<section class="case-hero"><div class="wrap">
<span class="eyebrow">About</span>
<h1>A direct response writer with a mechanic's habits</h1>
<p class="lede">I lead marketing communications at APMEX and its affiliated brands. I got here the long way, and it's why I work the way I do.</p>
</div></section>
<div class="wrap"><div class="case-body about-grid">
<article class="prose">
<h2>The story</h2>
<p>For eight years I ran an auto repair shop in Stillwater, leading a crew of five to eight people. The job taught me to diagnose before I fix, to explain technical problems in plain words, and to earn the trust of customers who assumed they were about to be oversold.</p>
<p>When my kids were young I stayed home with them full time and started freelance copywriting: direct response, email, SEO and product copy, much of it for automotive brands like FIXD. That time at home taught me more than any job has. It's where I learned to manage my own pipeline, deadlines and revisions with no one checking in.</p>
<p>In 2023 I joined APMEX, one of the largest online precious metals retailers in the U.S. Today I lead marketing communications across APMEX and its affiliates: social strategy for three brands, press releases and earned media, campaigns, content, print and out-of-home advertising, email copy and analysis, and the AI-built tools my team uses every day. In my first months I was named Employee of the Quarter.</p>
<h2>How I work</h2>
<ul>
<li><b>Diagnose first.</b> Find what's actually broken before proposing a fix. The partner email review started with the tracking, not the creative.</li>
<li><b>Write for skeptics.</b> Plain facts, no hype. If a claim can't be proven, it doesn't go in.</li>
<li><b>Plan channels together.</b> Email, social, PR and content work best as one program.</li>
<li><b>Report the truth.</b> A recap that names its weak spot earns more trust than one that only lists wins.</li>
</ul>
<h2>What I'm looking for</h2>
<p>A full-time role leading email and lifecycle marketing, remote or in the Oklahoma City area. I'm especially interested in fitness, finance, supplements and e-commerce brands.</p>
</article>
<aside class="aside" style="gap:24px">
<div style="display:grid;gap:12px"><span class="eyebrow">Career</span>
<ol class="timeline">
<li><span class="when">2023 – now</span><b>Marketing Communications Lead</b><span>APMEX, Oklahoma City</span></li>
<li><span class="when">2020 – 2023</span><b>Freelance copywriter and stay-at-home dad</b><span>FIXD, HotCars and others</span></li>
<li><span class="when">2019 – 2020</span><b>Parts Professional</b><span>Janzen Toyota, Stillwater</span></li>
<li><span class="when">2011 – 2019</span><b>Shop Manager</b><span>Downtown 66, Stillwater</span></li>
</ol></div>
<div style="display:grid;gap:10px"><span class="eyebrow">Tools</span><div class="chips"><span>Sprout Social</span><span>Brand24</span><span>GA4</span><span>Search Console</span><span>Botify</span><span>Mailchimp reporting</span><span>Notified</span><span>Qwoted</span><span>Jira</span><span>Claude</span></div></div>
<div style="display:grid;gap:10px"><span class="eyebrow">Learning</span><div class="chips"><span>Anthropic Academy: Claude 101</span><span>AI Fluency</span></div></div>
<div style="display:grid;gap:10px"><span class="eyebrow">Recognition</span><div class="chips"><span>APMEX Employee of the Quarter, Q4 2023</span><span>Valedictorian, Hooker High School</span></div></div>
</aside>
</div></div>
"""
page("about.html", "About | Keith Rollins", "From running an auto repair shop to leading marketing communications at APMEX: Keith Rollins' story and how he works.", about, "about.html")

# ---------------- DCF
dcf = """
<section class="case-hero"><div class="wrap">
<div class="crumbs"><span>Currently building</span></div>
<h1>Dungeon Crawler Fitness</h1>
<p class="lede">A fitness app that turns workouts into a dungeon crawl. It started as a board game I designed. Now I'm building its email program from zero, and documenting every step here.</p>
<dl class="factbar">
<div><dt>My role</dt><dd>Creator; owner of all marketing</dd></div>
<div><dt>Industry</dt><dd>Fitness</dd></div>
<div><dt>Email platform</dt><dd>Kit</dd></div>
<div><dt>Status</dt><dd>Prototype in playtesting</dd></div>
</dl>
</div></section>
<div class="wrap"><div class="case-body">
<article class="prose">
<h2>Why this project is here</h2>
<p>Most of my email work at APMEX was done with a team. This project is mine end to end: strategy, list growth, automation, segmentation, copy, testing and reporting. When it has results, they'll be real and they'll be here.</p>
<h2>The game</h2>
<p>Players complete quest cards made of bodyweight exercises to earn XP and gold, fight floor bosses, keep streaks alive and grow a five-skill character. The design is locked; a working prototype is being playtested.</p>
<h2>The email plan</h2>
<ol>
<li><b>Waitlist.</b> An honest landing page on Kit. No fake scarcity, no invented testimonials, no results claims.</li>
<li><b>Welcome sequence.</b> Introduce the game, the creator and what's coming, and learn what each subscriber wants.</li>
<li><b>Build-log newsletter.</b> Regular updates from the build, so the list stays warm until launch.</li>
<li><b>Segmentation.</b> Tag subscribers by fitness level and interest to tailor launch messaging.</li>
<li><b>Launch campaign.</b> A paced sequence to turn the waitlist into first players.</li>
<li><b>Reporting.</b> List growth, opens, clicks and conversions, published here.</li>
</ol>
</article>
<aside class="aside">
<div class="results"><h2>Progress</h2>
<ul class="checklist" style="padding:0">
<li class="done">Game system designed</li>
<li class="now">Prototype in playtesting</li>
<li class="now">Email waitlist page</li>
<li>Welcome sequence</li>
<li>Build-log newsletter</li>
<li>Launch campaign and results</li>
</ul></div>
<p class="note">The app and its sign-up will live at <a href="https://dungeoncrawlerfitness.com" target="_blank" rel="noopener">dungeoncrawlerfitness.com</a>.</p>
</aside>
</div></div>
"""
page("dungeon-crawler-fitness.html", "Dungeon Crawler Fitness | Keith Rollins", "Keith Rollins is building the email program for Dungeon Crawler Fitness, a gamified fitness app, from zero and documenting the results.", dcf, "dungeon-crawler-fitness.html")

# ---------------- CONTACT
contact = f"""
<section class="case-hero"><div class="wrap">
<span class="eyebrow">Contact</span>
<h1>Let's talk about your next program.</h1>
<p class="lede">I'm looking for a full-time role leading email and lifecycle marketing, remote or in the Oklahoma City area. The fastest way to reach me is email.</p>
<div class="idcard" style="margin-top:28px;max-width:560px">
<dl>
<dt>Email</dt><dd><span class="addr" style="color:var(--ink)">{EMAIL}</span></dd>
<dt>Location</dt><dd>Edmond, OK</dd>
<dt>Resume</dt><dd><a href="files/Keith_Rollins_Resume.pdf">Download PDF</a></dd>
</dl>
<div class="btns"><button class="btn primary" type="button" data-copy="{EMAIL}">Copy email address</button><span class="toast" aria-live="polite"></span></div>
</div>
</div></section>
"""
page("contact.html", "Contact | Keith Rollins", "Contact Keith Rollins about email and marketing communications roles.", contact, "contact.html")

# ---------------- COLOPHON
col = f"""
<section class="case-hero"><div class="wrap">
<div class="crumbs"><a href="work.html">Work</a><span>/</span><a href="work.html#ai">AI &amp; operations</a></div>
<h1>How I built this site</h1>
<p class="lede">This portfolio is part of my work. I researched, wrote and coded it with Claude as a working partner, and I made every call about what's true and what goes in.</p>
<dl class="factbar">
<div><dt>My role</dt><dd>Owner, editor, director</dd></div>
<div><dt>AI partner</dt><dd>Claude</dd></div>
<div><dt>Code</dt><dd>Hand-written HTML and CSS</dd></div>
<div><dt>Hosting</dt><dd>GitHub Pages</dd></div>
</dl>
</div></section>
<div class="wrap"><div class="case-body">
<article class="prose">
<h2>What AI did, and what I did</h2>
<ul>
<li><b>Research.</b> Claude pulled my author pages and counted my published work: 63 APMEX articles and 20 FIXD guides. It read public view counts to find which of my social formats outperformed.</li>
<li><b>Honesty rules.</b> I set the rule that every project names my exact role and every number traces to a source. Where I supported a team, the page says so.</li>
<li><b>Writing.</b> Claude drafted from my notes and case study kit. I corrected roles, cut what wasn't mine and approved every claim.</li>
<li><b>Code.</b> Plain HTML and one stylesheet, no framework, so it loads fast and runs anywhere.</li>
</ul>
<h2>Why it matters</h2>
<p>AI Fluency isn't typing prompts. It's knowing what to delegate, describing it clearly, checking the result and owning what ships. This site is a working example.</p>
</article>
<aside class="aside">
<div class="results"><h2>Built for</h2><ul><li>A 60-second skim: the home page leads with who I am and the numbers.</li><li>Depth on demand: {len(CASES)} case studies, one template.</li><li>Phones, dark mode and screen readers.</li><li>Search: page titles, descriptions and structured data.</li></ul></div>
</aside>
</div></div>
"""
page("how-i-built-this-site.html", "How I Built This Site | Keith Rollins", "How Keith Rollins built his portfolio with Claude: research, honesty rules, writing and code.", col)

# assets
HERE = os.path.dirname(os.path.abspath(__file__))
shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)
shutil.copytree(os.path.join(HERE, "emails"), os.path.join(OUT, "emails"), dirs_exist_ok=True)
shutil.copytree(os.path.join(HERE, "files"), os.path.join(OUT, "files"), dirs_exist_ok=True)
open(os.path.join(OUT, "CNAME"), "w").write("keithrrollins.com\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("built", len(CASES) + 6, "pages into", os.path.relpath(OUT, ROOT))

if not LIVE and len(sys.argv) == 1:
    shutil.rmtree(DOCS, ignore_errors=True)
    os.makedirs(DOCS)
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(DOCS, "assets"))
    hold = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Keith Rollins | Marketing Strategist and Communications Leader</title>
<meta name="description" content="Keith Rollins, marketing strategist and communications leader. Full portfolio coming soon.">
<meta name="robots" content="noindex">
{FONTS}
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<main id="main" class="hold">
<div class="wrap">
<span class="eyebrow">keithrrollins.com</span>
<h1>Keith Rollins</h1>
<p class="hold-title">Marketing strategist and <em>communications leader.</em></p>
<p class="lede">I lead marketing communications at APMEX across strategy, email, social, PR, content and paid media. My full portfolio is getting a final check and will be here soon.</p>
<div class="readout hold-card">
<div class="readout-head"><span>Diagnostic report · K. Rollins</span><span>Status: final inspection</span></div>
<div class="hold-body">
<span class="addr">{EMAIL}</span>
<div class="btns"><button class="btn primary" type="button" data-copy="{EMAIL}">Copy email address</button><span class="toast" aria-live="polite"></span></div>
</div>
</div>
</div>
</main>
<script src="assets/site.js"></script>
</body>
</html>
"""
    open(os.path.join(DOCS, "index.html"), "w").write(hold)
    open(os.path.join(DOCS, "404.html"), "w").write(hold)
    open(os.path.join(DOCS, "CNAME"), "w").write("keithrrollins.com\n")
    open(os.path.join(DOCS, ".nojekyll"), "w").write("")
    print("docs/ now holds the coming-soon page (LIVE = False)")
