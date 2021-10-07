import math

def inCircle():
    radius = float(input("Enter the radius of a circle: "))
    xCoord = float(input("Enter an x coordinate: "))
    yCoord = float(input("Enter a y coordinate: "))

    dist = math.sqrt((xCoord ** 2 + yCoord**2))

    if (dist <= radius):
        print("Point (", xCoord, ",", yCoord, ") is within the radius of", radius)
    else: 
        print("Point (", xCoord, ",", yCoord, ") is not within the radius of", radius)

inCircle()