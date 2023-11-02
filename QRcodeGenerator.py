import pyqrcode

link = "https://www.youtube.com/@niveshdarpan"

img = pyqrcode.create(link)
img.svg('NiveshDarpan Channel.svg',scale = 10)