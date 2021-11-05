import random as rand
n = rand.randint(2, 10)
print(n)
numbers = []
for i in range(n):
    print("Enter a value", (i+1) , ": ", end="")
    num = int(input())
    numbers.append(num)
def collapse(list):
    collapseList = []
    for index in range(0,len(list), 2):
        if (len(list)%2 == 0):
            collapseList.append(list[index] + list[index+1])
        else:
            if i == (len(list)-1):
                collapseList.append(list[index])
                continue
            collapseList.append(list[index] + list[index+1])
    print("Old List: ", list)
    print("Collapse List: ", collapseList)
collapse(numbers)