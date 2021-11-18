file = open("Lab/numbers.txt", 'r')
numList = []
for i in file:
    line = i.split()
    numList.append(int(line[1]))
negCount = 0
oddCount = 0
negativeNums = []
positiveNums = []
for i in numList:
    if i < 0:
        negCount += 1
        negativeNums.append(i)
    if i % 2 == 1:
        oddCount += 1
    if i > 0:
        positiveNums.append(i)
print("Negative count: ", negCount)
print("Odd count: ", oddCount)
print("Negative sum: ", sum(negativeNums))
print("Positive average: ", sum(positiveNums)/len(positiveNums))
file.close()