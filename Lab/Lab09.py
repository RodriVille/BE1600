import random as r
k = r.randint(2, 10)
print(k)
nums = []
for i in range(k):
    print("Enter a value", (i+1) , ": ", end="")
    num = int(input())
    nums.append(num)
def collapse(list):
    collapseNums = []
    for i in range(0,len(list), 2):
        if (len(list)%2 == 0):
            collapseNums.append(list[i] + list[i+1])
        else:
            if i == (len(list)-1):
                continue
            collapseNums.append(list[i] + list[i+1])
    print("Old List: ", list)
    print("Collapse List: ", collapseNums)
collapse(nums)