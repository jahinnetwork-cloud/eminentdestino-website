"""Decorative inline SVG illustrations (no text, so no i18n). Flat fills only: no ids, so they can repeat on a page."""

O, OD, OS, OT, INK, W = "#FF6B00", "#E04E00", "#FFE6D1", "#FFF5EC", "#1E1611", "#FFFFFF"

def _svg(cls, vb, inner, extra=""):
    return f'<svg class="{cls}" viewBox="{vb}" aria-hidden="true" focusable="false"{extra}>{inner}</svg>'

# ---- hero stickers: float over the video, right-hand side (desktop only)
_STICKER_PLAY = _svg("st st--play", "0 0 220 150", f'''
  <rect x="6" y="6" width="208" height="138" rx="26" fill="{W}"/>
  <rect x="22" y="22" width="176" height="82" rx="16" fill="{O}"/>
  <circle cx="110" cy="63" r="26" fill="{W}"/><path d="M102 50v26l22-13z" fill="{O}"/>
  <rect x="22" y="116" width="176" height="8" rx="4" fill="{OS}"/><rect x="22" y="116" width="104" height="8" rx="4" fill="{OD}" class="st__prog"/>''')

_STICKER_VINYL = _svg("st st--vinyl", "0 0 160 160", f'''
  <g class="st__spin"><circle cx="80" cy="80" r="76" fill="{INK}"/>
  <circle cx="80" cy="80" r="62" fill="none" stroke="#3a2c22" stroke-width="2"/><circle cx="80" cy="80" r="50" fill="none" stroke="#3a2c22" stroke-width="2"/>
  <circle cx="80" cy="80" r="28" fill="{O}"/><path d="M60 62a28 28 0 0 1 40 0" fill="none" stroke="{W}" stroke-opacity=".55" stroke-width="5" stroke-linecap="round"/>
  <circle cx="80" cy="80" r="6" fill="{W}"/></g>''')

_STICKER_NOTE = _svg("st st--note", "0 0 110 110", f'''
  <circle cx="55" cy="55" r="52" fill="{W}"/><circle cx="55" cy="55" r="40" fill="{O}"/>
  <path d="M47 71V40l24-6v31" fill="none" stroke="{W}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <ellipse cx="41" cy="72" rx="8" ry="6.5" fill="{W}"/><ellipse cx="65" cy="66" rx="8" ry="6.5" fill="{W}"/>''')

_STICKER_CHART = _svg("st st--chart", "0 0 190 140", f'''
  <rect x="5" y="5" width="180" height="130" rx="24" fill="{W}"/>
  <rect x="26" y="78" width="22" height="38" rx="6" fill="{OS}"/><rect x="58" y="62" width="22" height="54" rx="6" fill="#FFB46B"/>
  <rect x="90" y="46" width="22" height="70" rx="6" fill="{O}"/><rect x="122" y="28" width="22" height="88" rx="6" fill="{OD}"/>
  <path d="M30 60 70 44l30-12 52-14" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M142 16l16 2-6 15" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>''')

_STICKER_COIN = _svg("st st--coin", "0 0 100 100", f'''
  <circle cx="50" cy="50" r="46" fill="#FFC53D"/><circle cx="50" cy="50" r="36" fill="none" stroke="#E5A100" stroke-width="4"/>
  <path d="M58 37c-2-4-14-5-16 2-2 8 18 4 16 13-2 8-15 7-18 1M50 29v6M50 66v6" fill="none" stroke="#B37800" stroke-width="5" stroke-linecap="round"/>''')

_STICKER_HEART = _svg("st st--heart", "0 0 100 100", f'''
  <circle cx="50" cy="50" r="46" fill="{W}"/>
  <path d="M50 72C30 58 24 47 28 38c4-9 16-9 22 0 6-9 18-9 22 0 4 9-2 20-22 34z" fill="{OD}"/>''')

HERO = '<div class="hero-art" aria-hidden="true">' + "".join([
    f'<span class="hero-art__i hero-art__i--{n}">{s}</span>' for n, s in
    [("play", _STICKER_PLAY), ("vinyl", _STICKER_VINYL), ("note", _STICKER_NOTE),
     ("chart", _STICKER_CHART), ("coin", _STICKER_COIN), ("heart", _STICKER_HEART)]]) + '</div>'

# ---- about: Eminent + Destino connect around the globe
def _pin(x, y, c, d):
    return (f'<g transform="translate({x} {y})"><circle r="9" fill="{c}" class="map__ring" style="animation-delay:{d}s"/>'
            f'<circle r="6" fill="{c}" stroke="{W}" stroke-width="3"/></g>')

