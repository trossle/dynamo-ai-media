import re, math
MARK = open("/home/claude/carousel/mark_teal.svg").read(); WORD = open("/home/claude/carousel/word.svg").read()

def tower(cx, base, top, wb, wt, sc=1.0):
    """Striped lighthouse tower with lantern room. cx centre, base y, top y (of tower body)."""
    h = base - top
    bands = ""
    for i in range(6):
        y0 = top + h * i / 6; y1 = top + h * (i + 1) / 6
        w0 = wt + (wb - wt) * i / 6; w1 = wt + (wb - wt) * (i + 1) / 6
        col = "#E9EEF3" if i % 2 == 0 else "#C8364A"
        bands += f'<polygon points="{cx-w0/2},{y0} {cx+w0/2},{y0} {cx+w1/2},{y1} {cx-w1/2},{y1}" fill="{col}"/>'
    shade = f'<polygon points="{cx},{top} {cx+wt/2},{top} {cx+wb/2},{base} {cx},{base}" fill="#000" opacity=".22"/>'
    lw = wt * 1.25; lh = wt * 0.9
    lantern = (f'<rect x="{cx-lw/2-10}" y="{top-14}" width="{lw+20}" height="16" rx="4" fill="#1C2A3A"/>'
               f'<rect x="{cx-lw/2}" y="{top-14-lh}" width="{lw}" height="{lh}" fill="#FFE9A8" opacity=".95"/>'
               f'<circle cx="{cx}" cy="{top-14-lh/2}" r="{lw*0.9}" fill="url(#glow)"/>'
               + "".join(f'<rect x="{cx-lw/2+k*lw/4-2}" y="{top-14-lh}" width="4" height="{lh}" fill="#1C2A3A"/>' for k in range(5))
               + f'<polygon points="{cx-lw/2-8},{top-14-lh} {cx+lw/2+8},{top-14-lh} {cx},{top-14-lh-lw*0.6}" fill="#1C2A3A"/>')
    rock = f'<ellipse cx="{cx}" cy="{base+18}" rx="{wb*1.4}" ry="40" fill="#0A1626"/>'
    defs = '<defs><radialGradient id="glow"><stop offset="0" stop-color="#FFF6D0" stop-opacity=".9"/><stop offset="1" stop-color="#FFE6A0" stop-opacity="0"/></radialGradient></defs>'
    return defs + rock + bands + shade + lantern

def lantern_room():
    s = '<rect x="140" y="260" width="800" height="900" rx="30" fill="none" stroke="#1C2A3A" stroke-width="26"/>'
    s += "".join(f'<rect x="{140+k*200-8}" y="260" width="16" height="900" fill="#1C2A3A"/>' for k in range(5))
    s += '<rect x="140" y="700" width="800" height="16" fill="#1C2A3A"/>'
    s += '<rect x="420" y="750" width="240" height="40" rx="10" fill="#7A5A2C"/><rect x="455" y="790" width="170" height="260" rx="20" fill="#5B4120"/>'
    s += '<rect x="470" y="680" width="140" height="80" rx="16" fill="none" stroke="#B9C7D4" stroke-width="10" opacity=".7"/>'
    s += '<rect x="60" y="1150" width="960" height="40" fill="#0A1626"/>'
    return s

def keeper():
    return ('<path d="M150 70 C120 70 105 95 108 120 C110 145 128 165 150 165 C172 165 190 145 192 120 C195 95 180 70 150 70 Z" fill="#0A1626"/>'
            '<path d="M95 78 L205 78 L190 52 L110 52 Z" fill="#0A1626"/><rect x="88" y="74" width="124" height="12" rx="6" fill="#0A1626"/>'
            '<path d="M60 620 L80 260 C85 200 115 178 150 178 C185 178 215 200 220 260 L240 620 Z" fill="#0A1626"/>'
            '<path d="M80 270 L20 420 L48 432 L100 320 Z" fill="#0A1626"/>')

def xsect():
    s = '<polygon points="330,1780 750,1780 660,560 420,560" fill="#0E2236" stroke="#1F4060" stroke-width="10"/>'
    pts = [(540, 1700), (700, 1560), (380, 1420), (700, 1280), (400, 1140), (680, 1000), (430, 860), (640, 720), (540, 600)]
    s += '<polyline points="' + " ".join(f"{x},{y}" for x, y in pts) + '" fill="none" stroke="#2A5A80" stroke-width="16" stroke-dasharray="26 12" stroke-linecap="round"/>'
    s += '<rect x="430" y="420" width="220" height="140" fill="#FFE9A8" opacity=".9"/><polygon points="410,420 670,420 540,330" fill="#1C2A3A"/>'
    s += '<line x1="540" y1="560" x2="540" y2="1500" stroke="#9FB6CC" stroke-width="4" stroke-dasharray="8 8"/><rect x="515" y="1500" width="50" height="90" rx="8" fill="#9FB6CC"/>'
    return s

