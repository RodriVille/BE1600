from cImage import *

window = ImageWin("Image", 300, 300)
img = EmptyImage(300, 300)

red = Pixel(255, 0, 0)
green = Pixel(0, 255, 0)

for i in range(300):
    img.setPixel(150, i, green)
    img.setPixel(i, 150, green)
x, y = 150, 150
while x < 300 and y < 300:
    img.setPixel(x, y, red)
    x += 1
    y += 1

img.draw(window)
window.exitOnClick()