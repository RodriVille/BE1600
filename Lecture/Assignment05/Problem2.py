from cImage import *

def red(pix):
    newRed = pix.getRed() + ((255-pix.getRed())//2)
    newPix = Pixel(newRed, pix.getGreen(), pix.getBlue())
    return newPix

def makeRed(img):
    oldImg = FileImage(img)
    width = oldImg.getWidth()
    height = oldImg.getHeight()
    
    window = ImageWin("Red Image", width, height)
    oldImg.draw(window)
    emptyIm = EmptyImage(width, height)
    
    for y in range(height):
        for x in range(width):
            oldPix = oldImg.getPixel(x, y)
            newPix = red(oldPix)
            emptyIm.setPixel(x, y, newPix)
    
    emptyIm.draw(window)
    window.exitOnClick()

makeRed("butterfly.gif")