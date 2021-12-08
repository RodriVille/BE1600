from cImage import *

#This is not the most efficient algorithm so its going to take a bit to load

def smooth(img, x, y):
    image = FileImage(img)
    localPixRed, localPixGreen, localPixBlue = image.getPixel(x, y).getRed(), image.getPixel(x, y).getGreen(), image.getPixel(x, y).getBlue()
    try:
        pixRed1, pixGreen1, pixBlue1 = image.getPixel(x + 1, y).getRed(), image.getPixel(x + 1, y).getGreen(), image.getPixel(x + 1, y).getBlue()
        pixRed2, pixGreen2, pixBlue2 = image.getPixel(x - 1, y).getRed(), image.getPixel(x - 1, y).getGreen(), image.getPixel(x - 1, y).getBlue()
        pixRed3, pixGreen3, pixBlue3 = image.getPixel(x, y + 1).getRed(), image.getPixel(x, y + 1).getGreen(), image.getPixel(x, y + 1).getBlue()
        pixRed4, pixGreen4, pixBlue4 = image.getPixel(x, y - 1).getRed(), image.getPixel(x, y - 1).getGreen(), image.getPixel(x, y - 1).getBlue()
        avgRed = (localPixRed + pixRed1 + pixRed2 + pixRed3 + pixRed4)//5
        avgBlue = (localPixBlue + pixBlue1 + pixBlue2 + pixBlue3 + pixBlue4)//5
        avgGreen = (localPixGreen + pixGreen1 + pixGreen2 + pixGreen3 + pixGreen4)//5
        print(avgRed, avgGreen, avgBlue)
        return Pixel(avgRed, avgGreen, avgBlue)
    
    except:
        return image.getPixel(x, y)
    
    
def imageEdit(img):
        
    oldImg = FileImage(img)
    width = oldImg.getWidth()
    height = oldImg.getHeight()
        
    window = ImageWin("Scale Image", width * 2, height)
    emptyIm = EmptyImage(width * 2, height)
    for y in range(height):
        for x in range(width):
            oldPix = oldImg.getPixel(x, y)
            emptyIm.setPixel(x, y, oldPix)
            emptyIm.setPixel(width + x, y, smooth(img, x, y))
    
    emptyIm.draw(window)
    window.exitOnClick()
            
imageEdit("pic.gif")