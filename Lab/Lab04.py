firstNum = int(input("Enter an odd number"))
secondNum = int(input("Enter another number: "))

def allNums(a, b):
    print("All numbers: ")
    for x in range(a, b+1):
        print(x, end = " ")
    print(" ")

def oddNums(a, b):
    print("All odd numbers: ")
    for x in range(a, b+1):
        if ((x % 2) != 0):
            print(x, end = " ")
    print(" ")
    
def evenNums(a, b):
    print("Sum of all even numbers: ")
    sum = 0
    for x in range(a, b+1):
        if ((x % 2) == 0):
            sum += x
    print(sum)
            
def oddSum(a, b):
    print("Sum of the square of all odd numbers: ")
    sum = 0
    for x in range(a, b+1):
        if ((x % 2) != 0):
            sum += (x ** 2)
    print(sum)
    
allNums(firstNum, secondNum)
oddNums(firstNum, secondNum)
evenNums(firstNum, secondNum)
oddSum(firstNum, secondNum)