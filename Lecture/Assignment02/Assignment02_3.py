
numerator = 1
denominator = 30

sum = 0

for x in range(30):
    div = numerator/denominator
    numerator += 1
    denominator -= 1
    sum = sum + div
    
print(sum)    