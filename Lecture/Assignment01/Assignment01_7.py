import math

area = float(input("Enter wall space in square feet: "))
galPrice = float(input("Enter paint price per gallon: "))

paintGal = math.ceil(area / 115)
labor = paintGal * 8
wagePrice = labor * 20
paintPrice = paintGal * galPrice
totalPrice = wagePrice + paintPrice

print("Gallons of paint:", paintGal)
print("Hours of labor:", labor)
print("Paint charges:", paintPrice)
print("Labor charges:", wagePrice)
print("Total cost:", totalPrice)
