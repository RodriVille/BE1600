alpha = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]

print("Part A")
for i in alpha:
    for j in i:
        print(j , end = ' ')
    print('')
    
print("Part B")
for i in range(len(alpha)):
    for j in range(len(alpha[i])):
        if i == 0:
            alpha[i][j] = 1
        else:
            alpha[i][j] = 3
for i in alpha:
    for j in i:
        print(j , end = ' ')
    print('')
    
print("Part C")
for i in range(len(alpha)):
    for j in range(len(alpha[i])):
        alpha[i][j] = (2**(j + 1))
for i in alpha:
    for j in i:
        print(j , end = ' ')
    print('')