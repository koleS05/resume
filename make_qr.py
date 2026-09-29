# Usage: pip install "qrcode[pil]" && python make_qr.py https://YOURUSER.github.io/REPO/
# Outputs resume_qr.png (print at >= 2x2 cm) and resume_qr.svg. Error correction Q.
import sys
import qrcode
import qrcode.image.svg
from qrcode.constants import ERROR_CORRECT_Q

url = sys.argv[1]
qr = qrcode.QRCode(error_correction=ERROR_CORRECT_Q, box_size=20, border=4)
qr.add_data(url)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save("resume_qr.png")
qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage,
            error_correction=ERROR_CORRECT_Q).save("resume_qr.svg")
print("Saved resume_qr.png and resume_qr.svg for", url)
