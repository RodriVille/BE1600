def getData():
    temps = []
    for row in range(2):
        rows = []
        if row == 0:
            print("Enter the highest temperatures for each month of the year")
        elif row == 1:
            print("Enter the lowest temperatures for each month of the year")
        for col in range(12):
            print("Month", col + 1, ": ", end = '')
            user = float(input(''))
            rows.append(user)
        temps.append(rows)
    return temps

def avgHigh(temps):
    highs = 0
    for i in range(12):
        highs += temps[0][i]
    return highs/12

def avgLow(temps):
    lows = 0
    for i in range(12):
        lows += temps[1][i]
    return lows/12

def highTemp(temps):
    return max(temps[0])

def lowTemp(temps):
    return min(temps[1])


temps = getData()
print("List of the highest and lowest temperatures for each month of the year")
for i in range(len(temps)):
    for j in range(len(temps[i])):
        print(temps[i][j], end = " ")
    print(' ')
print("Average high temperature for the year: ", avgHigh(temps))
print("Average low temperature for the year: ", avgLow(temps))
print("Highest high temperature for the year: ", highTemp(temps))
print("Lowest low temperature for the year: ", lowTemp(temps))