running = True
while running == True:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    sum = num1 + num2
    print("The sum of the numbers you entered is:", sum)
    user = input("Do you want to do that again? (y/n) ")
    if user == "y":
        continue
    else:
        running = False