import csv

file = open('riskfactors.csv', 'r')
reader = csv.reader(file)
data = [i for i in reader]
data = data[5:]
def dataLook(data):
    states = [i[0] for i in data][1:]
    headers = data[0]
    maxes = []
    lines = {}
    for column in range(len(headers)):
        vals = []
        if column == 0:
            continue
        for row in range(len(data)):
            if row == 0:
                continue
            if "N/A" not in data[row][column] and "%" not in data[row][column]:
                vals.append(float(data[row][column]))
            elif "%" in data[row][column]:
                vals.append(float(''.join([i for i in data[row][column] if i != "%"])))
            else:
                vals.append(0)
        lines["{0:35s}".format(headers[column])] = "{0:25s}{1:10s}{2:25s}{3:5s}".format(":  " + states[vals.index(min(vals))], str(min(vals)), states[vals.index(max(vals))], str(max(vals)))
    printData(lines)
def printData(lines):
    print("{0:40s}{1:35s}{2:35s}".format("Indicator", "Min", "Max"))
    print(105*"-")
    for i in lines:
        print(i, lines[i])
dataLook(data)