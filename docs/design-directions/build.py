"""Builds the two design-direction mockups (A and B) for the 4 marketing pages.

Run:  python3 docs/design-directions/build.py
Output: docs/design-directions/{a,b}/{index,services,about,contact}.html
Copy follows the advisor-support rewrite (PR #1). Plain static HTML, no build needed to view.
"""
from pathlib import Path

ROOT = Path(__file__).parent
CTA = "Start intake &amp; book a meeting"
COMPLIANCE = ("Ravi is not a registered investment adviser and does not provide investment advice "
              "to the public. All services support the advisor&rsquo;s own firm.")
PAGES = [("index", "Home"), ("services", "Services"), ("about", "About"), ("contact", "Contact")]
TITLES = {"index": "Ravi Yeleswarapu | Back-office support for advisors", "services": "Services | Ravi Yeleswarapu",
          "about": "About | Ravi Yeleswarapu", "contact": "Start intake | Ravi Yeleswarapu"}

# ---------------------------------------------------------------- shared copy
HOURS = [
    ("Plan prep", "Who builds the plan before the meeting?",
     "Statements, account details and questionnaires arrive in pieces. Someone has to organize them and get them into your planning software before you can do the real work."),
    ("Business-owner clients", "Are your owner clients ready to talk about an exit?",
     "Most owners haven&rsquo;t pulled together what an exit conversation needs. Preparing that groundwork takes time you could spend advising."),
    ("Your own books", "When were the firm&rsquo;s books last reconciled?",
     "Fee revenue, expenses and bank accounts drift out of sync while you&rsquo;re busy with clients. Then tax season arrives."),
]
STEPS = [
    ("Pick from the menu", "Choose any services from any stage. Nothing is a package."),
    ("Fill a short intake", "A few questions about your firm and tools. No client information."),
    ("Book a meeting", "Thirty minutes to agree scope, data access, timeline and price."),
    ("You review and sign off", "Everything comes back to you. Nothing reaches a client without your approval."),
]
BACKGROUND = [
    ("Financial planning", "B.S., Financial Counseling &amp; Planning, Purdue"),
    ("Regulation &amp; risk", "Consulting at Capgemini &amp; Capco"),
    ("Data &amp; reporting", "BMO and NXT Capital"),
    ("Business owners", "Certified Exit Planning Advisor (CEPA)"),
]
TIMELINE = [
    ("2013&ndash;2017", "Capgemini &amp; Capco", "Consulting in banking regulation, financial risk and compliance."),
    ("2017&ndash;2021", "BMO", "Analytics and reporting. Automating executive reports and the manual effort behind them."),
    ("2021&ndash;2022", "Epsilon", "Product management for measurement and reporting."),
    ("2022&ndash;2024", "BMO, again", "Product ownership across data and technology, aligning architects, engineers and the business."),
    ("2024&ndash;2025", "NXT Capital", "Data and reporting. Helped cut a monthly reporting process from five days to one."),
    ("Now", "Back-office support for advisors", "Paraplanning and bookkeeping for independent advisors. It puts my planning degree and compliance habits to use."),
]
OUTSIDE = [("Reading", "Wodehouse, Tolkien, the Stormlight Archive. Pratchett above all."),
           ("Music", "Guitar and bansuri. Still learning both."),
           ("Games", "Chess regularly; Go, rather less competently."),
           ("Languages", "English, Hindi, Telugu, and very rough Japanese.")]
SUPERVISION = ("I work as a contractor for your firm, under your direction. You remain responsible for all advice and "
               "client communication, and nothing I prepare goes to a client without your review. I follow your firm&rsquo;s "
               "data-security policies and sign your confidentiality agreement. I don&rsquo;t prepare tax returns, perform "
               "audits, give legal advice, produce formal valuations, or broker business sales.")

