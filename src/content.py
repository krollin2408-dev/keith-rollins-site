# Site content for keithrrollins.com. Every claim traces to Keith's own words, his case study kit,
# or a public page he wrote. Edit words here; run `python3 src/build.py` to rebuild.

# Set LIVE = True to publish the full site to keithrrollins.com. False shows a coming-soon page.
LIVE = True
EMAIL = "keithrrollins@gmail.com"
SITE = "https://keithrrollins.com"

HERO = dict(
    label="Right now",
    headline="I'm Keith. I make brands sound like people again.",
    lede="Today I lead marketing communications across the brands of Bullion International Group, including APMEX, one of the biggest precious metals retailers in the country. Ten years ago I was running a repair shop in Stillwater. Here's how I got from there to here, and what I can build for you.",
)

# The four chapter teasers on the home page (dates, title, one line).
CHAPTERS = [
    ("2011 – 2019", "The shop", "Running every part of a small business: sales, service, the books and the crew."),
    ("2020 – 2023", "Home", "Raising my kids and writing copy that sells, one freelance job at a time."),
    ("2023 – now", "B.I.G.", "From articles to leading communications for a family of brands."),
    ("Next", "Your team", "What I want to build next, with email at the center."),
]

QUOTE = ("Diagnosing a car and diagnosing a campaign work the same way.",
         "Find what's actually broken, fix it, then check that the fix held.")

# The full story page. Each section: (label, heading, paragraphs). Plain first person.
STORY = [
    ("Right now", "Marketing Communications Lead", [
        "I'm the Marketing Communications Lead for Bullion International Group, based in Oklahoma City. B.I.G. is the company behind APMEX, one of the largest online precious metals retailers in the U.S., OneGold and several other brands, and I lead communications channels across them. In a single week I might write a press release, plan a campaign, dig through email numbers, steer social media for several brands, and build a tool with AI that saves my team time every morning.",
        "Precious metals buyers are some of the most skeptical customers there are. They've seen every hype cycle. Writing for them taught me to keep things plain, specific and honest.",
        "Of everything I do, email is where I get the most out of the work: one message, one reader, one clear reason to act. That's where I want to spend my next chapter.",
    ]),
    ("2011 – 2019", "The shop", [
        "For eight years I managed Downtown 66, an auto repair shop in Stillwater, Oklahoma. In a small shop, the manager runs all of it, and I did. I sold the work and handled customer service. I kept the books and the schedule. I hired, trained and led a crew of five to eight people. If the shop needed it to stay open, it was my job.",
        "Most people walked into the shop expecting to get taken. You don't win those people over with a pitch. You win them by explaining the problem in plain words, fixing what's actually broken and standing behind the work. Sales, service, operations and marketing, all in one job. I just didn't call it marketing yet.",
    ]),
    ("2020 – 2023", "Home", [
        "In 2020 I stepped away to stay home with my kids. It's the most important job I've ever had, and it taught me more than any other. It's where I learned to run my own schedule, my own pipeline and my own deadlines, with nobody checking in.",
        "It's also when I started freelancing as a copywriter: direct response, email, SEO and product copy, much of it for automotive brands. For FIXD I wrote 20 data-heavy guides to the best and worst years of popular cars. A decade of fixing cars, it turns out, makes you pretty good at telling people which ones to buy.",
    ]),
    ("2023 – now", "Bullion International Group", [
        "In August 2023 I joined APMEX, the flagship brand of Bullion International Group, and that winter I was named Employee of the Quarter. The job has kept growing ever since, and today it reaches across B.I.G.'s family of brands.",
        "Today I lead social strategy for multiple B.I.G. brands. I chose Sprout Social and rolled it out across the company. I write and distribute our press releases, and I built the plan to bring the PR program to our sister brands. I run campaigns like APMEX Is the Spot, plan print and billboard buys, write email for programs like the Bullion Card, and report results to leadership every month. I've written 63 articles for the APMEX Knowledge Center along the way.",
        "I've also become the person people come to about AI. I build tools with Claude that my team uses every day.",
    ]),
    ("Next", "Your team", [
        "I want to lead email, SMS and lifecycle marketing for a brand that cares about getting it right. Fitness, finance, supplements and e-commerce are at the top of my list, remote or here in Oklahoma City.",
    ]),
]

