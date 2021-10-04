import math

radius = float(input("Enter the raduis of a sphere: "))

def sphere_volume(r):
    vol = 4/3 * math.pi * (r ** 3)
    print(vol)
    
sphere_volume(radius)