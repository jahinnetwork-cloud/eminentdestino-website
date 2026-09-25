import json, os, shutil, zipfile, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = ROOT

SERVICES = json.load(open(f"{SRC}/services.json", encoding="utf-8"))
MCN_COPY = json.load(open(f"{SRC}/mcn-copy.json", encoding="utf-8"))
CSS = open(f"{SRC}/style.css", encoding="utf-8").read()
CSS += """
ol{margin:0;padding:0;list-style:none}
.sp-hero::after{background:var(--orange-tint)}
.sec--tint .forbox{background:#fff}
.sec--tint .form{background:#fff}
.sec--line{border-top:1px solid var(--line)}
"""
JS = open(f"{SRC}/site.js", encoding="utf-8").read().replace(
    "/*__SERVICES__*/[]", json.dumps(SERVICES, ensure_ascii=False)).replace(
    "/*__MCN_COPY__*/{}", json.dumps(MCN_COPY["my"], ensure_ascii=False))

ICONS = {
 "youtube-mcn": '<rect x="3" y="5" width="18" height="14" rx="4"/><path d="M10 9.5v5l4.5-2.5z"/>',
 "music-distribution": '<path d="M9 18V6l10-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="16.5" cy="16" r="2.5"/>',
 "music-publishing": '<path d="M5 4h10a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
 "vevo": '<rect x="3" y="6" width="13" height="12" rx="3"/><path d="M16 10l5-3v10l-5-3"/>',
 "facebook": '<path d="M4 11v2a1 1 0 0 0 1 1h2l5 4V6L7 10H5a1 1 0 0 0-1 1z"/><path d="M16 9a4 4 0 0 1 0 6"/>',
 "white-label": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "api": '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>',
 "copyright": '<path d="M12 3l8 3v6c0 4.5-3.2 7.8-8 9-4.8-1.2-8-4.5-8-9V6z"/><path d="M14.8 9.6a3.3 3.3 0 1 0 0 4.8"/>',
 "video-production": '<rect x="3" y="9" width="18" height="11" rx="2"/><path d="M3 9l3-5h4L7 9M10 9l3-5h4l-3 5M17 9l3-5"/>',
}
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def svg(inner): return f'<svg viewBox="0 0 24 24" aria-hidden="true">{inner}</svg>'
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;")
SVC = {s["id"]: s for s in SERVICES}

# ---------------------------------------------------------------- shared blocks
def header(home):
    idx = "" if home else "../index.html"
    brand = "#top" if home else "../index.html"
    nav = f'''
        <a href="{idx}#services" data-i18n="nav.services">Services</a>
        <a href="{idx}#mcn" data-i18n="nav.mcn">YouTube MCN</a>
        <a href="{idx}#partners" data-i18n="nav.partners">Partners &amp; API</a>
        <a href="#contact" data-i18n="nav.contact">Contact</a>'''
    return f'''
<header class="hdr">
  <div class="wrap">
    <div class="hdr__bar">
      <a class="logo" href="{brand}" aria-label="Eminent Destino">
        <img class="logo__img" alt="Eminent Destino" referrerpolicy="no-referrer" decoding="async">
        <span class="logo__fb"><b>EDO</b><em>Eminent Destino</em></span>
      </a>
      <nav class="nav" aria-label="Main">{nav}
      </nav>
      <div class="hdr__end">
        <div class="lang" role="group" aria-label="Language">
          <button type="button" data-lang="en" aria-pressed="true">EN</button>
          <button type="button" data-lang="my" aria-pressed="false" lang="my">မြန်မာ</button>
        </div>
        <a class="btn btn--sm" href="#contact"><span data-i18n="cta.work">Work with EDO</span>{ARROW}</a>
        <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="mmenu"><span></span><span></span><span></span></button>
      </div>
    </div>
    <div class="mmenu" id="mmenu">{nav}
    </div>
  </div>
</header>'''

def footer(home):
    pre = "services/" if home else ""
    idx = "" if home else "../index.html"
    brand = "#top" if home else "../index.html"
    links = "".join(f'<li><a href="{pre}{s["id"]}.html" data-s="{s["id"]}|t">{esc(s["en"]["t"])}</a></li>' for s in SERVICES)
    return f'''
<footer class="ftr">
  <div class="ftr__big" aria-hidden="true">EDO</div>
  <div class="wrap">
    <div class="ftr__grid">
      <div>
        <a class="logo" href="{brand}" aria-label="Eminent Destino">
          <img class="logo__img" alt="Eminent Destino" referrerpolicy="no-referrer" decoding="async">
          <span class="logo__fb"><b>EDO</b><em>Eminent Destino</em></span>
        </a>
        <p style="margin-top:1rem;max-width:34ch" data-i18n="ft.line">A joint venture by Eminent (Jahin Music) and Destino. Built for Myanmar's digital creators.</p>
      </div>
      <div>
        <h3 data-i18n="ft.services">Services</h3>
        <ul>{links}</ul>
      </div>
      <div>
        <h3 data-i18n="ft.offices">Offices</h3>
        <ul>
          <li><strong>Eminent (Jahin Music)</strong><br><span data-i18n="ft.eminent">USA (HQ), UAE, Bangladesh</span></li>
          <li><strong>Destino</strong><br><span data-i18n="ft.destino">Myanmar</span></li>
        </ul>
      </div>
      <div>
        <h3 data-i18n="ft.contact">Contact</h3>
        <ul>
          <li><a id="mailLink2" href="#"></a></li>
          <li><a href="https://www.facebook.com/profile.php?id=61592448591808" target="_blank" rel="noopener noreferrer">Facebook</a></li>
          <li><a href="https://t.me/+959674092920" target="_blank" rel="noopener noreferrer">Telegram · +95 9674092920</a></li>
        </ul>
      </div>
    </div>
    <div class="ftr__legal">
      <span>© <span id="yr">2026</span> Eminent Destino</span>
      <a href="{'#top' if home else '#top'}" data-i18n="ft.top">Back to top</a>
    </div>
  </div>
</footer>'''

