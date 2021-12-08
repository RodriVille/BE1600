import math
from cImage import *

window = ImageWin("Image", 300, 300)
img = EmptyImage(300, 300)
bluePixel = Pixel(0, 0, 255)

for i in range(360):
    img.setPixel(int(math.sin(i) * 50) + 150, int(math.cos(i) * 50) + 150, bluePixel)
    
img.draw(window)
window.exitOnClick()