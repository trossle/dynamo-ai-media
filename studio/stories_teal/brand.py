import pathlib, re
S = pathlib.Path(__file__).parent
LOGO_SVG = (S / "logo.svg").read_text()
GRAD = "linear-gradient(135deg,#12D8D0 0%,#0BB2E0 45%,#1670E0 100%)"
INK, CHAR, CHAR2 = "#0B1B2E", "#13263B", "#1B3149"
WARM, CARD = "#EEF8FB", "#E3F0F5"
G1, G2, G3, G4 = "#2A3B4D", "#4C5F73", "#7F93A8", "#B9C7D4"
SUN, AMBER, ORANGE = "#12D8D0", "#12D8D0", "#1670E0"

def logo(w, uid="a", mono=None):
    """Logo SVG at width w. mono=colour for a flat version."""
    s = LOGO_SVG.replace('id="dg"', f'id="dg{uid}"').replace('url(#dg)', mono if mono else f'url(#dg{uid})')
    h = round(w * 626 / 678)
    return s.replace('<svg ', f'<svg width="{w}" height="{h}" ', 1)

WORD_D = (S / "dynamo_word_path.txt").read_text()
def dword(h, color=INK):
    """DYNAMO lettering from the Dynamo India logo, h px tall (cap height)."""
    return (f'<svg width="{h * 6.9235:.1f}" height="{h}" viewBox="7218.78 5548.24 9625.19 1390.23" style="display:block;flex-shrink:0">'
            f'<path fill="{color}" d="{WORD_D}"/></svg>')

def wordmark(size=28, dark=False, uid="w"):
    tx = "#FFFFFF" if dark else INK
    return (f'<div style="display:flex;align-items:center;gap:{round(size*.55)}px">{logo(round(size*1.9), uid)}'
            f'<div style="display:flex;align-items:center;gap:{round(size*.45)}px">{dword(round(size*.74), tx)}'
            f'<span style="font-size:{size}px;font-weight:700;letter-spacing:{round(size*.2)}px;line-height:1;color:{G3}">AI</span></div></div>')

GT = f"background:{GRAD};-webkit-background-clip:text;background-clip:text;color:transparent"
