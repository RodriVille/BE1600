books = open("books.txt", 'r')
dict = {}
for i in books:
    line = i.split(",")
    name = line[1][:-1]
    title = line[0]
    if name not in dict:
        dict[name] = [title]
    else:
        dict[name].append(title)
for i in dict:
    print(i, dict[i])
books.close()