import random as r

nums = []

for i in range(5):
    randNum = r.randint(0,10)
    nums.append(randNum)
    
def listEdit(list):
    print("Old list: ", list)
    firstNum = list[0]
    lastNum = list[len(list) - 1]
    swappedList = list
    swappedList[0] = lastNum
    swappedList[len(swappedList)-1] = firstNum
    print("New List after swapping first and last elements of Old List: ", swappedList)
    list.reverse()
    print("After reversing New List elements: ", list)

listEdit(nums)