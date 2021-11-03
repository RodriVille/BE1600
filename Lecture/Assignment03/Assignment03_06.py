numList = []
for i in range(10):
    num = int(input("Enter a number: "))
    numList.append(num)
print("Low: ", float(min(numList)))
print("High: ", float(max(numList)))
print("Total: ", float(sum(numList)))
print("Average: ", float(sum(numList))/len(numList))