"""Make a 9:16 story image from a 1080x1350 post: python3 story_image.py post.jpg out.jpg"""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
F = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
p = Image.open(sys.argv[1]).convert("RGB")
bg = Image.new("RGB", (1080, 1920), (11, 27, 46)); glow = Image.new("RGB", (1080, 1920), (11, 27, 46)); d = ImageDraw.Draw(glow)
d.ellipse((500, -300, 1500, 700), fill=(14, 110, 130)); d.ellipse((-500, 1300, 500, 2300), fill=(16, 70, 150))
bg = Image.blend(bg, glow.filter(ImageFilter.GaussianBlur(180)), 0.8)
card = p.resize((920, 1150), Image.LANCZOS); mask = Image.new("L", card.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, 919, 1149), 40, fill=255)
sh = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((80, 400, 1000, 1550), 40, fill=(0, 0, 0, 150))
bg = Image.alpha_composite(bg.convert("RGBA"), sh.filter(ImageFilter.GaussianBlur(30))).convert("RGB"); bg.paste(card, (80, 360), mask)
ImageDraw.Draw(bg).text((540, 260), "New post", font=ImageFont.truetype(F, 60), fill=(255, 255, 255), anchor="mm")
bg.save(sys.argv[2], quality=92)