INTAKE_FORM = """
<form novalidate>
  <p class="mock-note mock-top">Mockup. The fields below are filled with example answers so you can click straight through.</p>
  <fieldset class="f-chips"><legend>Services you picked</legend><div data-chips></div></fieldset>
  <div class="f-row">
    <p class="f"><label for="fname">Your name</label><input id="fname" name="fname" autocomplete="name" required value="Jordan Ellis"></p>
    <p class="f"><label for="femail">Work email</label><input id="femail" name="femail" type="email" autocomplete="email" required value="jordan@ellisplanning.example"></p>
  </div>
  <div class="f-row">
    <p class="f"><label for="ffirm">Firm name</label><input id="ffirm" name="ffirm" autocomplete="organization" value="Ellis Planning Group"></p>
    <p class="f"><label for="ftype">Your firm is</label><select id="ftype" name="ftype"><option>A solo RIA</option><option selected>A small RIA (2&ndash;10 people)</option><option>An ensemble practice</option><option>Something else</option></select></p>
  </div>
  <p class="f"><label for="ftools">Planning and accounting software you use <span class="opt">optional</span></label><input id="ftools" name="ftools" placeholder="Your planning software, CRM, accounting software"></p>
  <p class="f"><label for="fneed">What&rsquo;s piling up?</label><textarea id="fneed" name="fneed" rows="4" required>About 12 annual reviews in Q1 and the data entry is behind. Books are two months out of date.</textarea>
    <span class="f-note">Please don&rsquo;t include client names, account numbers or statements. We&rsquo;ll agree on a secure way to share data first.</span></p>
  <p class="f"><label for="fwhen">When would you like help to start?</label><select id="fwhen" name="fwhen"><option>Within two weeks</option><option selected>This month</option><option>Next quarter</option><option>Just exploring</option></select></p>
  <div class="f-actions"><button class="btn btn-primary" type="submit">Continue to scheduling</button><span class="f-step">Step 1 of 2</span></div>
</form>"""

SCHEDULER = """
<p class="sched-lead">Thanks, <span data-who>there</span>. Pick a time for a 30-minute call.</p>
<div class="sched">
  <div><p class="sched-label">Day</p><div class="days" data-days></div></div>
  <div><p class="sched-label">Time (Pacific)</p><div class="times" data-times></div></div>
</div>
<p class="mock-note">Mockup. In the live site this step would show a real scheduling tool. These times are placeholders.</p>
<div class="f-actions"><button class="btn btn-primary" type="button" data-confirm disabled>Confirm meeting</button><button class="btn btn-quiet" type="button" data-back>Back to intake</button><span class="f-step">Step 2 of 2</span></div>"""

DONE = """<p>You&rsquo;re booked for <strong data-when></strong>. I&rsquo;ll read your intake before we talk and come with questions, not a pitch.</p>
<p class="mock-note">Mockup. No email has been sent and no meeting has been created.</p>"""


