from cImage import *

def editImg(pic, scale):
    
    old = FileImage(pic)
    old = FileImage(pic)
    w = old.getw()
    h = old.geth()
    
    window = ImageWin("Scale Image", w * scale, h)
    emptyIm = EmptyImage(w * scale, h)
    
    for y in range(h):
        for x in range(w * scale):
            pixel = old.getPixel((x//2), y)
            emptyIm.setPixel(x, y, pixel)
    
    emptyIm.draw(window)
    window.exitOnClick()
    
editImg("butterfly.gif", 2)