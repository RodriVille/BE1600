ogList = ['be', 'be', 'is', 'not', 'or', 'question', 'that', 'the', 'to', 'to']
print("original list: ", ogList)
checkList = []
for i in ogList:
    if i not in checkList:
        checkList.append(i)
    else:
        continue
print("list after removing dublicates: ", checkList)