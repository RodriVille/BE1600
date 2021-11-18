import random as r
userSum = int(input("Desired dice sum: "))
def dice_sum(sum):
    num1 = r.randint(1, 6)
    num2 = r.randint(1, 6)
    sums = num1 + num2
    print(num1, "and", num2, "=", sums)
    if sums == sum:
        pass
    else:
        dice_sum(sum)
dice_sum(userSum)