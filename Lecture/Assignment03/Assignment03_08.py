ogList = ['how', 'are', 'you?']
def double_list(list):
    newList = []
    for i in list:
        for l in range(2):
            newList.append(i)
    print("original list: ", list)
    print("double list: ", newList)
double_list(ogList)