aCount = float(input("Enter count of A seats: "))
bCount = float(input("Enter count of B seats: "))
cCount = float(input("Enter count of C seats: "))

def seatIncome(a, b, c):
    aIncome = a * 15
    bIncome = b * 12
    cIncome = c * 9
    total = aIncome + bIncome + cIncome
    print("Income from class A seats: ", aIncome)
    print("Income from class B seats: ", bIncome)
    print("Income from class C seats: ", cIncome)
    print("Total income: ", total)
    
seatIncome(aCount, bCount, cCount)