MAP = _svg("art art--map", "0 0 520 300", f'''
  <circle cx="260" cy="150" r="132" fill="{OT}" stroke="{OS}" stroke-width="2"/>
  <ellipse cx="260" cy="150" rx="132" ry="46" fill="none" stroke="{OS}" stroke-width="2"/>
  <ellipse cx="260" cy="150" rx="58" ry="132" fill="none" stroke="{OS}" stroke-width="2"/>
  <path d="M128 150h264M260 18v264" stroke="{OS}" stroke-width="2"/>
  <path class="map__arc" d="M96 96C170 20 300 20 410 168"/>
  <path class="map__arc" d="M268 118C330 70 380 100 410 168" style="animation-delay:.4s"/>
  <path class="map__arc" d="M332 184C350 160 380 160 410 168" style="animation-delay:.8s"/>
  <path class="map__arc map__arc--hq" d="M410 168C432 214 410 246 380 250" style="animation-delay:1.2s"/>
  {_pin(96, 96, INK, 0)}{_pin(268, 118, INK, .5)}{_pin(332, 184, INK, 1)}{_pin(410, 168, O, 1.5)}{_pin(380, 250, OD, 2)}
  <g class="map__fl"><rect x="22" y="196" width="92" height="52" rx="16" fill="{W}" stroke="{OS}" stroke-width="2"/>
  <path d="M42 232V214l22-6v16" fill="none" stroke="{O}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="38" cy="233" r="5" fill="{O}"/><circle cx="60" cy="227" r="5" fill="{O}"/>
  <rect x="78" y="212" width="24" height="5" rx="2.5" fill="{OS}"/><rect x="78" y="224" width="16" height="5" rx="2.5" fill="{OS}"/></g>
  <g class="map__fl map__fl--b"><rect x="420" y="30" width="80" height="56" rx="16" fill="{O}"/><path d="M450 46v24l20-12z" fill="{W}"/></g>''')

# ---- about: small badges for the two company cards
BADGE_A = _svg("badge", "0 0 80 80", f'''
  <circle cx="40" cy="40" r="38" fill="{W}" stroke="{OS}" stroke-width="2"/>
  <ellipse cx="40" cy="40" rx="15" ry="31" fill="none" stroke="{O}" stroke-width="3"/><path d="M9 40h62M14 24h52M14 56h52" stroke="{O}" stroke-width="3" fill="none"/>
  <circle cx="40" cy="40" r="31" fill="none" stroke="{O}" stroke-width="3"/>''')

BADGE_B = _svg("badge", "0 0 80 80", f'''
  <circle cx="40" cy="40" r="38" fill="{INK}"/>
  <path d="M40 14c4 8 12 10 12 22H28c0-12 8-14 12-22zM24 36h32l4 8H20zM18 44h44v8H18zM12 52h56v10H12z" fill="{O}"/>
  <path d="M40 14v-4" stroke="{O}" stroke-width="3" stroke-linecap="round"/>''')

# ---- MCN: a creator studio that grows
STUDIO = _svg("art art--studio", "0 0 480 340", f'''
  <ellipse cx="240" cy="312" rx="190" ry="14" fill="{OS}"/>
  <g><rect x="70" y="40" width="340" height="212" rx="26" fill="{INK}"/><rect x="86" y="56" width="308" height="180" rx="16" fill="{O}"/>
  <circle cx="240" cy="132" r="42" fill="{W}"/><path d="M227 108v48l42-24z" fill="{O}"/>
  <rect x="104" y="204" width="212" height="9" rx="4.5" fill="{OS}" fill-opacity=".55"/><rect x="104" y="204" width="132" height="9" rx="4.5" fill="{W}" class="st__prog"/>
  <rect x="200" y="252" width="80" height="26" fill="{INK}"/><rect x="160" y="276" width="160" height="14" rx="7" fill="{INK}"/></g>
  <g class="map__fl"><rect x="12" y="150" width="124" height="92" rx="20" fill="{W}" stroke="{OS}" stroke-width="2"/>
  <rect x="30" y="196" width="18" height="30" rx="5" fill="{OS}"/><rect x="56" y="180" width="18" height="46" rx="5" fill="#FFB46B"/><rect x="82" y="164" width="18" height="62" rx="5" fill="{O}"/>
  <path d="M30 184l32-18 22-4" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/></g>
  <g class="map__fl map__fl--b"><circle cx="420" cy="70" r="34" fill="#FFC53D"/><circle cx="420" cy="70" r="26" fill="none" stroke="#E5A100" stroke-width="3.5"/>
  <path d="M427 59c-2-4-12-5-14 1-2 7 15 3 13 11-2 7-13 6-15 1M420 51v5M420 84v5" fill="none" stroke="#B37800" stroke-width="4" stroke-linecap="round"/></g>
  <g class="map__fl"><circle cx="410" cy="244" r="30" fill="{W}" stroke="{OS}" stroke-width="2"/><path d="M410 262c-17-11-22-19-19-26 3-8 13-8 19 0 6-8 16-8 19 0 3 7-2 15-19 26z" fill="{OD}"/></g>
  <path class="st__spark" d="M40 70l5 14 14 5-14 5-5 14-5-14-14-5 14-5z" fill="{O}"/>
  <path class="st__spark st__spark--b" d="M452 170l3.5 9 9 3.5-9 3.5-3.5 9-3.5-9-9-3.5 9-3.5z" fill="{OD}"/>''')

# ---- contact: paper plane
PLANE = _svg("art art--plane", "0 0 180 140", f'''
  <path class="map__arc" d="M8 120C40 130 66 96 92 84" style="animation-delay:0s"/>
  <g class="map__fl"><path d="M164 14 30 66l40 14 14 36 22-26 34 24z" fill="{O}"/><path d="M164 14 70 80l14 36 6-30z" fill="{OD}"/><path d="M164 14 90 86l-6 30" fill="none" stroke="{W}" stroke-opacity=".6" stroke-width="2"/></g>''')
