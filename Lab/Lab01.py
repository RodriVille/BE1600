import math

radius = float(input("Enter the radius of a circle: "))

diameter = radius * 2
circumference = radius * math.pi * 2
area = (radius ** 2) * math.pi

print("Circle radius: ", radius)
print("Diameter: ", diameter)
print("Circumference: ", round(circumference, 3))
print("Area: ", round(area, 3))