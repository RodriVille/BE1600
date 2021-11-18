import string
userFile = input("Enter file name: ")
words = open("Lecture/Assignment04/" + userFile, 'r')
wordsUnedited = [i for i in words]
wordsNoPucntuation = [i.translate(str.maketrans('', '', string.punctuation))[:-1] for i in wordsUnedited]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dict = {}
for i in alphabet:
    count = 0
    for j in wordsNoPucntuation:
        count += (j.lower()).count(i)
    dict[i] = count
print("Letter\tCount")
for i in dict:
    print(i, "\t",dict[i])
userFile.close()