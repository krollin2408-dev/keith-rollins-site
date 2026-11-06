# keithrrollins.com — working rules

Keith Rollins' portfolio site. A living project: it grows as Keith does new work.

## How the site is built

- `src/content.py` holds all words: HERO, CHAPTERS, QUOTE, STORY (the My Story page), WORK (featured projects, shown work-first), ALSO (smaller items listed on the Work page without their own pages), FEATURED (home page cards), FIXD (guide slugs). Edit content here, never in `docs/` or `preview/`.
- `src/build.py` generates every page: home, story, work, `work/<slug>.html`, resume (rendered from `src/resume/resume.html`, so the resume page and PDF never disagree), contact, dungeon-crawler-fitness, how-i-built-this-site. Run `python3 src/build.py` from the repo root.
- `src/assets/site.css` / `site.js`: plain CSS/JS, no framework. `src/images/` (headshot, Coinage ad), `src/emails/` (Bullion Card series), `src/files/` (public resume PDF).
- **Design: "The Workshop"** (chosen by Keith, Nov 2026): Archivo condensed uppercase headlines, Source Serif 4 body, JetBrains Mono labels; concrete gray `#E8E7E3`, ink `#1C1F22`, toolbox red `#B8322A`; heavy 3px rules; a dark "How I work" band. Light and dark themes are both required. Copy voice: Keith's first person, plain and warm (the "C" wording he picked).
- `docs/` is what GitHub Pages serves (`main` → `/docs`, custom domain keithrrollins.com, HTTPS enforced).

## How to update (playbook)

Keith asks for changes in plain English. Do the work end to end, then tell him what changed in one or two sentences.

- **Site wording or a page:** edit `src/content.py` (case studies, groups) or the page templates in `src/build.py`, run `python3 src/build.py`, commit, push.
- **Resume:** edit `src/resume/resume.html`, run `python3 src/build_resume.py` (public PDF, no phone) and confirm it is still one page, then `python3 src/build.py`, commit, push. Keep the site and resume consistent: if a fact changes on one, change it on the other.
- **Application copy of the resume (with phone):** `python3 src/build_resume.py --phone "<number>"` writes to `private/` (git-ignored). Send it to Keith; never commit it.
- **Photos:** resize for the web (max ~1600px wide, compressed JPEG/WebP), put them in `src/images/`, copy them in `build.py` like `emails/`, and give every image real alt text.
- **New project:** add a dict to `WORK` in `src/content.py` (or a line to `ALSO`) with Keith's exact role, sources for every number, and the right `group`.
- **Design:** change `src/assets/site.css`; keep both light and dark themes working and check phone width (~390px).
- **After any change:** add a line to the log in `PROJECT_HISTORY.md`.
- Publishing is automatic: a push to `main` updates keithrrollins.com in about two minutes. Review bigger changes in a private preview before pushing, since every push to `main` goes live.
- PDF builds need Playwright (`pip install playwright && python3 -m playwright install chromium`); fonts for the resume are in `src/resume/fonts/`.

## Content rules (set by Keith; do not break these)

1. **Every project names Keith's exact role.** Where he supported a team or specialist, the page says so (e.g. the Bullion Card emails: copy and messaging by Keith; designed and built by the email specialist; YouTube: Keith schedules and writes descriptions, not titles).
2. **No number without a source.** Every stat traces to Keith's own reports, his case study kit, or a public page. Never invent or round up results.
3. **The site tells Keith's story.** Home: who he is right now, the chapter teaser, the quote, three featured pieces. Show the actual work (images, emails, links) before describing it. Keep the featured set curated (about 9); smaller items go in ALSO. Assume a visitor spends one to two minutes on the home page.
4. **Positioning:** marketing strategist and communications leader. Resume title: Email & Marketing Communications Lead. Target roles: email and lifecycle marketing leadership, remote or Oklahoma City. Target industries: fitness, finance, supplements, e-commerce.
5. **APMEX has cleared** naming APMEX, OneGold, Bullion International Group and these projects publicly.
6. **Live since Nov 6, 2026.** `LIVE = True` in `src/content.py`: the full site builds into `docs/` (with 404, sitemap.xml, robots.txt, CNAME). Set `LIVE = False` to put the coming-soon page back. No LinkedIn link until Keith says his profile is updated.
7. **Keep personal contact details out of this public repo** beyond the email address already on the site. The public resume PDF (`src/files/Keith_Rollins_Resume.pdf`) omits the phone number on purpose to avoid scam calls; the application copy with phone builds to `private/` and is never committed.

## Known facts (verified)

- Joined APMEX (flagship brand of Bullion International Group) Aug 2023; Marketing Communications Lead, Brand Marketing, leading channels across multiple B.I.G. brands (APMEX, OneGold and affiliates). Employee of the Quarter Q4 2023. **Frame Keith's role as Bullion International Group across its brands** (Keith's instruction, Nov 2026); individual pieces keep the brand they ran under (e.g. "Print · APMEX").
- 63 bylined APMEX Knowledge Center articles (learn.apmex.com/author/keith-rollins/); 20 FIXD "Best & Worst Years" guides (2023, freelance).
- Social he owns: 3 brands; selected and rolled out Sprout Social across 8+ platforms. Stack-value format (his strategy and writing; video team produced): TikTok 420.5K and 239.5K views; Instagram 50.9K, 24.1K, 23.7K.
- APMEX Is the Spot (Aug 2026, his campaign): ~2/3 of week's link clicks; link clicks +~25%; net follower growth +~33%.
- Career: shop manager, Downtown 66, Stillwater (2011–2019), running every side of the shop: sales, customer service, bookkeeping, scheduling, operations, hiring, training and leading a team of 5–8; freelance copywriter and stay-at-home parent (2020–2023). **Do not mention Janzen Toyota** anywhere (Keith's instruction).

## Open items

- Sprout Social growth reports (followers, impressions, engagement over 3 years) — strongest missing stat.
- Notified pickup numbers; remaining press releases.
- HotCars and Copywriting.org links.
- Confirm Bullion Card series year (2023 taken from the email footer).
- Dungeon Crawler Fitness: update its progress checklist and add real email metrics as they arrive.
