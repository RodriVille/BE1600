phrase = input("Enter a string: ")
dict={}
for i in phrase:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
print("The character that appears most frequently in the string is", list(dict.keys())[list(dict.values()).index(max(dict.values()))])