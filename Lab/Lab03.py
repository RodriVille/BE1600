import math

xcoord = float(input("Enter the x coordinate of the center of the circle: "))
ycoord = float(input("Enter the y coordinate of the center of the circle: "))
xpoint = float(input("Enter the x coordinate of a point on the circle: "))
ypoint = float(input("Enter the y coordinate of a point on the circle: "))

def distance(a, b, c, d):
    return math.sqrt(((a - c) ** 2) + ((b - d) ** 2))

def circumference(r):
    return (2 * math.pi * r)

def radius(a, b, c, d):
    return distance(a, b, c, d)

print("Circle radius: ", distance(xcoord, ycoord, xpoint, ypoint))
print("Circle curcumferenec: ", circumference(radius(xcoord, ycoord, xpoint, ypoint)))
