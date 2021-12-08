import math

file = open('data.txt', 'r')
file = file.readlines()

data = [[float(i.split()[0]), float(i.split()[1])] for i in file]

dists = []

for i in data:
    point = []
    for j in data:
        c = round(math.sqrt( ((i[0] - j[0])**2) + ((i[1] - j[1])**2)), 2)
        text = "{0:6s}".format(str(c))
        point.append(text)
    dists.append(point)

dists.insert(0, ['       P1', '    P2', '    P3', '    P4','    P5', '    P6', '    P7', '    P8'])
for i in range(len(dists)):
    num = i
    if num == 0:
        print("0")
    else:
        print("P{0:6s}".format(str(num)), end = '')
    for j in range(len(dists[i])):
        print(dists[i][j], end = ' ')
    print('')
        