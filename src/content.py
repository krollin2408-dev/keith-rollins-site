# Site content. Every claim here traces to Keith's kit, his ledger answers, or public pages he wrote.
# Set LIVE = True to publish the full site to keithrrollins.com. False shows a coming-soon page.
LIVE = False
EMAIL = "keithrrollins@gmail.com"
SITE = "https://keithrrollins.com"

GROUPS = [
    ("email", "Email & lifecycle", "Send analysis, sequences and email copy.",
     "How the inbox earns its keep: performance audits, lifecycle series and outreach sequences."),
    ("campaigns", "Campaigns", "Integrated launches and promotions with measured results.",
     "Multi-channel campaigns planned end to end, with results reported honestly."),
    ("social", "Social", "Strategy, formats and the systems behind three brands.",
     "Social strategy for APMEX and its affiliated brands, and the tooling that keeps it measurable."),
    ("pr", "PR & media", "Press releases, earned media and expert programs.",
     "Wire distribution, media relations and programs that bring credible voices to the brand."),
    ("advertising", "Advertising", "Out-of-home and print, planned against the numbers.",
     "Paid media plans built for a fast executive decision."),
    ("strategy", "Strategy & brand", "Positioning, voice standards and leadership reporting.",
     "The frameworks that keep many writers, channels and brands consistent and measurable."),
    ("writing", "Writing", "83 published articles across finance and automotive.",
     "Long-form SEO content that teaches, ranks and moves readers to act."),
    ("ai", "AI & operations", "Tools built with AI that save the team time every day.",
     "AI Fluency in practice: working tools, and this site itself."),
]

