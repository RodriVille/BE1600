user = input("Enter phrase to encode: ")

def encrypt(user):
    print("PlainText:", user)
    railOne = ""
    railTwo = ""
    railThree = ""
    for i in range(0, len(user), 3):
        try:
            railOne = railOne + user[i]
            railTwo = railTwo + user[i + 1]
            railThree = railThree + user[i + 2]
        except:
            continue
    print(railOne, "\n", railTwo, "\n", railThree)
    cipher = railOne + railTwo + railThree
    print("CipherText:", cipher)
    
encrypt(user)