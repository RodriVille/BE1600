import random as r
def three_heads():
    headInARowCount = 0
    while headInARowCount < 3:
        coin = r.randint(1,2)
        if coin == 1:
            print("H", end = " ")
            headInARowCount += 1
        else:
            print("T", end = " ")
            headInARowCount = 0
    print("")
    print("Three heads in a row!")
three_heads()