def options():
    return "".join(f'<option value="{s["id"]}" data-s="{s["id"]}|t">{esc(s["en"]["t"])}</option>' for s in SERVICES)

def contact(service_page):
    tint = " sec--tint" if service_page else ""
    title_key, sub_key = ("ct2.title", "ct2.sub") if service_page else ("ct.title", "ct.sub")
    title = "Ready to start? Tell us about your project." if service_page else "Your work deserves a bigger stage."
    sub = ("Send us a few details and our team will reply by email." if service_page
           else "Artists, labels, creators and media partners — let's build your global digital future from Myanmar.")
    return f'''
  <section class="sec{tint}" id="contact">
    <div class="wrap contact">
      <div data-reveal>
        <h2 data-i18n="{title_key}">{title}</h2>
        <p class="lead" data-i18n="{sub_key}">{sub}</p>
        <dl class="info">
          <div><dt>Email</dt><dd><a id="mailLink" href="#"></a></dd></div>
          <div><dt>Facebook</dt><dd><a href="https://www.facebook.com/profile.php?id=61592448591808" target="_blank" rel="noopener noreferrer">Eminent Destino</a></dd></div>
          <div><dt>Telegram</dt><dd><a href="https://t.me/+959674092920" target="_blank" rel="noopener noreferrer">+95 9674092920</a></dd></div>
          <div><dt data-i18n="ft.eminent.h">Eminent (Jahin Music)</dt><dd data-i18n="ft.eminent">USA (HQ), UAE, Bangladesh</dd></div>
          <div><dt>Destino</dt><dd data-i18n="ft.destino">Myanmar</dd></div>
        </dl>
      </div>
      <form class="form" id="form" novalidate data-reveal style="--d:.12s">
        <div class="two">
          <label><span data-i18n="ct.name">Name</span><input name="name" autocomplete="name" required></label>
          <label><span data-i18n="ct.email">Email</span><input name="email" type="email" autocomplete="email" required></label>
        </div>
        <label><span data-i18n="ct.company">Company or channel</span><input name="company" autocomplete="organization"></label>
        <label><span data-i18n="ct.interest">I'm interested in</span><select name="interest" id="interest">{options()}</select></label>
        <label><span data-i18n="ct.msg">Message</span><textarea name="message"></textarea></label>
        <button class="btn" type="submit"><span data-i18n="ct.send">Send message</span>{ARROW}</button>
        <p class="msg" id="msg" role="status"></p>
      </form>
    </div>
  </section>'''

CODE_PANEL = '''
      <div class="code" data-reveal aria-label="API example" style="max-width:920px">
        <div class="code__bar">
          <i></i><i></i><i></i>
          <div class="tabs" role="tablist">
            <button role="tab" type="button" data-tab="release" aria-selected="true" data-i18n="wl.tab1">Create release</button>
            <button role="tab" type="button" data-tab="statement" aria-selected="false" data-i18n="wl.tab2">Get statement</button>
            <button role="tab" type="button" data-tab="webhook" aria-selected="false" data-i18n="wl.tab3">Webhook</button>
          </div>
        </div>
        <pre class="req" id="codeReq"></pre>
        <pre class="res" id="codeRes" aria-live="polite"></pre>
        <p class="code__note" data-i18n="wl.note">Sample only. Endpoints and fields are shared with approved partners.</p>
      </div>'''

FLOW = '''
      <div class="flow flow--solo" data-reveal>
        <div class="node"><h3 data-i18n="flow.brand">Your brand</h3><p data-i18n="flow.brandsub">Dashboard, domain, app</p></div>
        <div class="link" aria-hidden="true"></div>
        <div class="node node--hub"><b>EDO</b><p data-i18n="flow.hub">Rights, delivery, payouts</p></div>
        <div class="link" aria-hidden="true"></div>
        <div class="node">
          <h3 data-i18n="flow.dest">Global destinations</h3>
          <ul class="dests"><li>YouTube</li><li>Facebook</li><li>VEVO</li><li data-i18n="flow.d3">Music platforms</li><li data-i18n="flow.d5">Film &amp; series</li></ul>
        </div>
      </div>'''

PAYOUT_CHIPS = '''
        <div class="chipgroup">
          <h3 data-i18n="mcn.methods">Payout methods</h3>
          <ul class="chips"><li data-i18n="pay.1">Bank transfer</li><li data-i18n="pay.2">Crypto</li><li>KBZ Pay</li><li>Payoneer</li><li>PayPal</li></ul>
        </div>
        <div class="chipgroup">
          <h3 data-i18n="mcn.currency">Payout currencies</h3>
          <ul class="chips"><li data-i18n="pay.mmk">Kyat (MMK)</li><li>USD</li></ul>
        </div>'''

SITE = "https://www.eminentdestino.com"

