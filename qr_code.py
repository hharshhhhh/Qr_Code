import qrcode as qr
from qrcode.image.pil import PilImage

img: PilImage = qr.make("https://github.com/hharshhhhh")
img.save("github_profile.png")