# Featured work, in display order. kind: "image" shows a picture on the card; "stat" shows a big number.
WORK = [
dict(slug="coinage-print-ad", title="A full-page ad for skeptics", label="Print · APMEX · 2026",
     role="Concept and copy", kind="image", image="images/coinage-print-ad.jpg",
     image_alt="APMEX full-page Coinage magazine ad headlined Graded American Eagles for the Serious Collector",
     summary="A full-page Coinage magazine ad for collectors who have seen every pitch.",
     show="ad",
     body=[
       ("The brief", "<p>Coin collectors who read Coinage know more than most salespeople. A generic \"shop with us\" ad would get flipped past. The ad had to earn attention with facts this audience already respects.</p>"),
       ("What I did", "<p>I researched print placements for two audiences, precious metals investors and pop-culture coin buyers, then wrote an ad built on proof instead of adjectives. It leads with two facts serious collectors care about: APMEX is an authorized purchaser of the U.S. Mint, so new American Eagles are available the day they're released, and its graded coins are certified by PCGS, NGC and CAC.</p>"),
       ("Why it works", "<ul><li>The headline names the reader: the serious collector.</li><li>Every claim is checkable, with no superlatives.</li><li>One clear next step, with a QR code for readers holding the magazine.</li></ul>"),
     ]),
dict(slug="bullion-card-emails", title="Eight emails to a first purchase", label="Email · APMEX",
     role="Copy and messaging; designed and built by the email specialist", kind="image", image="emails/02-flash.jpg",
     image_alt="Bullion Card email with a 72-hour countdown timer",
     summary="A five-stage lifecycle series that moves new cardholders from approval to their first bonus.",
     show="series",
     body=[
       ("The brief", "<p>New Bullion Card holders earn bonus points by hitting a spend target before a deadline. The series had to get them to a first purchase, keep them moving and close before time ran out.</p>"),
       ("What I did", "<p>I wrote the messaging for all eight emails across five stages, and partnered with our email specialist on the sequencing. The deadline tightens from 60 days to 45, 25 and 5. A personalized progress bar shows the dollars left to the bonus, a 72-hour countdown offer drives the first purchase, and the midpoint email cross-sells AutoInvest and the Knowledge Center.</p>"),
       ("What I'd test next", "<ul><li>Subject lines that lead with points left versus days left.</li><li>A re-engagement branch for cardholders who stall halfway.</li><li>Send-time tests for the 72-hour offer.</li></ul>"),
     ]),
dict(slug="apmex-is-the-spot", title="APMEX Is the Spot", label="Campaign · APMEX · 2026",
     role="Campaign lead", kind="stat", stat="~2/3", stat_note="of the week's social media link clicks came from campaign posts",
     summary="A one-week at-spot promotion, built so the explanation would outlive the offer.",
     body=[
       ("The brief", "<p>APMEX sold silver dollars at spot price for one week. \"At spot\" is a strong offer, but plenty of newer buyers don't know what it means, and a one-week promotion leaves little behind once it ends.</p>"),
       ("What I did", """<ul><li>Wrote an evergreen explainer, <a href="https://learn.apmex.com/investing-guide/what-does-at-spot-mean/" target="_blank" rel="noopener">What Does "At Spot" Mean?</a>, that keeps working in search and AI answers.</li><li>Wrote a 76-word vertical video script that can run again with any future at-spot offer.</li><li>Wrote and distributed the <a href="https://www.globenewswire.com/news-release/2026/08/11/3342819/0/en/this-week-only-apmex-offers-silver-dollars-at-spot-through-august-16.html" target="_blank" rel="noopener">press release</a> through Notified.</li><li>Tagged every campaign post so the campaign could be measured on its own, then wrote the recap for leadership.</li></ul>"""),
       ("What happened", "<ul><li>Campaign posts drove nearly two-thirds of the social account's link clicks that week.</li><li>Total social link clicks rose about 25% week over week, and net follower growth rose about 33%.</li><li>One thing to improve: engagement per post was lower than our other content. I said so in the recap and recommended fewer, sharper at-spot posts next time.</li></ul>"),
     ]),
dict(slug="stack-value-videos", title="What a stack of silver is worth", label="Social video · APMEX · 2025 – 2026",
     role="Concept and scripts; produced by the APMEX video team", kind="stat", stat="420K", stat_note="views on the top video, 440 times the channel's typical video",
     summary="A short-form idea anyone gets in one second: a real stack of metal, and its dollar value.",
     body=[
       ("The idea", "<p>Precious metals content tends to be charts and commentary. I came up with a simpler format: show a physical stack of metal and put a price on it, or show what the same stack was worth then and now. I wrote the videos; our video team shot and edited them.</p>"),
       ("What happened", """<div class="tablewrap"><table><thead><tr><th>Platform</th><th>Video</th><th>Views</th></tr></thead><tbody>
<tr><td>TikTok</td><td>10 kilo silver bars, stacked</td><td class="num">420.5K</td></tr>
<tr><td>TikTok</td><td>What $5,000 looks like in silver vs. gold</td><td class="num">239.5K</td></tr>
<tr><td>Instagram</td><td>A growing silver stack worth almost $30K</td><td class="num">50.9K</td></tr>
<tr><td>Instagram</td><td>28 Gold Eagles, one year later</td><td class="num">24.1K</td></tr>
<tr><td>Instagram</td><td>A $1,000 silver stack, months later</td><td class="num">23.7K</td></tr>
</tbody></table></div><p class="note">The channels' typical videos get about 955 views on TikTok and 2,400 on Instagram. Public view counts, October 2026.</p>"""),
     ]),
dict(slug="partner-email-review", title="Which emails actually paid for themselves", label="Email analysis · APMEX · 2026",
     role="Analyst and report author", kind="stat", stat="7 sends", stat_note="audited; 3 hidden tracking gaps found",
     summary="An audit of paid partner email that showed what was working, and what the tracking was hiding.",
     body=[
       ("The brief", "<p>APMEX pays a coin pricing publication to email its collector audience. Every send costs money, but nobody could say which ones paid for themselves, because the numbers lived in two places that didn't agree.</p>"),
       ("What I did", "<p>I pulled all seven sends into one view: delivery, opens, clicks, click-to-open rate, list health and revenue. Then I compared the creative, and checked the email clicks against our own site data to see whether the tracking could be trusted.</p>"),
       ("What I found", "<ul><li>The send with the offer in the subject line had the best open rate.</li><li>Fewer than half the sends covered their cost in tracked revenue.</li><li>Three tracking problems were hiding results: shared campaign tags, links losing their tracking codes, and purchases going unrecorded.</li><li>I set a unique tracking tag for every send and a break-even bar each one has to clear.</li></ul>"),
     ]),
dict(slug="podcast-outreach", title="A four-week email sequence to book experts", label="Email outreach · APMEX · 2026",
     role="Outreach lead", kind="stat", stat="11", stat_note="vetted experts, two waves, three templates",
     summary="A paced outreach sequence to book credible guests for the Market Pulse Podcast.",
     body=[
       ("The brief", "<p>The Market Pulse Podcast wants experts who can argue both sides of the metals market, not promoters. Booking guests was feast or famine.</p>"),
       ("What I did", "<p>I built a shortlist of 11 experts, each with a reason they fit and anything to watch out for. Then I wrote a four-week, two-wave email sequence: the first wave goes out in week one, the second in week three, so early replies set the pace. Every email names the topic and the host and offers the questions in advance.</p>"),
       ("The first email", """<blockquote><span class="subj">Subject: Invitation: Market Pulse Podcast conversation on [specific topic]</span><p>Dr. [Last name],</p><p>I'm Keith Rollins, Marketing Communications Lead at APMEX. Our Market Pulse Podcast is hosted by our Head of Media Relations and focuses on balanced, fact-driven conversations about precious metals, with no hype and no sales pitches.</p><p>I'm writing because of your [work / book / recent comments]. We would value your view on [one specific question], including where you see risks as well as opportunities.</p><p>The recording is remote, about 30 to 60 minutes, and we can share the question outline ahead of time. Recent episodes include [episode title and link].</p><p>Would you be open to a conversation? I can send a few times or our booking link.</p></blockquote>"""),
     ]),
dict(slug="press-releases", title="Press releases on the wire", label="PR · APMEX · 2026",
     role="Writer and media contact", kind="stat", stat="Notified", stat_note="wire distribution, written and sent by me",
     summary="Releases on promotions, milestones and community giving, distributed through Notified.",
     body=[
       ("What I do", "<p>I write APMEX's press releases, send them out over the wire through Notified (GlobeNewswire) and serve as a media contact. I lead with the news a reporter can use and leave the adjectives out.</p>"),
       ("Recent releases", """<ul><li><a href="https://www.globenewswire.com/news-release/2026/08/25/3350528/0/en/apmex-celebrates-26-years-of-providing-direct-access-to-physical-precious-metals.html" target="_blank" rel="noopener">APMEX Celebrates 26 Years of Providing Direct Access to Physical Precious Metals</a> · Aug 25, 2026</li><li><a href="https://www.globenewswire.com/news-release/2026/08/11/3342819/0/en/this-week-only-apmex-offers-silver-dollars-at-spot-through-august-16.html" target="_blank" rel="noopener">This Week Only: APMEX Offers Silver Dollars at Spot Through August 16</a> · Aug 11, 2026</li><li><a href="https://www.globenewswire.com/news-release/2026/06/02/3305385/0/en/apmex-employees-raise-55-000-for-regional-food-bank-of-oklahoma-during-annual-fun-week-fundraiser.html" target="_blank" rel="noopener">APMEX Employees Raise $55,000 for Regional Food Bank of Oklahoma</a> · Jun 2, 2026</li></ul>"""),
     ]),
dict(slug="fixd-guides", title="Car advice from a mechanic", label="Freelance · FIXD · 2023",
     role="Freelance writer", kind="stat", stat="20", stat_note="data-driven car buying guides",
     summary="Long-form guides to the best and worst years of popular cars, written for FIXD.",
     show="fixd",
     body=[
       ("What they are", "<p>As a freelancer I wrote FIXD's Best &amp; Worst Years guides. Each one helps a shopper pick a used car with charts on reliability, safety, fuel economy and repair costs, a year-by-year review, answers to common questions, and a natural path to the FIXD sensor.</p><p>Ten years of fixing cars is why they read like advice from a mechanic.</p>"),
     ]),
dict(slug="knowledge-center", title="63 articles that teach and sell", label="Content · APMEX · 2023 – now",
     role="Writer", kind="stat", stat="63", stat_note="bylined articles on the APMEX Knowledge Center",
     summary="Plain-English articles on investing, history and selling, each with a next step.",
     body=[
       ("What I write", "<p>The Knowledge Center is where APMEX teaches buyers and collectors. My articles turn monetary history and economics into plain English, then point readers toward their next step. They include a 12-part How to Sell series that supports the buyback program, explainers on topics like quantitative easing and the CPI, and dozens of history pieces.</p>"),
       ("A favorite", """<p><a href="https://learn.apmex.com/investing-guide/gold/you-bought-your-first-gold-bar-now-what/" target="_blank" rel="noopener">You Bought Your First Gold Bar, Now What?</a> is written for first-time buyers coming from big-box stores. It works like a welcome email series in article form: storing it, tracking its value, buying more and selling, with a clear next step at each stage.</p>"""),
     ]),
]

