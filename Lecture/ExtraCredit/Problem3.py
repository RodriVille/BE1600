running = True
while running == True:
    year = int(input("Enter a year in the range 1903-2020: "))
    worldSeries = open('WorldSeries.txt', 'r')
    dict = {}
    lines = worldSeries.readlines()
    for i in lines:
        i = i[:-1]
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    if year >= 1903:
        print("The team that won the world series in", year, "is", lines[year-1903][:-1])
        print("They won the world series", dict[lines[year - 1903][:-1]], 'times')
    else:
        print("The year", year, "is not included in our database")
    cont = input("Do you want to continue, type 'y' for yes, 'n' for No: ")
    if cont == 'n':
        running = False