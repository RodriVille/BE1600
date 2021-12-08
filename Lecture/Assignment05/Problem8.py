yrs = int(input("Enter the number of years: "))
months = yrs * 12
totalRain = 0

for year in range(yrs):
    print("For year", year + 1)
    for month in range(12):
        dis = month + 1
        dis1 = "Enter the rainfall amount for the month " + str(dis) + ": "
        rain = float(input(dis1))
        totalRain += rain
        
print("For", months, "months")
print("Total rainfall: ", totalRain)
print("Average monthly rainfall: ", round(totalRain/months, 2), "inches")