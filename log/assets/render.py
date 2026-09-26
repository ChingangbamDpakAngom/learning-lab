"""Render a cheat-sheet HTML to a cropped JPEG next to it.

Usage: python render.py path/to/Topic-Cheat-Sheet.source.html
"""
import pathlib, subprocess, sys
from PIL import Image, ImageChops

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

src = pathlib.Path(sys.argv[1]).resolve()
png = src.with_suffix(".png")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--force-device-scale-factor=2", "--window-size=1600,3200",
                "--virtual-time-budget=2000", f"--screenshot={png}", src.as_uri()],
               check=True, capture_output=True)
im = Image.open(png).convert("RGB")
bg = Image.new("RGB", im.size, im.getpixel((5, im.height - 5)))
bottom = ImageChops.difference(im, bg).getbbox()[3]
out = src.with_name(src.name.replace(".source.html", ".jpg"))
im.crop((0, 0, im.width, min(im.height, bottom + 88))).save(out, quality=92, optimize=True, subsampling=0)
png.unlink()
print(out, im.width, bottom + 88)
