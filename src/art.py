"""Decorative inline SVG illustrations (no text, so no i18n). Flat fills only: no ids, so they can repeat on a page."""

O, OD, OS, OT, INK, W = "#FF6B00", "#E04E00", "#FFE6D1", "#FFF5EC", "#1E1611", "#FFFFFF"

def _svg(cls, vb, inner, extra=""):
    return f'<svg class="{cls}" viewBox="{vb}" aria-hidden="true" focusable="false"{extra}>{inner}</svg>'

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


# ---- service tiles: one animated illustration each. Colours come from CSS vars set on .tile__art
def _a(inner): return f'<svg class="tile__art" viewBox="0 0 160 130" aria-hidden="true" focusable="false">{inner}</svg>'

SERVICE_ART = {
"youtube-mcn": _a("""
  <rect class="a3" x="6" y="14" width="108" height="76" rx="14"/><rect class="a1" x="13" y="21" width="94" height="60" rx="9"/>
  <circle class="a0 an-pulse" cx="60" cy="51" r="17"/><path class="a1" d="M54 42v18l16-9z"/>
  <rect class="a3" x="34" y="94" width="52" height="7" rx="3.5"/>
  <rect class="a2 an-bar" x="122" y="82" width="11" height="30" rx="4"/><rect class="a1 an-bar an-d1" x="137" y="62" width="11" height="50" rx="4"/>
  <circle class="a2 an-float" cx="138" cy="34" r="10"/><path class="a0 an-float" d="M138 29l1.8 3.7 4 .6-2.9 2.8.7 4-3.6-1.9-3.6 1.9.7-4-2.9-2.8 4-.6z"/>"""),
"music-distribution": _a("""
  <circle class="a3" cx="80" cy="65" r="36"/><ellipse class="s1" cx="80" cy="65" rx="15" ry="36" stroke-width="3"/><ellipse class="s1" cx="80" cy="65" rx="36" ry="13" stroke-width="3"/>
  <circle class="s1" cx="80" cy="65" r="36" stroke-width="3"/>
  <g class="an-orbit"><circle class="s1" cx="80" cy="65" r="58" stroke-width="2" stroke-dasharray="3 7"/><circle class="a1" cx="138" cy="65" r="8"/></g>
  <g class="an-orbit an-orbit--r"><circle class="a2" cx="22" cy="65" r="6"/></g>
  <circle class="a1" cx="80" cy="65" r="17"/><path class="s0" d="M76 72V57l10-3v14" stroke-width="3"/><circle class="a0" cx="73" cy="73" r="4"/><circle class="a0" cx="83" cy="69" r="4"/>"""),
"music-publishing": _a("""
  <rect class="a3" x="34" y="8" width="92" height="114" rx="12"/>
  <path class="s2" d="M46 32h68M46 38h68M46 44h68M46 50h68M46 56h68M46 76h68M46 82h68M46 88h68M46 94h68M46 100h68" stroke-width="1.6"/>
  <g class="an-note"><ellipse class="a1" cx="62" cy="52" rx="6" ry="4.6"/><path class="s1" d="M67 52V28" stroke-width="2.6"/></g>
  <g class="an-note an-d1"><ellipse class="a2" cx="88" cy="46" rx="6" ry="4.6"/><path class="s2" d="M93 46V24" stroke-width="2.6"/></g>
  <g class="an-note an-d2"><ellipse class="a1" cx="76" cy="96" rx="6" ry="4.6"/><path class="s1" d="M81 96V72" stroke-width="2.6"/></g>
  <g class="an-note an-d3"><ellipse class="a4" cx="102" cy="90" rx="6" ry="4.6"/><path class="s4" d="M107 90V68" stroke-width="2.6"/></g>
  <rect class="a2 an-pen" x="116" y="86" width="9" height="34" rx="4" transform="rotate(35 120 100)"/>"""),
"vevo": _a("""
  <rect class="a4" x="8" y="6" width="144" height="74" rx="13"/>
  <g class="an-scan"><rect class="a1" x="8" y="6" width="26" height="74" opacity=".3"/></g>
  <circle class="s1 an-ping" cx="80" cy="40" r="22" stroke-width="2.5"/><circle class="a1 an-pulse" cx="80" cy="40" r="19"/><path class="a0" d="M74 30v20l17-10z"/>
  <rect class="a3" x="20" y="68" width="120" height="5" rx="2.5" opacity=".35"/><rect class="a1 an-load" x="20" y="68" width="120" height="5" rx="2.5"/>
  <g class="an-vevo" transform="translate(4 0)">
    <path class="s1 an-note" d="M10 90l12 29 12-29" stroke-width="7"/>
    <path class="s2 an-note an-d1" d="M46 90v29M46 90h17M46 104h14M46 119h17" stroke-width="6.5"/>
    <path class="s1 an-note an-d2" d="M74 90l12 29 12-29" stroke-width="7"/>
    <ellipse class="s2 an-note an-d3" cx="125" cy="104.5" rx="11" ry="14" stroke-width="6.5"/>
  </g>"""),
"facebook": _a("""
  <rect class="a3" x="10" y="12" width="104" height="106" rx="16"/><rect class="a1" x="17" y="19" width="90" height="36" rx="10"/>
  <circle class="a0" cx="40" cy="58" r="15"/><circle class="a2" cx="40" cy="58" r="11"/>
  <rect class="a2" x="60" y="62" width="40" height="7" rx="3.5"/><rect class="a1" x="22" y="84" width="80" height="7" rx="3.5" opacity=".6"/><rect class="a1" x="22" y="97" width="54" height="7" rx="3.5" opacity=".6"/>
  <g class="an-pop"><circle class="a1" cx="130" cy="42" r="22"/><rect class="a0" x="119" y="44" width="7" height="16" rx="2"/><path class="a0" d="M129 44l5-12c3 0 6 2 5 6l-1.5 5h8c3 0 4 3 3 6l-3 8c-1 2-2 3-4 3h-12z"/></g>
  <g class="an-float"><rect class="a2" x="112" y="84" width="44" height="28" rx="12"/><circle class="a0 an-dot" cx="124" cy="98" r="3"/><circle class="a0 an-dot an-d1" cx="134" cy="98" r="3"/><circle class="a0 an-dot an-d2" cx="144" cy="98" r="3"/></g>"""),
"white-label": _a("""
  <g class="an-fan"><rect class="a3" x="34" y="22" width="86" height="64" rx="13" transform="rotate(-14 77 54)"/><rect class="a2" x="34" y="26" width="86" height="64" rx="13" transform="rotate(-5 77 58)" opacity=".85"/></g>
  <rect class="a1" x="36" y="30" width="88" height="66" rx="13"/><circle class="a0" cx="58" cy="52" r="10"/><rect class="a0" x="76" y="46" width="36" height="6" rx="3"/><rect class="a0" x="76" y="58" width="24" height="6" rx="3" opacity=".7"/><rect class="a0" x="48" y="76" width="64" height="6" rx="3" opacity=".55"/>
  <circle class="a1 an-swatch" cx="48" cy="114" r="8"/><circle class="a2 an-swatch an-d1" cx="72" cy="114" r="8"/><circle class="a4 an-swatch an-d2" cx="96" cy="114" r="8"/><circle class="a3 an-swatch an-d3" cx="120" cy="114" r="8"/>
  <path class="a1 an-spark" d="M140 18l3 8 8 3-8 3-3 8-3-8-8-3 8-3z"/>"""),
"api": _a("""
  <path class="s1" d="M52 24c-13 0-13 7-13 16v10c0 7-5 11-11 11 6 0 11 4 11 11v10c0 9 0 16 13 16" stroke-width="7"/>
  <path class="s1" d="M108 24c13 0 13 7 13 16v10c0 7 5 11 11 11-6 0-11 4-11 11v10c0 9 0 16-13 16" stroke-width="7"/>
  <circle class="a2 an-dot" cx="64" cy="65" r="6"/><circle class="a1 an-dot an-d1" cx="80" cy="65" r="6"/><circle class="a4 an-dot an-d2" cx="96" cy="65" r="6"/>
  <rect class="a3" x="28" y="108" width="104" height="8" rx="4"/><rect class="a1 an-load" x="28" y="108" width="104" height="8" rx="4"/>"""),
"copyright": _a("""
  <circle class="s1 an-ping" cx="80" cy="64" r="48" stroke-width="2"/>
  <path class="a3 s1" d="M80 8l42 14v32c0 30-19 48-42 58-23-10-42-28-42-58V22z" stroke-width="5"/>
  <circle class="s1" cx="80" cy="60" r="20" stroke-width="4"/><path class="s1" d="M88 51a12 12 0 1 0 0 18" stroke-width="4.5"/>
  <circle class="a1 an-pop" cx="126" cy="104" r="16"/><path class="s0 an-check" d="M118 104l6 6 11-12" stroke-width="4.5"/>"""),
"video-production": _a("""
  <rect class="a4" x="22" y="56" width="116" height="64" rx="10"/>
  <g class="an-clap"><rect class="a1" x="22" y="30" width="116" height="24" rx="6"/>
  <path class="a0" d="M36 30h16L40 54H24zM64 30h16L68 54H52zM92 30h16L96 54H80zM120 30h14L122 54h-14z"/></g>
  <path class="a1 an-pulse" d="M70 76v28l26-14z"/>
  <path class="a2 an-spark" d="M142 12l3 8 8 3-8 3-3 8-3-8-8-3 8-3z"/><circle class="a1 an-float" cx="14" cy="44" r="5"/>"""),
}
