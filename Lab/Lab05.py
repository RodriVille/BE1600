days = int(input("Ente the number of days: "))

def calculation(days):
    print("Days         Pennies")
    print("--------------------")
    money = .01
    sum = 0
    for x in range(1, days + 1):
        print(x, "           ", money)
        sum += money
        money = money * 2
    print("The total salary for", days, "days is: ", round(sum, 2))
    
calculation(days)