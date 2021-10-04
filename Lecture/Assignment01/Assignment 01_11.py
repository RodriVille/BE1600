
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

def nums(a, b):
    sum = 0
    if(a < b):
        for x in range (a, b + 1):
            print(x, end = " ")
            sum += x
    else:
        for x in range (b, a + 1):
            print(x, end = " ")
            sum += x
    print("")
    print("Sum of numbers", sum)
    
nums(a, b)