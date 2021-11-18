numList = []
for i in range(10):
    num = int(input("Enter a number: "))
    numList.append(num)
print("Low: ", float(min(numList)), "\n",
      "High: ", float(max(numList)), "\n",
      "Total: ", float(sum(numList)), "\n",
      "Average: ", float(sum(numList))/len(numList))