def head(d, page):
    fonts = {
        "a": "family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500",
        "b": "family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..600,100;1,9..144,300..600,100&family=Manrope:wght@400;500;600;700",
    }[d]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<title>{TITLES[page]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="./style.css">
<script src="../shared/menu.js" defer></script>
</head>
<body class="p-{page}">
<a class="skip" href="#main">Skip to content</a>
"""


def nav(page, cls=""):
    out = []
    for slug, name in PAGES:
        if slug == "contact":
            continue
        cur = ' aria-current="page"' if slug == page else ""
        out.append(f'<a href="./{slug}.html"{cur}>{name}</a>')
    return "".join(out)


# ================================================================ DIRECTION A
def a_header(page):
    return f"""<header class="masthead"><div class="wrap mast">
<a class="brand" href="./index.html"><span class="brand-name">Ravi Yeleswarapu</span><span class="brand-sub">Back office for advisors</span></a>
<nav class="nav" aria-label="Primary">{nav(page)}<a href="./contact.html" class="nav-contact"{' aria-current="page"' if page == 'contact' else ''}>Contact</a></nav>
<a class="btn btn-primary btn-sm" data-cta="./contact.html" href="./contact.html">{CTA}</a>
</div></header>
<main id="main">
"""


def a_footer():
    return f"""</main>
<footer class="foot"><div class="wrap">
<div class="foot-top">
  <p class="foot-big">Paraplanning, owner-client prep and bookkeeping, done for the advisor.</p>
  <a class="btn btn-primary" data-cta="./contact.html" href="./contact.html">{CTA}</a>
</div>
<div class="foot-grid">
  <p class="foot-legal"><span class="label">Compliance</span>{COMPLIANCE}</p>
  <nav class="foot-nav" aria-label="Footer"><a href="./index.html">Home</a><a href="./services.html">Services</a><a href="./about.html">About</a><a href="./contact.html">Contact</a><a href="https://www.linkedin.com/in/ryeleswa">LinkedIn</a></nav>
  <p class="foot-meta">&copy; <span data-year>2026</span> Ravi Yeleswarapu<br>Vancouver, WA &middot; working remotely<br>No analytics or ad trackers.</p>
</div>
</div></footer>
</body>
</html>
"""


def a_home():
    hours = "".join(f"""<article class="hour"><p class="label">{k}</p><h3>{q}</h3><p>{t}</p></article>""" for k, q, t in HOURS)
    steps = "".join(f"""<li><span class="step-n">{i:02d}</span><h3>{h}</h3><p>{t}</p></li>""" for i, (h, t) in enumerate(STEPS, 1))
    bg = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in BACKGROUND)
    return f"""
<section class="hero"><div class="wrap hero-grid">
  <p class="label hero-label">For independent advisors and small RIAs</p>
  <h1>More time with clients.<br><em>Less time on prep and&nbsp;books.</em></h1>
  <div class="hero-side">
    <p class="lead">I handle the preparation around your client meetings and the bookkeeping behind your practice. You review everything, and the advice stays&nbsp;yours.</p>
    <div class="actions"><a class="btn btn-primary" data-cta="./contact.html" href="./contact.html">{CTA}</a><a class="btn btn-line" href="./services.html">Browse the service menu</a></div>
  </div>
</div>
<div class="wrap"><ul class="ticker" aria-label="Who this is for"><li>Solo advisors</li><li>Small RIAs &amp; ensembles</li><li>Advisors with business-owner clients</li></ul></div>
</section>

<section class="sec"><div class="wrap two">
  <div class="rail"><p class="label">Where the hours go</p></div>
  <div><h2 class="h2">Work that has to get done, but doesn&rsquo;t need to be done by&nbsp;you.</h2>
  <div class="hours">{hours}</div></div>
</div></section>

<section class="sec sec-ink"><div class="wrap two">
  <div class="rail"><p class="label">How it works</p></div>
  <div><h2 class="h2">You stay the advisor. I do the&nbsp;preparation.</h2><ol class="steps">{steps}</ol></div>
</div></section>

<section class="sec"><div class="wrap two">
  <div class="rail"><p class="label">Background</p></div>
  <div class="why">
    <h2 class="h2">I started in regulatory compliance. I&rsquo;m comfortable working inside the&nbsp;rules.</h2>
    <div class="why-cols">
      <p>My degree is in financial counseling and planning. I spent my first years consulting on banking regulation and risk, then most of a decade in data and reporting. At NXT Capital I helped cut a monthly reporting process from five days to one.</p>
      <p>Paraplanning as an outside service is new for me, and I&rsquo;d rather say that plainly. Start with one client file or one month of books, and judge the quality before giving me&nbsp;more.</p>
    </div>
    <dl class="creds">{bg}</dl>
    <p class="fine">Results named above are from previous employment, not client results for this practice.</p>
  </div>
</div></section>
"""


def a_services():
    return f"""
<section class="page-head"><div class="wrap two">
  <div class="rail"><p class="label">Services</p></div>
  <div><h1 class="h1">An &agrave; la carte menu, in three&nbsp;stages.</h1>
  <p class="lead">Pick any items from any stage. Your picks carry into the intake, and we agree scope and price on a call before any work starts.</p></div>
</div></section>
<section class="menu-wrap"><div class="wrap">
  <div data-menu="columns" class="menu"></div>
</div></section>
<div class="tray" data-tray><div class="wrap tray-in">
  <p><span class="tray-dot" aria-hidden="true"></span><span data-count-label>Nothing selected yet</span></p>
  <a class="btn btn-primary" data-cta="./contact.html" href="./contact.html">{CTA}</a>
</div></div>
<section class="sec"><div class="wrap two">
  <div class="rail"><p class="label">How the work is supervised</p></div>
  <div class="supervise"><p>{SUPERVISION}</p><p class="compliance-box">{COMPLIANCE}</p></div>
</div></section>
"""


def a_about():
    tl = "".join(f"<li><span class='tl-year'>{y}</span><h3>{h}</h3><p>{t}</p></li>" for y, h, t in TIMELINE)
    out = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in OUTSIDE)
    return f"""
<section class="page-head"><div class="wrap two">
  <div class="rail"><p class="label">About</p></div>
  <div><h1 class="h1">Hi, I&rsquo;m Ravi.</h1>
  <div class="why-cols">
    <p class="lead">I started in regulatory compliance and financial risk, moved into data and technology, and stayed because the problems kept changing.</p>
    <p>Much of my work has been getting people with different priorities to agree: business teams, engineers, risk and executives. I&rsquo;m not always the deepest specialist in the room. I&rsquo;m comfortable finding out what I need to know.</p>
  </div></div>
</div></section>
<section class="sec sec-rule"><div class="wrap two">
  <div class="rail"><p class="label">The work, in order</p></div>
  <ol class="timeline">{tl}</ol>
</div></section>
<section class="sec"><div class="wrap two">
  <div class="rail"><p class="label">Outside work</p></div>
  <dl class="creds creds-4">{out}</dl>
</div></section>
"""


def a_contact():
    return f"""
<section class="page-head"><div class="wrap two">
  <div class="rail"><p class="label">Contact</p></div>
  <div><h1 class="h1">Start intake, then book a&nbsp;meeting.</h1>
  <p class="lead">Two short steps. Tell me about your firm and what you&rsquo;d hand off, then pick a time to talk.</p></div>
</div></section>
<section class="sec sec-tight"><div class="wrap two">
  <div class="rail"><ol class="progress" data-progress><li class="is-current"><span>01</span> Intake</li><li><span>02</span> Schedule</li><li><span>03</span> Done</li></ol></div>
  <div class="intake" data-intake data-services-href="./services.html">
    <div data-step="1"><h2 class="h3">Intake</h2>{INTAKE_FORM}</div>
    <div data-step="2" hidden><h2 class="h3">Schedule</h2>{SCHEDULER}</div>
    <div data-step="done" hidden><h2 class="h3">See you then.</h2>{DONE}</div>
    <aside class="alt"><p class="label">Rather send an email?</p><p><span class="mono">info@raviyeleswarapu.org</span>. A few sentences about the problem are enough.</p></aside>
  </div>
</div></section>
"""


# ================================================================ DIRECTION B
def b_header(page):
    return f"""<header class="top"><div class="wrap top-in">
<a class="brand" href="./index.html"><span class="mono-mark" aria-hidden="true">RY</span><span class="brand-text"><strong>Ravi Yeleswarapu</strong><small>Back-office support for advisors</small></span></a>
<nav class="nav" aria-label="Primary">{nav(page)}<a href="./contact.html"{' aria-current="page"' if page == 'contact' else ''}>Contact</a></nav>
<a class="btn btn-primary btn-sm" data-cta="./contact.html" href="./contact.html">{CTA}</a>
</div></header>
<main id="main">
"""


def b_footer():
    return f"""</main>
<footer class="foot"><div class="wrap">
<div class="foot-card">
  <div><h2 class="h2">Let&rsquo;s see what you&rsquo;d hand off first.</h2><p>Two short steps: a quick intake, then a 30-minute call.</p></div>
  <a class="btn btn-primary" data-cta="./contact.html" href="./contact.html">{CTA}</a>
</div>
<div class="foot-row">
  <p class="foot-legal">{COMPLIANCE}</p>
  <nav class="foot-nav" aria-label="Footer"><a href="./index.html">Home</a><a href="./services.html">Services</a><a href="./about.html">About</a><a href="./contact.html">Contact</a><a href="https://www.linkedin.com/in/ryeleswa">LinkedIn</a></nav>
</div>
<p class="foot-meta">&copy; <span data-year>2026</span> Ravi Yeleswarapu &middot; Vancouver, WA &middot; No analytics or ad trackers.</p>
</div></footer>
</body>
</html>
"""


def b_home():
    hours = "".join(f"""<article class="card"><p class="kicker">{k}</p><h3>{q}</h3><p>{t}</p></article>""" for k, q, t in HOURS)
    steps = "".join(f"""<li class="card step"><span class="step-n">{i}</span><h3>{h}</h3><p>{t}</p></li>""" for i, (h, t) in enumerate(STEPS, 1))
    bg = "".join(f"<li><strong>{k}</strong><span>{v}</span></li>" for k, v in BACKGROUND)
    stages = "".join(f"""<li><span class="pill-n">{n}</span><strong>{name}</strong><span>{line}</span></li>""" for n, name, line in
                     [("1", "Diagnostic", "Understand the situation"), ("2", "Prescription", "Prepare the plan materials"), ("3", "Operation", "Ongoing books and upkeep")])
    return f"""
<section class="hero"><div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="kicker kicker-gold">For independent advisors and small RIAs</p>
    <h1>A steady pair of hands <em>behind your practice.</em></h1>
    <p class="lead">Paraplanning, preparation for business-owner clients, and bookkeeping for your firm. I work quietly under your direction. You review everything, and the advice stays yours.</p>
    <div class="actions"><a class="btn btn-primary" data-cta="./contact.html" href="./contact.html">{CTA}</a><a class="btn btn-ghost" href="./services.html">See the menu</a></div>
  </div>
  <aside class="hero-card" aria-label="How services are organized">
    <p class="kicker">The menu, in three stages</p>
    <ol class="stage-list">{stages}</ol>
    <a class="link-gold" href="./services.html">Pick what you need &rarr;</a>
  </aside>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><p class="kicker kicker-gold">Where the hours go</p><h2 class="h2">Work that has to get done, but doesn&rsquo;t need to be done by you.</h2></div>
  <div class="grid3">{hours}</div>
</div></section>

<section class="sec sec-cream"><div class="wrap">
  <div class="sec-head"><p class="kicker">How it works</p><h2 class="h2">You stay the advisor. I do the preparation.</h2></div>
  <ol class="grid4">{steps}</ol>
</div></section>

<section class="sec"><div class="wrap split">
  <div><p class="kicker kicker-gold">Why me</p><h2 class="h2">Planning training, compliance habits, and a lot of reporting.</h2>
  <p>I started in regulatory compliance, then spent most of a decade in data and reporting. At NXT Capital I helped cut a monthly reporting process from five days to one.</p>
  <p>Paraplanning as an outside service is new for me, and I&rsquo;d rather say that plainly. Start small, with one client file or one month of books, and judge the work for yourself.</p>
  <p class="fine">Results named here are from previous employment, not client results for this practice.</p></div>
  <ul class="cred-card card">{bg}</ul>
</div></section>
"""


def b_services():
    return f"""
<section class="page-head"><div class="wrap narrow">
  <p class="kicker kicker-gold">Services</p>
  <h1 class="h1">Choose what you need. <em>Skip what you don&rsquo;t.</em></h1>
  <p class="lead">Every service sits in one of three stages. Pick from any of them; your choices carry into the intake, and we settle scope and price together on a call.</p>
</div></section>
<section class="menu-wrap"><div class="wrap">
  <div data-menu="tabs" class="menu"></div>
  <p class="compliance-note"><span class="dot" aria-hidden="true"></span>{COMPLIANCE}</p>
</div></section>
<div class="tray" data-tray><div class="tray-in">
  <span class="tray-count" data-count>0</span><span class="tray-label" data-count-label>Nothing selected yet</span>
  <a class="btn btn-primary btn-sm" data-cta="./contact.html" href="./contact.html">{CTA}</a>
</div></div>
<section class="sec sec-cream"><div class="wrap narrow">
  <p class="kicker">How the work is supervised</p>
  <p class="big-p">{SUPERVISION}</p>
</div></section>
"""


def b_about():
    tl = "".join(f"<li><span class='tl-year'>{y}</span><div><h3>{h}</h3><p>{t}</p></div></li>" for y, h, t in TIMELINE)
    out = "".join(f"<li class='card'><p class='kicker'>{k}</p><p>{v}</p></li>" for k, v in OUTSIDE)
    return f"""
<section class="page-head"><div class="wrap narrow">
  <p class="kicker kicker-gold">About</p>
  <h1 class="h1">Hi, I&rsquo;m Ravi.</h1>
  <p class="lead">I started in regulatory compliance and financial risk, moved into data and technology, and stayed because the problems kept changing.</p>
  <p>Much of my work has been getting people with different priorities to agree: business teams, engineers, risk and executives. I&rsquo;m not always the deepest specialist in the room. I&rsquo;m comfortable finding out what I need to know.</p>
</div></section>
<section class="sec sec-cream"><div class="wrap narrow">
  <p class="kicker">The work, in order</p>
  <ol class="timeline">{tl}</ol>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><p class="kicker kicker-gold">Outside work</p><h2 class="h2">A few other things.</h2></div>
  <ul class="grid4">{out}</ul>
</div></section>
"""


def b_contact():
    return f"""
<section class="page-head"><div class="wrap narrow">
  <p class="kicker kicker-gold">Contact</p>
  <h1 class="h1">Start intake, <em>then book a meeting.</em></h1>
  <p class="lead">Tell me about your firm and what you&rsquo;d hand off, then pick a time for a 30-minute call.</p>
</div></section>
<section class="sec sec-tight"><div class="wrap narrow">
  <div class="intake card" data-intake data-services-href="./services.html">
    <ol class="progress" data-progress><li class="is-current"><span>1</span>Intake</li><li><span>2</span>Schedule</li><li><span>3</span>Done</li></ol>
    <div data-step="1"><h2 class="h3">Tell me about your firm</h2>{INTAKE_FORM}</div>
    <div data-step="2" hidden><h2 class="h3">Pick a time</h2>{SCHEDULER}</div>
    <div data-step="done" hidden><h2 class="h3">See you then.</h2>{DONE}</div>
  </div>
  <p class="alt">Rather send an email? <span class="mono">info@raviyeleswarapu.org</span></p>
</div></section>
"""


DIRS = {
    "a": (a_header, a_footer, {"index": a_home, "services": a_services, "about": a_about, "contact": a_contact}),
    "b": (b_header, b_footer, {"index": b_home, "services": b_services, "about": b_about, "contact": b_contact}),
}

for d, (hdr, ftr, bodies) in DIRS.items():
    for slug, fn in bodies.items():
        (ROOT / d / f"{slug}.html").write_text(head(d, slug) + hdr(slug) + fn() + ftr(), encoding="utf-8")
print("built", sum(len(b[2]) for b in DIRS.values()), "pages")
