widthA = float(input("Enter the width for rectange A: "))
heightA = float(input("Enter the height for rectange A: "))
widthB = float(input("Enter the width for rectange B: "))
heightB = float(input("Enter the height for rectange B: "))

areaA = widthA * heightA
areaB = widthB * heightB

if (areaA > areaB):
    print("Area A is greater than area B")
elif (areaA < areaB):
    print("Area B is greater than area A")
else:
    print("Area A is equal to area B")