# Each case: slug, group, title, card, stat (big, small), brand, year, role, own, status, lede,
# body (list of (heading, html)), results (list), tools, extra (html after body), links
CASES = [
# ---------------- EMAIL
dict(slug="partner-email-review", group="email", title="Partner Email Performance Review",
 card="Seven paid partner sends audited in one view. Three hidden tracking gaps found, and a break-even bar set for every future send.",
 stat=("7 sends", "audited; 3 tracking gaps found"), brand="APMEX", year="2026", role="Analyst and report author", own="Owned", status="Delivered",
 lede="APMEX pays a numismatic pricing publication to email its collector audience. Nobody could say which sends paid for themselves. I built the view that could.",
 body=[
  ("The problem", "<p>Each partner send has a real cost. The data was split between the partner's email platform reports and our own analytics, so the honest answer to \"is this working?\" was \"we think so.\"</p>"),
  ("What I did", "<ul><li>Pulled all seven sends into one deck: delivery, opens, clicks, click-to-open, list health and revenue.</li><li>Compared creative across sends to find what actually drove opens and clicks.</li><li>Reconciled email-platform clicks against analytics sessions to test whether tracking could be trusted.</li><li>Wrote six recommendations for the next send, split between creative and measurement.</li></ul>"),
  ("The tracking gaps", "<ol><li><b>Reused campaign tags.</b> Several sends shared one tag, so analytics couldn't split revenue by email.</li><li><b>Lost sessions.</b> On four sends, analytics recorded only about half to two-thirds as many sessions as the email platform had clickers. Link redirects were likely stripping UTM parameters.</li><li><b>Missing revenue.</b> One campaign showed heavy engagement and long time on site with no recorded revenue, which pointed to purchases going untracked.</li></ol>"),
  ("What wins in this inbox", "<p>The send with the offer in the subject line earned the best open rate. Vintage and historic pieces with a real price hook and several product entry points drove the most engagement.</p>"),
 ],
 results=["Fewer than half the sends covered their cost in tracked revenue, a fact nobody could see before.", "A unique UTM per send and a break-even bar for every future send.", "Clear creative direction: put the offer in the subject line and lead with a price hook."],
 tools="GA4, Mailchimp reports, PowerPoint"),

dict(slug="bullion-card-activation", group="email", title="Bullion Card Activation Series",
 card="Eight emails across five stages that move new cardholders from approval to their first bonus, with urgency that tightens on schedule.",
 stat=("8 emails", "across a 5-stage lifecycle series"), brand="APMEX", year="2023", role="Copy and messaging", own="Copy and messaging", status="Shipped",
 lede="New Bullion Card holders earn bonus points by hitting a spend target before a deadline. The series gets them to the first purchase, keeps them moving and closes before time runs out.",
 body=[
  ("My role", "<p>I wrote the messaging for all eight emails. The email specialist designed and built them. We partnered on sequencing and urgency.</p>"),
  ("How the series works", "<ul><li><b>Urgency on a schedule.</b> The deadline tightens from 60 days to 45, 25 and finally 5.</li><li><b>A goal you can see.</b> A personalized progress bar shows the dollars left before the bonus.</li><li><b>A reason to buy now.</b> A 72-hour countdown offer with featured products drives the first spend.</li><li><b>Depth, not just pressure.</b> The midpoint email cross-sells AutoInvest and the Knowledge Center.</li><li><b>Variants.</b> Different product pairings, with and without the progress tracker.</li></ul>"),
  ("What I'd test next", "<ul><li>Subject lines that lead with points remaining versus days remaining.</li><li>A re-engagement branch for cardholders who stall halfway to the target.</li><li>Send-time testing for the 72-hour offer.</li></ul>"),
 ],
 results=["A complete lifecycle journey: offer, urgency, progress and reward.", "Dynamic content (progress bar, countdown timer) in every stage that needed it.", "Cross-sell into recurring purchases built into the middle of the series."],
 tools="Copy in partnership with the email specialist",
 extra="series"),

dict(slug="podcast-guest-outreach", group="email", title="Podcast Guest Outreach Sequence",
 card="A vetted shortlist of 11 experts and a paced four-week, two-wave email sequence for the Market Pulse Podcast.",
 stat=("4 weeks", "two-wave sequence, 3 templates"), brand="APMEX", year="2026", role="Guest outreach lead", own="Owned", status="In progress",
 lede="The Market Pulse Podcast needs experts who can argue both the bull and bear case for metals. Booking was feast or famine. I built a pipeline.",
 body=[
  ("The shortlist", "<p>I reviewed past guests against the show's guidelines and filled the gaps: monetary economists and historians, academic researchers on gold, and mint and sovereign program leaders. Every name has a fit rationale, a bull or bear angle, and watch-outs such as conflicts of interest.</p>"),
  ("The sequence", "<ul><li><b>Two waves.</b> Tier 1 gets first contact in week one. Tier 2 opens in week three, so first-wave replies set the pace.</li><li><b>Three templates</b> plus a variant for mint and sovereign program leaders.</li><li><b>Credibility in the ask.</b> Each email states the topic, names the host, offers the questions in advance and includes audience proof.</li><li><b>Target:</b> two to three confirmed recordings.</li></ul>"),
  ("Writing sample: first-touch email", """<blockquote><span class="subj">Subject: Invitation: Market Pulse Podcast conversation on [specific topic]</span><p>Dr. [Last name],</p><p>I'm Keith Rollins, Marketing Communications Lead at APMEX. Our Market Pulse Podcast is hosted by our Head of Media Relations and focuses on balanced, fact-driven conversations about precious metals, with no hype and no sales pitches.</p><p>I'm writing because of your [work / book / recent comments]. We would value your view on [one specific question], including where you see risks as well as opportunities.</p><p>The recording is remote, about 30 to 60 minutes, and we can share the question outline ahead of time. Recent episodes include [episode title and link].</p><p>Would you be open to a conversation? I can send a few times or our booking link.</p></blockquote>"""),
 ],
 results=["A repeatable guest pipeline with clear criteria.", "A paced sequence that protects the show's \"experts, not promoters\" stance.", "Templates any teammate can run."],
 tools="Research, email copywriting"),

# ---------------- CAMPAIGNS
dict(slug="apmex-is-the-spot", group="campaigns", title="APMEX Is the Spot",
 card="A one-week at-spot promotion turned into lasting content. Campaign posts drove nearly two-thirds of the week's link clicks.",
 stat=("~2/3", "of the week's link clicks"), brand="APMEX", year="2026", role="Campaign lead", own="Owned", status="Completed",
 lede="APMEX sold silver dollars at spot price for one week. I built the campaign so the explanation would outlive the offer.",
 body=[
  ("The challenge", "<p>\"At spot\" is a strong offer, but many newer buyers don't know what it means. A one-week promotion also leaves little behind once it ends. Leadership wanted to know whether the campaign moved anything beyond sales.</p>"),
  ("What I built", """<ul><li><b>Evergreen explainer.</b> <a href="https://learn.apmex.com/investing-guide/what-does-at-spot-mean/" target="_blank" rel="noopener">What Does "At Spot" Mean?</a> answers the question plainly and keeps working in search and AI answers.</li><li><b>Short-form video.</b> A 76-word, four-scene vertical script, written to run again with any future at-spot offer.</li><li><b>Press release.</b> <a href="https://www.globenewswire.com/news-release/2026/08/11/3342819/0/en/this-week-only-apmex-offers-silver-dollars-at-spot-through-august-16.html" target="_blank" rel="noopener">This Week Only: APMEX Offers Silver Dollars at Spot</a>, distributed through Notified.</li><li><b>Measurable social.</b> Campaign posts tagged in Sprout Social so the campaign could be measured on its own.</li><li><b>Leadership recap.</b> A deck and companion email covering AI search discoverability, earned media and week-over-week social change.</li></ul>"""),
  ("The honest part", "<p>The campaign made the week bigger, not better per post: at-spot posts had a lower engagement rate than our other content. I said so in the recap and recommended fewer, sharper at-spot posts that borrow the format of our best-performing market update series.</p>"),
 ],
 results=["Campaign posts drove nearly two-thirds of the account's link clicks for the week.", "Total link clicks rose about 25% week over week.", "Net follower growth rose about 33%; impressions and engagements grew by double digits.", "Campaign posts drew roughly half of all tagged-post impressions."],
 tools="Sprout Social, Notified, PowerPoint"),

dict(slug="onegold-card-launch", group="campaigns", title="OneGold Card Launch",
 card="Video scripts, a 12-post launch arc and native ad copy for a new kind of card, in a voice built to stand apart from its parent brand.",
 stat=("12 posts", "sequenced as one launch story"), brand="OneGold", year="2026", role="Copywriter and social strategist", own="Owned", status="Delivered",
 lede="OneGold, an APMEX affiliate, launched a card in a category most people have never heard of. The content had to explain it fast and sound unlike APMEX.",
 body=[
  ("Brand first", "<p>OneGold uses a Magician archetype with a Ruler, Rebel and Sage persona framework. I kept it fully separate from APMEX's composed voice so the two brands never blur.</p>"),
  ("What I delivered", "<ul><li><b>Video in two packages.</b> Spoken-dialogue scripts and a silent-cut set built on visual storytelling and sound design, so the ads work with or without sound.</li><li><b>A 12-post launch arc</b> that builds as a story instead of repeating one announcement.</li><li><b>Native advertising</b> for Kiplinger, written to read as useful editorial for a personal finance audience.</li><li><b>OneGold 2.0 rebrand</b> social launch strategy deck.</li><li><b>Clean tracking.</b> A UTM convention for every launch link.</li></ul>"),
 ],
 results=["A complete launch content system in one consistent voice.", "Scripts that work with and without sound.", "Every launch post traceable in analytics."],
 tools="Brand archetypes, scriptwriting, UTM tracking"),

dict(slug="holiday-season", group="campaigns", title="Holiday Social and Video Season",
 card="Halloween through New Year's: the campaign lineup and a 27-video plan fitted onto the standing posting rhythm.",
 stat=("27 videos", "planned across four phases"), brand="APMEX", year="2026", role="Season owner", own="Owned", status="In production",
 lede="The holiday stretch stacks Black Friday, Cyber Monday, Giving Tuesday and the 12 Days of Deals close together. The plan had to bring holiday energy without breaking a composed brand voice.",
 body=[
  ("The lineup", "<p>Halloween, a run of daily at-spot drops before Black Friday, Black Friday through Cyber Monday, Giving Tuesday and the 12 Days of Deals. A People's Choice poll lets followers pick one of the 12 deals.</p>"),
  ("The video plan", "<ul><li>27 videos from mid-October to December 23, placed on the standing Wednesday and Saturday reel slots.</li><li>Four phases: Warm-up, Holiday Shop, Cyber Week and Countdown.</li><li>Concepts ranked by brand-voice fit. Unboxing videos lead because they are product-first and need no hype.</li><li>One shoot day at the Mint covers three November videos and the sound for a fourth.</li></ul>"),
 ],
 results=["Every slot assigned and every concept tied to the brand voice.", "Production tickets ready for the video team.", "Open questions (KPIs, prize approvals) listed up front."],
 tools="Jira, Sprout Social"),

# ---------------- SOCIAL
dict(slug="stack-value-format", group="social", title="The Stack Value Format",
 card="A simple short-form idea: show a physical stack of metal and what it's worth. The top video reached 420K views.",
 stat=("420K", "views, 440x the channel median"), brand="APMEX", year="2025–2026", role="Strategy and writing", own="Strategy and writing", status="Ongoing",
 lede="Precious metals content tends to be charts and commentary. I developed a format anyone understands in one second: a real stack of metal, and its dollar value.",
 body=[
  ("My role", "<p>I developed the concept and wrote the videos. The APMEX video team produced them.</p>"),
  ("Why it works", "<ul><li><b>Instant comprehension.</b> A stack and a number need no explanation.</li><li><b>Built-in tension.</b> \"What it was worth then, what it's worth now\" creates a reason to watch to the end.</li><li><b>Repeatable.</b> Any product, any price move, any platform.</li></ul>"),
  ("Results by video", """<div class="tablewrap"><table><thead><tr><th>Platform</th><th>Video</th><th>Views</th><th>vs. median</th></tr></thead><tbody>
<tr><td>TikTok</td><td>10 kilo silver bars, stacked</td><td class="num">420.5K</td><td class="num">440x</td></tr>
<tr><td>TikTok</td><td>What $5,000 looks like in silver vs. gold</td><td class="num">239.5K</td><td class="num">250x</td></tr>
<tr><td>Instagram</td><td>A growing silver stack worth almost $30K</td><td class="num">50.9K</td><td class="num">22x</td></tr>
<tr><td>Instagram</td><td>28 Gold Eagles, value one year later</td><td class="num">24.1K</td><td class="num">10x</td></tr>
<tr><td>Instagram</td><td>A $1,000 silver stack, value months later</td><td class="num">23.7K</td><td class="num">10x</td></tr>
</tbody></table></div><p class="note">Medians: TikTok 955 views, Instagram 2.4K views. Public view counts captured October 2026.</p>"""),
 ],
 results=["Top TikTok: 420.5K views, 440x the channel median.", "Second TikTok: 239.5K views, 250x the median.", "Three Instagram reels at 10 to 22x the median.", "The account's most repeatable winning format across two platforms."],
 tools="Concept and scripts; produced by the APMEX video team"),

dict(slug="sprout-social-rollout", group="social", title="Sprout Social Rollout",
 card="Selected and implemented one publishing, listening and reporting platform for the whole company, across 8+ networks.",
 stat=("8+", "platforms connected company-wide"), brand="APMEX and affiliates", year="2023–2026", role="Selected and implemented", own="Owned", status="Ongoing",
 lede="Social ran across many brands, networks and logins. I picked the platform to unify it, set it up and made campaigns measurable inside it.",
 body=[
  ("What I did", "<ul><li><b>Selected Sprout Social</b> and implemented it company-wide.</li><li><b>Connected every network possible:</b> Facebook, Instagram, X, TikTok, LinkedIn, YouTube, Threads and Reddit, with more coming.</li><li><b>Campaign tagging</b> so a campaign like APMEX Is the Spot can be measured apart from the rest of the account.</li><li><b>Listening</b> paired with Brand24 to monitor brand sentiment and catch engagement opportunities.</li><li><b>Live dashboard</b> of social and YouTube numbers through the Sprout API (in progress).</li></ul>"),
 ],
 results=["One platform for publishing, listening and reporting.", "Campaign-level measurement that leadership recaps now rely on.", "A foundation for the group's other brands to join."],
 tools="Sprout Social, Brand24"),

dict(slug="always-on-social", group="social", title="Always-On Social and Content",
 card="The standing programs under every campaign: a fixed weekly cadence, a handle roster for every brand, Reddit reactivation and YouTube support.",
 stat=("190+", "YouTube descriptions written"), brand="APMEX and affiliates", year="2023–2026", role="Social media and content lead", own="Owned", status="Ongoing",
 lede="Campaigns get attention, but most of a brand's presence is the steady work between them. That work needs structure so it doesn't depend on anyone's memory.",
 body=[
  ("The programs", "<ul><li><b>A fixed weekly cadence.</b> Monday market update, Tuesday and Thursday educational articles, Wednesday and Saturday reels, Friday deals, no Sunday post. Every campaign sits on top of this rhythm.</li><li><b>A map of every account.</b> A handle roster for every brand in the group and its partners, organized by management tier.</li><li><b>Community activation.</b> Leading the reactivation of APMEX's dormant Reddit profiles, where the brand is often discussed.</li></ul>"),
  ("YouTube support", "<p>On APMEX's 186K-subscriber channel I manage the publishing schedule and write the SEO description for every video, more than 190 over three years. I've also run thumbnail and title A/B tests.</p>"),
 ],
 results=["A dependable rhythm across brands.", "Clear ownership of every account.", "SEO descriptions on 190+ videos."],
 tools="Sprout Social, Jira, YouTube Studio"),

# ---------------- PR
dict(slug="press-release-program", group="pr", title="Press Release Program",
 card="Releases written and distributed on the wire through Notified, with Keith as media contact.",
 stat=("Notified", "wire distribution I run"), brand="APMEX", year="2026", role="Writer and media contact", own="Owned", status="Ongoing",
 lede="I write APMEX's press releases, distribute them through Notified (GlobeNewswire) and serve as a media contact.",
 body=[
  ("Recent releases", """<div class="tablewrap"><table><thead><tr><th>Date</th><th>Release</th></tr></thead><tbody>
<tr><td class="num">Aug 25, 2026</td><td><a href="https://www.globenewswire.com/news-release/2026/08/25/3350528/0/en/apmex-celebrates-26-years-of-providing-direct-access-to-physical-precious-metals.html" target="_blank" rel="noopener">APMEX Celebrates 26 Years of Providing Direct Access to Physical Precious Metals</a></td></tr>
<tr><td class="num">Aug 11, 2026</td><td><a href="https://www.globenewswire.com/news-release/2026/08/11/3342819/0/en/this-week-only-apmex-offers-silver-dollars-at-spot-through-august-16.html" target="_blank" rel="noopener">This Week Only: APMEX Offers Silver Dollars at Spot Through August 16</a></td></tr>
<tr><td class="num">Jun 2, 2026</td><td><a href="https://www.globenewswire.com/news-release/2026/06/02/3305385/0/en/apmex-employees-raise-55-000-for-regional-food-bank-of-oklahoma-during-annual-fun-week-fundraiser.html" target="_blank" rel="noopener">APMEX Employees Raise $55,000 for Regional Food Bank of Oklahoma</a></td></tr>
</tbody></table></div><p class="note">More releases and pickup numbers coming soon.</p>"""),
  ("How I approach a release", "<ul><li>Lead with the news a reporter can use, not the brand's adjectives.</li><li>Tie promotions to the mission, as the at-spot release did with \"making precious metals accessible to everyone.\"</li><li>Plan wire volume ahead so contract credits get used.</li></ul>"),
 ],
 results=["Releases covering promotions, milestones and community giving.", "Wire distribution and media contact handled end to end."],
 tools="Notified (GlobeNewswire), Qwoted"),

dict(slug="multi-brand-pr", group="pr", title="Multi-Brand PR Expansion",
 card="A plan to take APMEX's working press and media-request program to its sister brands, one brand at a time.",
 stat=("1 brand", "at a time, starting from proof"), brand="Bullion International Group", year="2026", role="Plan owner", own="Owned", status="In progress",
 lede="APMEX built an earned media program on Notified and Qwoted. The group's other North American brands were barely using either.",
 body=[
  ("The plan", "<ul><li><b>Allocation, not equal shares.</b> An annual release allocation weighted toward the flagship, drawn from a shared pool of credits.</li><li><b>Fit before platform.</b> APMEX and OneGold suit expert-source pitching; other brands may only need the wire.</li><li><b>Start with one brand.</b> A pitch presentation showing what APMEX achieved on both platforms, then regroup.</li><li><b>Renew early.</b> Renew the wire contract ahead of its lapse with volume planned in advance.</li></ul>"),
 ],
 results=["A brand-by-brand path to scale earned media.", "A model I plan to reuse for a multi-brand YouTube strategy."],
 tools="Notified, Qwoted"),

dict(slug="expert-contributor-program", group="pr", title="Expert Contributor Program",
 card="A program that brings outside experts into APMEX's Knowledge Center, with rollout documents and outreach scripts.",
 stat=("Launched", "rollout docs and email scripts"), brand="APMEX", year="2026", role="Program lead", own="Owned", status="Ongoing",
 lede="Educational content earns more trust when credible outside voices contribute. I launched a program to bring them in.",
 body=[
  ("What I built", "<ul><li>Internal rollout documents explaining the program, the standards and the process.</li><li>Outreach email scripts to recruit contributors.</li><li>A fit with the Knowledge Center's standards and APMEX's no-hype voice.</li></ul>"),
 ],
 results=["New sources of expert content for the Knowledge Center.", "A repeatable recruiting process."],
 tools="Email copywriting, Jira"),

# ---------------- ADVERTISING
dict(slug="tampa-digital-billboards", group="advertising", title="Tampa Digital Billboard Plan",
 card="A 12-week, three-board holiday plan compared on reach, CPM and audience fit, with a cheaper fallback built in.",
 stat=("3/4", "of impressions for 60% of cost in the fallback"), brand="APMEX", year="2026", role="Strategist and author", own="Owned", status="Proposal",
 lede="APMEX had a fixed three-month budget to test digital out-of-home. Leadership needed to know where to spend it and how results would be measured.",
 body=[
  ("Groundwork", "<p>An executive research deck on digital out-of-home: market selection, buying models, vendors, tracking and KPIs, format and location.</p>"),
  ("The recommendation", "<ul><li>Three digital bulletins in Tampa for a 12-week flight, early November through late January.</li><li>An interstate board as the anchor: more than half of total impressions at the lowest CPM.</li><li>A second board with the strongest audience match by a wide margin.</li><li>A third board extending reach, flagged honestly as about twice the cost per impression.</li></ul>"),
  ("Built for a fast decision", "<p>If budget tightened, the first two boards alone keep roughly three-quarters of the impressions for about 60% of the cost. All three include attribution so results go beyond impressions.</p>"),
 ],
 results=["A plan leadership can approve or trim in one meeting.", "A ready-made lower-cost option.", "Measurement built in before booking."],
 tools="Media planning, CPM analysis, vendor evaluation"),

dict(slug="coinage-print-ad", group="advertising", title="Coinage Magazine Print Ad",
 card="A full-page ad for serious collectors that leads with credentials they already trust.",
 stat=("Full page", "in Coinage magazine"), brand="APMEX", year="2026", role="Concept and copy lead", own="Owned", status="Delivered",
 lede="Coin hobby print readers are knowledgeable and hard to impress. A generic \"shop with us\" ad would be ignored.",
 body=[
  ("Research first", "<p>I researched print placements for two audiences, precious metals investors and pop-culture coin buyers, to learn what each responds to and which titles reach them.</p>"),
  ("Proof, not claims", "<p>The ad centers on two facts collectors care about: APMEX is a U.S. Mint authorized purchaser, and its graded inventory is certified by PCGS, NGC and CAC. Composed and specific, with no superlatives.</p>"),
 ],
 results=["A full-page ad built on trust signals the audience respects.", "Placement research covering two collector audiences."],
 tools="Audience research, print copywriting"),

# ---------------- STRATEGY
dict(slug="value-positioning", group="strategy", title="Value Positioning Framework",
 card="Four pillars that answer cost concerns with value, mapped to every channel so every writer makes the same case.",
 stat=("4 pillars", "mapped across every channel"), brand="APMEX", year="2026", role="Framework lead", own="Owned", status="In progress",
 lede="Customers raised cost concerns online. Leadership asked the team to answer them with value. Several people write promotions, emails, releases and ads, and each handled it differently.",
 body=[
  ("The four pillars", "<ol><li><b>Deep value during events.</b> Real savings, with the at-spot campaign as the model.</li><li><b>Assortment breadth.</b> A product for every budget.</li><li><b>Free tools.</b> Value-adds stated explicitly.</li><li><b>Club benefits.</b> Membership value shown plainly.</li></ol>"),
  ("Channel map", "<p>Discount depth and range for promotions and ads. A standing value-add line for email. Assortment and tools framed as customer value in press releases. Every new line is checked against APMEX voice standards so value never turns into hype or defensiveness.</p>"),
 ],
 results=["One shared language for cost concerns.", "A standing value line built into email.", "Guardrails that keep value messaging on-voice."],
 tools="Positioning, messaging architecture"),

dict(slug="brand-voice-system", group="strategy", title="Two Brands, Two Voices",
 card="Voice standards for APMEX and OneGold, applied across every format from captions to review responses.",
 stat=("2 brands", "kept distinct across every format"), brand="APMEX and OneGold", year="2023–2026", role="Brand voice steward", own="Owned", status="Ongoing",
 lede="APMEX has to sound like a steady authority. OneGold has to feel new and inventive. With many writers and formats, both voices drift unless someone holds the line.",
 body=[
  ("APMEX: the Ruler", "<ul><li>No exclamation points and no superlatives.</li><li>No predictions about market direction.</li><li>No defensive framing; state the facts.</li><li>A defined list of banned words and phrases.</li></ul>"),
  ("OneGold: the Magician", "<p>Inventive and forward-looking, supported by a Ruler, Rebel and Sage persona framework. The two frameworks stay fully separate.</p>"),
  ("In practice", "<p>Weekly market update captions compare spot prices with the prior Monday's close and never forecast. Trustpilot review responses stay calm and specific. Holiday video concepts were ranked partly on voice fit.</p>"),
 ],
 results=["Two recognizable brands that stay distinct.", "Standards concrete enough for any writer to apply."],
 tools="Brand archetypes, editorial standards"),

dict(slug="leadership-reporting", group="strategy", title="Leadership Reporting",
 card="The monthly Brand Marketing Report and fiscal-year results across earned media, press and content.",
 stat=("Monthly", "leadership report I own"), brand="APMEX", year="2026", role="Report author", own="Owned", status="Ongoing",
 lede="Leadership needs to see what marketing did, in a format they can read in minutes.",
 body=[
  ("What I produce", "<ul><li><b>Monthly Brand Marketing Report.</b> One idea per slide, with caveats in an appendix rather than the headline.</li><li><b>Fiscal-year report</b> covering earned media, press release performance and Knowledge Center metrics.</li><li><b>Campaign recaps</b> that name what didn't work as clearly as what did.</li></ul>"),
  ("Sources", "<p>GA4, Google Search Console, Botify, Brand24, Sprout Social and monthly dashboards.</p>"),
 ],
 results=["A standing, trusted view of marketing performance.", "Recaps leadership can act on."],
 tools="GA4, Search Console, Botify, Brand24, Sprout Social, PowerPoint"),

# ---------------- WRITING
dict(slug="apmex-knowledge-center", group="writing", title="APMEX Knowledge Center",
 card="63 bylined articles on investing, history and selling, including a 12-part How to Sell series.",
 stat=("63", "bylined articles"), brand="APMEX", year="2023–2026", role="Writer", own="Owned", status="Ongoing",
 lede="APMEX's Knowledge Center teaches buyers and collectors. My articles turn monetary history and macroeconomics into plain English, then point readers to their next step.",
 body=[
  ("What I've written", """<div class="tablewrap"><table><thead><tr><th>Type</th><th>Count</th><th>Examples</th></tr></thead><tbody>
<tr><td>Conversion and onboarding</td><td class="num">~5</td><td>You Bought Your First Gold Bar, Now What?; Platinum Bars vs. Gold Bars</td></tr>
<tr><td>How to Sell series</td><td class="num">12</td><td>How to Sell American Eagle Gold Coins; Junk Silver; Maple Leafs</td></tr>
<tr><td>Macro and investing</td><td class="num">~12</td><td>Debt Monetization and Gold; Quantitative Easing; Black Swan Events</td></tr>
<tr><td>Practical how-tos</td><td class="num">~8</td><td>Specific Gravity Purity Tests; What Half Dollars Are Silver?</td></tr>
<tr><td>History and education</td><td class="num">~25</td><td>The London Gold Pool Collapse; Top 22 Famous Coin Hoards</td></tr>
</tbody></table></div>"""),
  ("Featured: You Bought Your First Gold Bar, Now What?", """<p>Written in 2024 for first-time buyers coming from big-box retail. It works like a post-purchase onboarding sequence in article form: storage, tracking value, buying more and selling. It routes readers into account creation, the portfolio tracker, the app, storage, AutoInvest and the newsletter. <a href="https://learn.apmex.com/investing-guide/gold/you-bought-your-first-gold-bar-now-what/" target="_blank" rel="noopener">Read it</a>.</p>"""),
 ],
 results=["63 articles under my byline.", "A 12-part series supporting the buyback program.", "Every article written to teach, rank and lead to a next step."],
 tools="SEO writing, WordPress",
 links=[("See every article on my APMEX author page", "https://learn.apmex.com/author/keith-rollins/")]),

dict(slug="fixd-best-worst-years", group="writing", title="FIXD Best & Worst Years Guides",
 card="20 data-driven car buying guides for FIXD, with reliability charts, owner surveys and product calls to action.",
 stat=("20", "car buying guides"), brand="FIXD", year="2023", role="Freelance writer", own="Owned", status="Published",
 lede="As a freelancer I wrote FIXD's Best & Worst Years guides: long-form, data-heavy articles that help shoppers pick a used car and introduce them to the FIXD sensor.",
 body=[
  ("What's in each guide", "<ul><li>A summary table of the best and worst model years.</li><li>Charts on reliability, safety ratings, fuel economy and value versus repair cost.</li><li>Year-by-year reviews covering common trouble codes and recalls.</li><li>Q&amp;A on engines, transmissions and high mileage.</li><li>Calls to action for the FIXD sensor and related guides.</li></ul><p>My decade in auto repair is why these read like advice from a mechanic.</p>"),
  ("The guides", "FIXD_TABLE"),
 ],
 results=["20 published guides under my byline.", "Technical automotive data made easy to act on.", "Conversion built into long-form editorial."],
 tools="SEO writing, data interpretation"),

# ---------------- AI
dict(slug="marketing-ops-tools", group="ai", title="Marketing Operations Tools",
 card="A daily start page, a live communications calendar and a social listening digest, built with Claude.",
 stat=("3 tools", "built with AI, used daily"), brand="APMEX", year="2026", role="Designer and builder", own="Owned", status="In use",
 lede="A marketing communications role runs on information spread across a dozen places. I built tools that bring it to me each morning.",
 body=[
  ("What I built", "<ul><li><b>Home Base.</b> A start page refreshed every weekday morning with listening highlights, social and YouTube numbers, a to-do list and priority emails sorted by urgency.</li><li><b>Communications Calendar.</b> A page that reads live from the team spreadsheet and leads with this week and next.</li><li><b>Social listening digest.</b> A daily email of Brand24 highlights, with deeper dives into community threads about our brands, pricing and service (in setup).</li><li><b>Live social dashboard</b> through the Sprout Social API (in progress).</li></ul>"),
  ("AI Fluency", "<p>I built these with Claude as a working partner, and I've completed Anthropic Academy coursework including Claude 101. The skill isn't typing prompts; it's knowing what to delegate, describing it clearly and checking the result.</p>"),
 ],
 results=["Less time gathering, more time doing.", "Nothing from the inbox gets lost.", "The team calendar visible without another meeting."],
 tools="Claude, Brand24, Sprout Social API, spreadsheets"),
]

FIXD = ["audi-a4","buick-enclave","buick-lesabre","cadillac-cts","cadillac-deville","cadillac-srx","chevrolet-avalanche","chevrolet-cobalt","chevrolet-trailblazer","ford-fiesta","ford-fusion","gmc-envoy","lexus-rx300","nissan-altima","nissan-maxima","nissan-pathfinder","nissan-sentra","nissan-titan","pontiac-g6","toyota-corolla"]

FEATURED = ["apmex-is-the-spot", "partner-email-review", "stack-value-format"]
