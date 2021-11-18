ogList = sorted(['be', 'be', 'is', 'not', 'or', 'question', 'that', 'the', 'to', 'to'])
print("original list: ", ogList)
def remove_duplicates(list):
    checkList = []
    for i in list:
        if i not in checkList:
            checkList.append(i)
        else:
            continue
    print("list after removing dublicates: ", checkList)
remove_duplicates(ogList)