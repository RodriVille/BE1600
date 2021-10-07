import random as r

evens = 0
odds = 0

for x in range(100):
    num = r.randint(1, 100)
    if((num % 2) == 0):
        evens += 1
    else:
        odds += 1
        
print("Out of 100 random numbers", odds, "were odd, and", evens, "were even")