def gear(n=12, r=150, d=26):
    pts = []
    for i in range(n * 2):
        a = math.pi * i / n
        rr = r if i % 2 == 0 else r - d
        a0, a1 = a - math.pi / (n * 2) * 0.7, a + math.pi / (n * 2) * 0.7
        pts += [(rr * math.cos(a0), rr * math.sin(a0)), (rr * math.cos(a1), rr * math.sin(a1))]
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<polygon points="{p}" fill="#2A5A80"/><circle r="{r-60}" fill="#0E2236"/><circle r="26" fill="#3FE6F0"/>'
            + "".join(f'<rect x="-8" y="{-(r-60)}" width="16" height="{r-60}" fill="#2A5A80" transform="rotate({k*60})"/>' for k in range(6)))

def lens():
    s = '<circle r="290" fill="rgba(63,230,240,.06)" stroke="#3FE6F0" stroke-width="6"/>'
    for k in range(1, 9):
        s += f'<circle r="{k*32}" fill="none" stroke="rgba(200,240,255,{0.7-k*0.06})" stroke-width="{10-k*0.6}"/>'
    s += '<circle r="40" fill="#FFF3C4"/>'
    s += "".join(f'<rect x="-3" y="-290" width="6" height="580" fill="rgba(63,230,240,.35)" transform="rotate({k*45})"/>' for k in range(4))
    return s

def lamp():
    return ('<rect x="440" y="900" width="200" height="40" rx="10" fill="#7A8C9E"/><path d="M420 940 L660 940 L620 1180 L460 1180 Z" fill="#5E7183"/>'
            '<ellipse cx="540" cy="1180" rx="120" ry="24" fill="#3E5062"/><rect x="520" y="640" width="40" height="270" rx="6" fill="#D9E2EA" opacity=".35"/>'
            '<rect x="531" y="620" width="18" height="40" rx="4" fill="#2A1F14"/>')

def ship():
    return ('<path d="M20 120 L280 120 L240 170 L50 170 Z" fill="#0A1626"/><rect x="140" y="30" width="10" height="92" fill="#0A1626"/>'
            '<path d="M150 34 L150 112 L232 112 Z" fill="#CFE9F5"/><path d="M140 44 L140 112 L76 112 Z" fill="#9FB6CC"/>')

PH = '<svg width="54" height="54" viewBox="0 0 24 24"><path d="M5 4 H8.5 L10.5 9 L8.2 10.4 A11 11 0 0 0 13.6 15.8 L15 13.5 L20 15.5 V19 A2 2 0 0 1 18 21 A15 15 0 0 1 3 6 A2 2 0 0 1 5 4 Z" fill="#fff"/></svg>'
PH_DOWN = PH.replace('viewBox', 'style="transform:rotate(135deg)" viewBox')
PH_DARK = PH.replace('fill="#fff"', 'fill="#04263F"')
sh = ",".join(f"{x}px {y}px 0 #000" for x, y in [(6,0),(-6,0),(0,6),(0,-6),(4,4),(-4,4),(4,-4),(-4,-4),(6,3),(-6,3),(6,-3),(-6,-3),(3,6),(-3,6),(3,-6),(-3,-6)])
mark = re.sub(r'width="[\d.]+" height="[\d.]+"', 'width="230" height="212"', MARK, count=1)
markG = re.sub(r'width="[\d.]+" height="[\d.]+"', 'width="200" height="185"', MARK, count=1).replace('id="lgh"', 'id="lgh2"').replace('url(#lgh)', 'url(#lgh2)')
word = re.sub(r'width="[\d.]+" height="[\d.]+"', f'width="{round(64*9625.19/1390.23)}" height="64"', WORD, count=1).replace('fill="currentColor"', 'fill="#E8F4FA"')
s = open("reel.html").read()
rep = {"__TOWER_A__": tower(700, 1360, 640, 240, 150), "__TOWER_E__": tower(760, 1340, 760, 190, 120), "__LANTERN__": lantern_room(),
       "__KEEPER__": keeper(), "__XSECT__": xsect(), "__GEAR__": gear(), "__LENS__": lens(), "__LAMP__": lamp(), "__SHIP__": ship(),
       "__PH_DOWN__": PH_DOWN, "__PH_DARK__": PH_DARK, "__PH__": PH, "__SH__": sh, "__MARK_G__": markG, "__MARK__": mark, "__WORD__": word,
       "__TL__": open("timeline.json").read()}
for k, v in rep.items(): s = s.replace(k, v)
open("reel_built.html", "w").write(s); print("ok", "__" in s.split("<script>")[0])