def head(title, desc, path, service=None):
    url = SITE + path
    data = {"@context":"https://schema.org", "@type":"Organization", "name":"Eminent Destino", "alternateName":"EDO", "url":SITE+"/", "logo":SITE+"/assets/logo.jpg", "description":"A Myanmar focused joint venture by Eminent (Jahin Music) and Destino for creators, artists and labels.", "contactPoint":{"@type":"ContactPoint", "email":"info@eminentdestino.com", "contactType":"customer support", "availableLanguage":["English","Burmese"]}}
    if service:
        data = {"@context":"https://schema.org", "@type":"Service", "name":service["en"]["t"], "description":desc, "url":url, "provider":{"@type":"Organization", "name":"Eminent Destino", "url":SITE+"/"}, "areaServed":{"@type":"Country", "name":"Myanmar"}}
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="referrer" content="no-referrer">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc).replace('"', '&quot;')}">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc).replace('"', '&quot;')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Eminent Destino">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/logo.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')}</script>
<meta name="theme-color" content="#FF6B00">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+Myanmar:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>'''

def page(title, desc, root, page_id, home, main, service=None):
    path = "/" if home else f"/services/{page_id}.html"
    return f'''{head(title, desc, path, service)}
<body data-root="{root}" data-page="{page_id}">
<div id="progress" aria-hidden="true"></div>
{header(home)}
<main id="top">
{main}
</main>
{footer(home)}
<script>
{JS}
</script>
</body>
</html>
'''

# ---------------------------------------------------------------- HOME
def tiles():
    out = []
    for i, s in enumerate(SERVICES):
        cls = "tile"
        if i == 0: cls += " tile--hot"
        if i in (5, 6): cls += " tile--soft tile--half"
        if i in (7, 8): cls += " tile--half"
        who = f'<span class="who" data-s="{s["id"]}|who">{esc(s["en"]["who"])}</span>' if "who" in s["en"] else ""
        out.append(f'''
        <a class="{cls}" href="services/{s["id"]}.html" data-tilt data-reveal style="--d:{(i%3)*0.08:.2f}s">
          <div class="tile__top"><span class="ico">{svg(ICONS[s["id"]])}</span>{who}</div>
          <div><h3 data-s="{s["id"]}|t">{esc(s["en"]["t"])}</h3><p data-s="{s["id"]}|tag">{esc(s["en"]["tag"])}</p></div>
          <span class="go"><span data-i18n="svc.more">Learn more</span>{ARROW}</span>
        </a>''')
    return "".join(out)

def marquee():
    items = "".join(f'<div class="marquee__item" data-s="{s["id"]}|t">{esc(s["en"]["t"])}</div>' for s in SERVICES)
    return items + items

MCN_ROWS = [
 ("Join our MCN", "Join EDO's Multi-Channel Network for your YouTube channels and Facebook Pages. After a quick channel review, our team handles onboarding and setup.",
  '<circle cx="9" cy="8" r="3.2"/><path d="M3.5 19c.6-3 2.7-4.7 5.5-4.7s4.9 1.7 5.5 4.7"/><path d="M16 5.5a3 3 0 0 1 0 5.8M18 14.6c1.6.6 2.6 2.1 3 4.4"/>'),
 ("AdSense help and policy guidance", "We help with AdSense-related issues and give you clear YouTube policy guidance, so your channel stays in good standing. We can't promise approval where platform policy doesn't allow it.",
  '<path d="M12 3l8 3v6c0 4.5-3.2 7.8-8 9-4.8-1.2-8-4.5-8-9V6z"/><path d="M9 12l2.2 2.2L15.5 10"/>'),
 ("Monthly, on-time payments", "You are paid every month, on time, with clear statements that show how your earnings were calculated.",
  '<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
 ("Choose your payout method", "Bank transfer, crypto, KBZ Pay, Payoneer or PayPal. Pick whatever works best for you.",
  '<rect x="3" y="6" width="18" height="12" rx="3"/><circle cx="12" cy="12" r="2.6"/>'),
 ("Kyat or USD", "Get paid directly in Kyat (MMK), or in USD if you prefer. The exchange rate is shown before every payout.",
  '<path d="M7 7h11l-3-3M17 17H6l3 3"/>'),
 ("Competitive payout rate", "A competitive revenue share with no hidden EDO fees. Any personal or local taxes remain your responsibility.",
  '<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>'),
 ("Burmese support team", "Talk to a team that speaks Burmese and understands local creators, payments and everyday channel problems.",
  '<path d="M4 5h16v11H9l-5 4z"/><path d="M8.5 9.5h7M8.5 12.5h4"/>'),
]
def mcn_rows():
    return "".join(f'''
        <li class="row" data-row>
          <span class="ico">{svg(ic)}</span>
          <div><h3 data-i18n="mcn.{i+1}t">{esc(t)}</h3><p data-i18n="mcn.{i+1}d">{esc(d)}</p></div>
        </li>''' for i, (t, d, ic) in enumerate(MCN_ROWS))

WL_FEATS = [
 ("White-label dashboard", "Your logo, your domain, your colors. Your partners never see another brand."),
 ("REST API", "Create releases, upload catalogs and pull statements straight from your own system."),
 ("Webhooks", "Get notified about delivery status, claims and payouts as they happen."),
 ("Sub-accounts and roles", "Give every label or creator their own login and permissions."),
 ("Royalty reporting", "Clear statements and split rules you can pass on to your own users."),
 ("Integration support", "A named EDO contact helps your team go live and stay live."),
]
def wl_feats():
    return "".join(f'''
            <div class="feat">{CHECK}<div><h3 data-i18n="wl.{i+1}t">{esc(t)}</h3><p data-i18n="wl.{i+1}d">{esc(d)}</p></div></div>''' for i, (t, d) in enumerate(WL_FEATS))

def home_main():
    return f'''
  <section class="hero" id="hero">
    <div class="hero__media">
      <video id="heroVideo" autoplay muted loop playsinline preload="auto" disablepictureinpicture disableremoteplayback aria-hidden="true"></video>
    </div>
    <div class="eqbars" id="eqbars" aria-hidden="true"></div>
    <div class="hero__shade"></div>
    <button type="button" class="playbtn" id="playBtn" hidden><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg><span data-i18n="play.btn">Tap to play video</span></button>
    <div class="wrap hero__inner">
      <p class="hero__badge" data-in style="--i:0"><i></i><span data-i18n="hero.badge">Empowering Myanmar's Digital Ecosystem</span></p>
      <h1 data-in style="--i:1"><span data-i18n="hero.l1">Myanmar's creators.</span><span data-i18n="hero.l2">Global reach.</span></h1>
      <p class="hero__lead" data-in style="--i:2" data-i18n="hero.lead">YouTube and Facebook monetization, music distribution, publishing, copyright protection and more — plus white-label and API services for B2B partners.</p>
      <div class="hero__cta" data-in style="--i:3">
        <a class="btn btn--white" href="#services"><span data-i18n="hero.cta1">Explore services</span>{ARROW}</a>
        <a class="btn btn--ghost" href="#contact" data-interest="youtube-mcn"><span data-i18n="hero.cta2">Join the MCN</span></a>
      </div>
    </div>
  </section>

  <div class="marquee" aria-hidden="true"><div class="marquee__track">{marquee()}</div></div>

  <section class="sec" id="about">
    <div class="wrap">
      <div class="about">
        <div data-reveal>
          <h2 data-i18n="about.title">Two companies. One platform for Myanmar.</h2>
          <p data-i18n="about.p">In 2026, Eminent (Jahin Music) and Destino joined forces to create Eminent Destino: a platform built to give Myanmar's creators a better service than the options available today.</p>
          <div class="eq" aria-label="Eminent plus Destino equals EDO"><b>Eminent</b><span>×</span><b>Destino</b><span>=</span><b class="edo">EDO</b></div>
        </div>
        <div class="stats" data-reveal style="--d:.15s">
          <div class="stat"><b data-count="9">0</b><span data-i18n="stat.1">Services</span></div>
          <div class="stat"><b data-count="5">0</b><span data-i18n="stat.2">Payout methods</span></div>
          <div class="stat"><b class="sm">MMK + USD</b><span data-i18n="stat.3">Payout currencies</span></div>
          <div class="stat"><b class="sm" data-i18n="stat.4v">Monthly</b><span data-i18n="stat.4">Payout cycle</span></div>
        </div>
      </div>
      <div class="ents">
        <article class="ent ent--a" data-reveal>
          <h3>Eminent (Jahin Music)</h3>
          <p data-i18n="ent.a">A music distribution and YouTube MCN company based in the USA, with offices in the UAE and Bangladesh.</p>
          <ul class="tags"><li data-i18n="loc.usa">USA (HQ)</li><li data-i18n="loc.uae">UAE</li><li data-i18n="loc.bd">Bangladesh</li></ul>
        </article>
        <article class="ent ent--b" data-reveal style="--d:.1s">
          <h3>Destino</h3>
          <p data-i18n="ent.b">A Myanmar-based label and music distribution company with strong knowledge of the local market.</p>
          <ul class="tags"><li data-i18n="loc.mm">Myanmar</li></ul>
        </article>
      </div>
    </div>
  </section>

  <section class="sec sec--tint" id="services">
    <div class="wrap">
      <div class="svc-head" data-reveal>
        <h2 data-i18n="svc.title">Everything your music and channels need.</h2>
        <p data-i18n="svc.sub">Nine services, one partner. Open any service to see how it works.</p>
      </div>
      <div class="explorer" data-reveal>
        <div class="explorer__intro"><p data-i18n="explore.label">FIND YOUR STARTING POINT</p><h3 data-i18n="explore.title">What do you need help with?</h3></div>
        <div class="explorer__choices" role="group" aria-label="Choose a service" data-i18n-aria="explore.aria">
          <button type="button" data-explore="youtube-mcn" aria-pressed="true" data-i18n="explore.creator">My YouTube channel</button>
          <button type="button" data-explore="music-distribution" aria-pressed="false" data-i18n="explore.artist">My music release</button>
          <button type="button" data-explore="white-label" aria-pressed="false" data-i18n="explore.partner">My creator business</button>
        </div>
        <div class="explorer__result" aria-live="polite"><div><strong id="explorerName"></strong><p id="explorerText"></p></div><a class="go" id="explorerLink" href="services/youtube-mcn.html"><span data-i18n="explore.action">Explore this service</span>{ARROW}</a></div>
      </div>
      <div class="bento">{tiles()}
      </div>
    </div>
  </section>

  <section class="sec" id="mcn">
    <div class="wrap mcn">
      <div class="mcn__side" data-reveal>
        <h2 data-i18n="mcn.title">Monetize in Myanmar with EDO.</h2>
        <p class="lead" data-i18n="mcn.intro">YouTube and Facebook monetization are not directly available for Myanmar accounts. Join EDO's Multi-Channel Network (MCN) and earn through our managed network, with policy guidance and support from a Burmese-speaking team.</p>{PAYOUT_CHIPS}
        <a class="btn" href="#contact" data-interest="youtube-mcn"><span data-i18n="mcn.cta">Join the MCN</span>{ARROW}</a>
      </div>
      <ul class="rows">{mcn_rows()}
      </ul>
    </div>
  </section>

  <section class="sec wl" id="partners">
    <div class="wrap">
      <div class="wl__grid">
        <div data-reveal>
          <h2 data-i18n="wl.title">One system. Your brand on top.</h2>
          <p class="lead" data-i18n="wl.intro">White label and API services for labels, distributors and B2B clients: run EDO's distribution, MCN and rights tools under your own brand, or connect your own platform straight to ours.</p>
          <div class="feats">{wl_feats()}
          </div>
          <div class="wl__cta">
            <a class="btn btn--white" href="#contact" data-interest="api"><span data-i18n="wl.cta1">Request API access</span>{ARROW}</a>
            <a class="btn btn--ghost" href="services/white-label.html"><span data-i18n="wl.cta2">See white-label services</span></a>
          </div>
        </div>
        {CODE_PANEL.replace(' style="max-width:920px"', ' style="--d:.15s"')}
      </div>
      {FLOW.replace("flow flow--solo", "flow")}
    </div>
  </section>
{contact(False)}
'''

# ---------------------------------------------------------------- SERVICE PAGES
def service_details(s):
    sid = s["id"]; en = s["en"]
    def field(key, tag="span", attrs=""):
        parts = key.split(".")
        value = en[parts[0]] if len(parts) == 1 else en[parts[0]][int(parts[1])]
        return f'<{tag} data-s="{sid}|{key}" {attrs}>{esc(value)}</{tag}>'
    cards = "".join(f'''<article class="service-card" data-reveal style="--d:{k*.08:.2f}s">
      <span class="service-card__number" aria-hidden="true">0{k+1}</span>
      {field(f"focus.{k*2}", "h3")}{field(f"focus.{k*2+1}", "p")}</article>''' for k in range(3))
    checklist = "".join(f'<li>{CHECK}{field(f"prepare.{k}")}</li>' for k in range(len(en["prepare"])))
    faqs = "".join(f'''<details class="service-faq" data-reveal>
      <summary>{field(f"faq.{k}")}<span class="service-faq__icon" aria-hidden="true"></span></summary>
      {field(f"faq.{k+1}", "p")}</details>''' for k in range(0, len(en["faq"]), 2))
    return f'''
  <section class="sec" id="service-details">
    <div class="wrap">
      <div class="service-heading" data-reveal>
        <p class="service-eyebrow" data-i18n="detail.eyebrow">The service, explained</p>
        {field("detailTitle", "h2")}{field("detailIntro", "p", 'class="lead"')}
      </div>
      <div class="service-grid">{cards}</div>
    </div>
  </section>
  <section class="sec sec--tint" id="why-edo">
    <div class="wrap service-reasons">
      <div data-reveal><p class="service-eyebrow" data-i18n="detail.partner">Your EDO partnership</p>
        {field("whyTitle", "h2")}{field("why", "p", 'class="lead"')}
        <a class="btn" href="#contact" data-interest="{sid}"><span data-i18n="detail.talk">Let's talk about your project</span>{ARROW}</a>
      </div>
      <aside class="service-prepare" data-reveal style="--d:.12s">
        <span class="ico" aria-hidden="true">{svg(ICONS[sid])}</span>
        <h3 data-i18n="detail.prepare">What to prepare</h3>
        <p data-i18n="detail.prepareNote">A few details help us make the first conversation useful.</p>
        <ul class="sp-list">{checklist}</ul>
      </aside>
    </div>
  </section>''', f'''
  <section class="sec" id="questions">
    <div class="wrap service-questions">
      <div data-reveal><p class="service-eyebrow" data-i18n="detail.before">Before you start</p>
        <h2 data-i18n="detail.faq">Good questions. Clear answers.</h2>
        <p class="lead" data-i18n="detail.faqNote">Explore the details, then talk to us about your own project.</p>
      </div>
      <div>{faqs}</div>
    </div>
    </section>'''

def mcn_extra():
    en = MCN_COPY["en"]
    def t(key, tag="p", cls=""):
        attr = f' class="{cls}"' if cls else ""
        return f'<{tag}{attr} data-i18n="{key}">{esc(en[key])}</{tag}>'
    pain = "".join(f'<article data-reveal style="--d:{i*.07:.2f}s"><span>0{i+1}</span>{t("mcn.pain"+str(i+1)+"h","h3")}{t("mcn.pain"+str(i+1)+"p")}</article>' for i in range(3))
    benefits = "".join(f'<article data-reveal style="--d:{(i%3)*.08:.2f}s"><span aria-hidden="true">✦</span>{t("mcn.benefit"+str(i+1)+"h","h3")}{t("mcn.benefit"+str(i+1)+"p")}</article>' for i in range(8))
    oo_steps = "".join(f'<article data-reveal style="--d:{i*.08:.2f}s"><span>0{i+1}</span>{t("mcn.oo"+str(i+1)+"h","h3")}{t("mcn.oo"+str(i+1)+"p")}</article>' for i in range(3))
    return f'''
  <section class="sec mcn-story sec--line" id="mcn-route">
    <div class="wrap">
      <div class="mcn-story__heading" data-reveal>{t("mcn.eyebrow","p","service-eyebrow")}{t("mcn.routeh","h2")}{t("mcn.routep","p","lead")}</div>
      <div class="mcn-pains">{pain}</div>
      <div class="mcn-bridge" data-reveal><span class="mcn-bridge__mark">EDO</span><div>{t("mcn.bridgeh","h3")}{t("mcn.bridgep")}</div></div>
    </div>
  </section>
  <section class="sec mcn-oo" id="mcn-oo"><div class="wrap">
    <div class="mcn-story__heading" data-reveal>{t("mcn.ooeye","p","service-eyebrow")}{t("mcn.ooh","h2")}{t("mcn.oop","p","lead")}</div>
    <div class="mcn-oo__grid">{oo_steps}</div>
    {t("mcn.oonote","p","mcn-note")}
  </div></section>
  <section class="sec sec--tint" id="mcn-payments">
    <div class="wrap">
      <div class="mcn-story__heading" data-reveal>{t("mcn.payeye","p","service-eyebrow")}{t("mcn.payh","h2")}{t("mcn.payp","p","lead")}</div>
      <div class="mcn-timeline" data-reveal>
        <div><span>01</span>{t("mcn.jan","h3")}{t("mcn.mar")}</div>
        <div><span>02</span>{t("mcn.feb","h3")}{t("mcn.apr")}</div>
        <div><span>03</span>{t("mcn.march","h3")}{t("mcn.may")}</div>
      </div>
      <div class="mcn-settlement" data-reveal>{t("mcn.settleh","h3")}{t("mcn.settlep")}</div>
      <div class="mcn-calculator" data-reveal>
        <div>{t("mcn.calch","h3")}{t("mcn.calcp")}
          <label for="mcnEarnings" data-i18n="mcn.input">Finalized channel revenue (USD)</label>
          <div class="mcn-calculator__input"><span>$</span><input type="number" id="mcnEarnings" min="0" step="1" value="1000" inputmode="decimal"></div>
        </div>
        <div class="mcn-calculator__result"><p data-i18n="mcn.share">Your share · example 80/20 agreement</p><output id="mcnResult" for="mcnEarnings">$800.00</output><p data-i18n="mcn.calcfoot">Example before any applicable withholding, transfer charges or adjustments. Your agreement and final statement control the actual amount.</p></div>
      </div>
      <div class="mcn-tax-policy" data-reveal><strong>0%</strong><div>{t("mcn.zeroh","h3")}{t("mcn.zerop")}</div></div>
      {t("mcn.tax","p","mcn-note")}
    </div>
  </section>
  <section class="sec mcn-support" id="mcn-support">
    <div class="wrap"><div class="mcn-story__heading" data-reveal>{t("mcn.supporteye","p","service-eyebrow")}{t("mcn.supporth","h2")}{t("mcn.supportp","p","lead")}</div><div class="mcn-benefits">{benefits}</div>
      <div class="mcn-addons" data-reveal>{t("mcn.addonsh","h3")}{t("mcn.addonsp")}</div>
    </div>
  </section>
  <section class="sec sec--tint mcn-join" id="mcn-eligibility"><div class="wrap mcn-join__grid">
    <div data-reveal>{t("mcn.joinh","h2")}{t("mcn.joinp","p","lead")}
      <div class="mcn-examples"><div>{t("mcn.yesh","h3")}{t("mcn.yesp")}</div><div>{t("mcn.noh","h3")}{t("mcn.nop")}</div></div>
      <a class="btn" href="#contact" data-interest="youtube-mcn"><span data-i18n="mcn.joincta">Ask for a channel review</span>{ARROW}</a>
    </div>
    <div class="mcn-criteria" data-reveal>{t("mcn.criteriah","h3")}<ul>
      <li>{t("mcn.criteria1")}</li><li>{t("mcn.criteria2")}</li><li>{t("mcn.criteria3")}</li><li>{t("mcn.criteria4")}</li>
    </ul></div></div></section>
  <section class="sec mcn-b2b"><div class="wrap mcn-b2b__grid" data-reveal><div>{t("mcn.b2beye","p","service-eyebrow")}{t("mcn.b2bh","h2")}{t("mcn.b2bp","p","lead")}</div><div class="mcn-b2b__action">{t("mcn.b2bdetail")}<a class="btn" href="white-label.html"><span data-i18n="mcn.b2bcta">Explore B2B services</span>{ARROW}</a></div></div></section>
  <div class="wrap mcn-sources">{t("mcn.sources")} <a href="https://support.google.com/youtube/answer/2737059" target="_blank" rel="noopener noreferrer">YouTube MCN overview</a> · <a href="https://support.google.com/youtube/answer/10391273" target="_blank" rel="noopener noreferrer">MCN tax guidance</a></div>'''

def service_main(i):
    s = SERVICES[i]; sid = s["id"]; en = s["en"]
    details, questions = service_details(s)
    prev_s = SERVICES[(i - 1) % len(SERVICES)]; next_s = SERVICES[(i + 1) % len(SERVICES)]
    who = f'<span class="sp-who" data-s="{sid}|who">{esc(en["who"])}</span>' if "who" in en else ""
    bullets = "".join(f'<li>{CHECK}<span data-s="{sid}|b.{k}">{esc(b)}</span></li>' for k, b in enumerate(en["b"]))
    steps = "".join(f'<li class="step" data-reveal style="--d:{k*0.1:.1f}s"><p data-s="{sid}|s.{k}">{esc(x)}</p></li>' for k, x in enumerate(en["s"]))
    others = "".join(f'<a href="{x["id"]}.html" data-s="{x["id"]}|t">{esc(x["en"]["t"])}</a>' for x in SERVICES if x["id"] != sid)

    extra = ""
    if s["extra"] == "payout":
        extra = f'''
  <section class="sec">
    <div class="wrap payx" data-reveal>
      <h2 data-i18n="payx.title">Get paid your way.</h2>
      <p class="lead" data-i18n="payx.note">Monthly, on time. The exchange rate is shown before every payout.</p>{PAYOUT_CHIPS}
    </div>
  </section>'''
    elif s["extra"] == "api":
        extra = f'''
  <section class="sec wl">
    <div class="wrap">
      <h2 data-i18n="x.api">A sample API request</h2>{CODE_PANEL}
    </div>
  </section>'''
    elif s["extra"] == "flow":
        extra = f'''
  <section class="sec wl">
    <div class="wrap">
      <h2 data-i18n="x.flow">How it fits together</h2>{FLOW}
    </div>
  </section>'''

    return f'''
  <section class="sp-hero">
    <div class="sp-art" aria-hidden="true">{svg(ICONS[sid])}</div>
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="../index.html" data-i18n="crumb.home">Home</a><span aria-hidden="true">/</span>
        <a href="../index.html#services" data-i18n="crumb.services">Services</a><span aria-hidden="true">/</span>
        <span data-s="{sid}|t">{esc(en["t"])}</span>
      </nav>
      <div class="sp-ico">{svg(ICONS[sid])}</div>
      <h1 data-s="{sid}|t">{esc(en["t"])}</h1>
      <p class="sp-tag" data-s="{sid}|tag">{esc(en["tag"])}</p>
      {who}
      <div class="sp-hero__cta">
        <a class="btn btn--white" href="#contact" data-interest="{sid}"><span data-i18n="sp.start">Get started</span>{ARROW}</a>
        <a class="btn btn--ghost" id="mailBtn" href="#"><span data-i18n="sp.email">Email us</span></a>
      </div>
    </div>
  </section>

  <nav class="service-jump wrap" aria-label="Service sections" data-i18n-aria="detail.nav">
    <a href="#service-details" data-i18n="detail.overview">Service overview</a>
    {'''<a href="#mcn-route" data-i18n="mcn.jump1">Myanmar &amp; MCN</a><a href="#mcn-oo" data-i18n="mcn.jumpoo">O&amp;O model</a><a href="#mcn-payments" data-i18n="mcn.jump2">Payments</a><a href="#mcn-eligibility" data-i18n="mcn.jump3">Eligibility</a>''' if sid == "youtube-mcn" else ""}
    <a href="#why-edo" data-i18n="detail.why">Why EDO</a>
    <a href="#how-it-works" data-i18n="sp.how">How it works</a>
    <a href="#questions" data-i18n="detail.faqShort">FAQs</a>
    <a href="#contact" data-i18n="nav.contact">Contact</a>
  </nav>

  <section class="sec sec--tint">
    <div class="wrap sp-body">
      <div data-reveal>
        <p class="lead" data-s="{sid}|p">{esc(en["p"])}</p>
        <div class="forbox"><h3 data-i18n="sp.for">Who it's for</h3><p data-s="{sid}|for">{esc(en["for"])}</p></div>
      </div>
      <div data-reveal style="--d:.1s">
        <h3 class="sp-list__h" data-i18n="sp.inc">What's included</h3>
        <ul class="sp-list">{bullets}</ul>
      </div>
    </div>
  </section>

