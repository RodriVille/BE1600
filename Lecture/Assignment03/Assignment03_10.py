dict = {'a':15 , 'c':35, 'b':10}
print("keys: ", end="")
for i in dict:
    print(i, end=" ")
print("")
print("Values: ", end="")
for i in dict:
    print(dict[i], end=" ")
print("")
print("Key-Value pairs")
for i in dict:
    print(i, dict[i])
print("Key-Value pairs sorted by key")
for i in sorted(dict):
    print(i, dict[i])
print("Key-Value pairs sorted by value")
for i in sorted(list(dict.values())):
    print(list(dict.keys())[list(dict.values()).index(i)], i)