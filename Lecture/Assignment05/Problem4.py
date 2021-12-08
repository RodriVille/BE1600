from cImage import *

def changePixel(pix):
    r = pix.getRed()
    g = pix.getGreen()
    b = pix.getBlue()
    average = (r + g + b)/3
    if average > 255/2:
        pixel = Pixel(255, 255, 255)
    else:
        pixel = Pixel(0, 0, 0)
    return pixel


def makeBlackAndWhite(img):
        
    image = FileImage(img)
    image = FileImage(img)
    w = image.getWidth()
    h = image.getHeight()
        
    win = ImageWin("Scale Image", w * 2, h)
    emptyIm = EmptyImage(w * 2, h)
    for y in range(h):
        for x in range(w):
            imgPixel = image.getPixel(x, y)
            emptyIm.setPixel(x, y, imgPixel)
            emptyIm.setPixel(w + x, y, changePixel(imgPixel))
    
    emptyIm.draw(win)
    win.exitOnClick()
            
makeBlackAndWhite("butterfly.gif")