{details}
{mcn_extra() if sid == "youtube-mcn" else ""}
  <section class="sec" id="how-it-works">
    <div class="wrap">
      <h2 class="steps-h" data-i18n="sp.how">How it works</h2>
      <ol class="steps">{steps}</ol>
    </div>
  </section>
{extra}
{questions}
{contact(True)}

  <section class="sec sec--line">
    <div class="wrap">
      <h2 style="font-size:clamp(1.6rem,3vw,2.4rem)" data-i18n="sp.more">More services</h2>
      <div class="more">{others}</div>
      <div class="pn">
        <a href="{prev_s["id"]}.html"><small data-i18n="sp.prev">Previous service</small><strong data-s="{prev_s["id"]}|t">{esc(prev_s["en"]["t"])}</strong></a>
        <a href="{next_s["id"]}.html"><small data-i18n="sp.next">Next service</small><strong data-s="{next_s["id"]}|t">{esc(next_s["en"]["t"])}</strong></a>
      </div>
    </div>
  </section>
'''

# ---------------------------------------------------------------- WRITE
os.makedirs(f"{OUT}/services", exist_ok=True); os.makedirs(f"{OUT}/assets", exist_ok=True)
for old in os.listdir(f"{OUT}/services"):
    if old.endswith(".html"): os.remove(os.path.join(OUT, "services", old))

def write_once(path, text):
    if not os.path.exists(path):
        open(path, "w", encoding="utf-8").write(text)

home_title = "Eminent Destino | Myanmar Creator, Music & B2B Services"
home_desc = "Myanmar creator services: YouTube and Facebook monetization, music distribution and publishing, copyright protection, VEVO, video production, white-label platforms and API services."
open(f"{OUT}/index.html", "w", encoding="utf-8").write(page(home_title, home_desc, "", "home", True, home_main()))

for i, s in enumerate(SERVICES):
    seo = {
        "youtube-mcn": ("YouTube Monetization in Myanmar | MCN & CMS — Eminent Destino", "Explore YouTube monetization support in Myanmar with Eminent Destino's MCN and CMS: channel review, rights management, Content ID and monthly payments."),
        "facebook": ("Facebook Monetization in Myanmar | Page Support — Eminent Destino", "Facebook Page management and monetization support for Myanmar creators. Explore eligibility, copyright support and payout coordination with Eminent Destino."),
        "music-distribution": ("Music Distribution in Myanmar | Eminent Destino", "Distribute music from Myanmar to global streaming platforms with Eminent Destino. Explore release delivery, rights support and royalty reporting for artists and labels."),
    }
    title, desc = seo.get(s["id"], (f'{s["en"]["t"]} in Myanmar | Eminent Destino', f'{s["en"]["tag"]} {s["en"]["p"][:100]}'))
    open(f'{OUT}/services/{s["id"]}.html', "w", encoding="utf-8").write(
        page(title, desc, "../", s["id"], False, service_main(i), s))

urls = [SITE + "/"] + [SITE + "/services/" + s["id"] + ".html" for s in SERVICES]
open(f"{OUT}/sitemap.xml", "w", encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{url}</loc></url>\n' for url in urls) + '</urlset>\n')
open(f"{OUT}/robots.txt", "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")

write_once(f"{OUT}/assets/README.txt", """ASSETS FOLDER
=============
Put these files here and the website will use them automatically:

  logo.png      Your main logo (PNG with transparent or white background, about 400px wide).
  hero.mp4      Homepage video (H.264 + AAC, ideally under 15 MB).
  hero.webm     Optional. Same video as WebM (smaller in Chrome/Firefox/Android).

If these files are missing, the site falls back to:
  logo   ->  https://storage.jahinmusic.com/2026-09-18%2023.58.40.jpg
  video  ->  https://storage.jahinmusic.com/0717.mp4  then  0717.mov
and finally to a clean EDO wordmark and an animated orange background.

CONVERT YOUR .MOV TO A WEB-FRIENDLY MP4 (works on iPhone, Android, Mac, Windows):

  ffmpeg -i 0717.mov -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 26 -preset slow \\
         -vf "scale='min(1280,iw)':-2" -movflags +faststart -c:a aac -b:a 128k hero.mp4

Optional WebM:

  ffmpeg -i 0717.mov -c:v libvpx-vp9 -crf 34 -b:v 0 -vf "scale='min(1280,iw)':-2" -c:a libopus hero.webm
""")

write_once(f"{OUT}/README.txt", """EMINENT DESTINO WEBSITE
=======================
index.html              Home page            (generated)
services/*.html         9 service pages      (generated)
assets/                 Put logo.png and hero.mp4 here (see assets/README.txt)
src/                    SOURCE: services.json (service text EN+Burmese), style.css, site.js
build.py                Regenerates index.html and services/*.html from src/
CLAUDE.md               Instructions for Claude Code
_headers                Cloudflare Pages cache and security headers
.gitignore              Keeps junk files out of Git

EDIT THE SITE
-------------
Edit files in src/ (never edit the generated HTML by hand), then run:   python3 build.py
Commit everything, including the regenerated HTML. Cloudflare only serves the committed files.

Every page is self-contained (styles and scripts are inside the file). No build step.

DEPLOY: GITHUB + CLOUDFLARE PAGES
---------------------------------
1) Put the files of this folder in the ROOT of a GitHub repository
   (index.html must sit at the top level of the repo, not inside a sub-folder).
2) Cloudflare dashboard > Workers & Pages > Create > Pages > Connect to Git > pick the repo.
3) Build settings:
     Framework preset ........ None
     Build command ........... (leave empty)
     Build output directory .. /        (a single slash, or leave the default)
4) Save and Deploy. Every git push to the main branch redeploys automatically.
5) Custom domain: Pages project > Custom domains > Set up a domain > eminentdestino.com

LIMITS
  Cloudflare Pages: max 25 MiB per file  ->  keep assets/hero.mp4 under 25 MB (aim for 8-15 MB).
  GitHub: max 100 MB per file (warning above 50 MB).

Contact form opens the visitor's email app addressed to info@eminentdestino.com.
Language switch (EN / Burmese) is in the top bar and is remembered.
""")

write_once(f"{OUT}/CLAUDE.md", """# Eminent Destino (EDO) website

Static multi-page site, deployed by Cloudflare Pages straight from this repo (no build step on Cloudflare).

## How it is organised
- `src/services.json`  Text of the 9 service pages, English (`en`) and Burmese (`my`). One source for tiles, pages, footer and the contact form.
- `src/site.js`        All behaviour: EN/Burmese switch (the `MY` object holds Burmese for the static text), hero video loader, logo loader, contact form, API sample.
- `src/style.css`      All styling. Orange #FF6B00 and white. Fully responsive.
- `build.py`           Generates `index.html` and `services/*.html` (each file is self-contained: CSS and JS are inlined).

## Rules
1. Edit `src/` and then run `python3 build.py`. Never hand-edit the generated HTML.
2. Commit the regenerated HTML together with the source change.
3. Every visible string needs an English version and a Burmese version (`data-i18n` key + entry in `MY` in `src/site.js`, or `en`/`my` in `services.json`).
4. Keep every file under 25 MiB (Cloudflare Pages limit). The hero video goes in `assets/hero.mp4` (H.264, aim for 8-15 MB), the logo in `assets/logo.png`.
5. Contact email is `info@eminentdestino.com` (`CONTACT_EMAIL` in `src/site.js`).
6. Do not promise results the company cannot guarantee (AdSense approval, revenue). Keep wording such as "help with" and "competitive".
""")

write_once(f"{OUT}/_headers", """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin

/assets/*
  Cache-Control: public, max-age=86400
""")

write_once(f"{OUT}/.gitignore", """.DS_Store
Thumbs.db
*.log
node_modules/
*.mov
""")

print("built", len(SERVICES) + 1, "pages")
