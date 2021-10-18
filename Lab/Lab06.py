import random as r

def sales():
    quantity = r.randint(1, 151)
    price = 25
    cost = price * quantity
    discount = 0
    if (quantity >= 10 and quantity <= 19):
        discount = .20
    elif (quantity >= 20 and quantity <= 49):
        discount = .30
    elif (quantity >= 50 and quantity <= 99):
        discount = .40
    elif (quantity >= 100):
        discount = .50
    costDiscount = cost * discount
    print("Numer of packages purchased: ", quantity)
    print("Discount Amount", costDiscount)
    print("Total Amount: ", (cost - costDiscount))
    
sales()