#  pip import install pillow
#  pip install pyzbar

from PIL import Image
from pyzbar.pyzbar import decode

read = decode(Image.oprn('qrcode.png'))
print(read[0].data)