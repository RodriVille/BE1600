print("First Nested Loop")
halfWay = True
for row in range(15):
    if row < 8:
        for i in range(row):
            print("*", end = "")
    else:
        if halfWay == True:
            print("\nSecond Nested Loop\n")
            halfWay = False
        for i in range((15-row), 0, -1):
            print("*", end = "")
            
    print("")