# Smaller things that show range but don't need their own page.
ALSO = [
    ("Digital billboards", "A 12-week, three-board Tampa plan compared on reach and cost, with a cheaper fallback built in."),
    ("Product launch", "Video scripts, a 12-post launch story and native ads for the OneGold Card."),
    ("Holiday season", "Black Friday through the 12 Days of Deals, with a 27-video social plan."),
    ("Brand voice", "Separate voice standards for APMEX and OneGold that any writer can follow."),
    ("Social tools", "Chose Sprout Social and rolled it out across 8+ platforms company-wide."),
    ("YouTube", "Publishing schedule and SEO descriptions for 190+ videos on a 186K-subscriber channel."),
    ("Reporting", "The monthly Brand Marketing Report for leadership."),
    ("AI tools", "A daily start page, a live team calendar and a social listening digest, built with Claude."),
]

FEATURED = ["coinage-print-ad", "bullion-card-emails", "fixd-guides"]

FIXD = ["audi-a4","buick-enclave","buick-lesabre","cadillac-cts","cadillac-deville","cadillac-srx","chevrolet-avalanche","chevrolet-cobalt","chevrolet-trailblazer","ford-fiesta","ford-fusion","gmc-envoy","lexus-rx300","nissan-altima","nissan-maxima","nissan-pathfinder","nissan-sentra","nissan-titan","pontiac-g6","toyota-corolla"]
