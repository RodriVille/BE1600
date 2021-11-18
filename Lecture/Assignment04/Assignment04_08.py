def print_average():
    numList = []
    userInput = 1
    running = True
    while (running == True):
        userInput = int(input("Type a number: "))
        if userInput > 0:
            numList.append(userInput)
        else:
            running = False
    try:
        average = sum(numList)/len(numList)
        print("Average is: ", average)
    except:
        print("Average is: 0")
print_average()