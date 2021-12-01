def substitutionDecrypt(msg, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    msg = msg.lower()
    plain = ""
    for i in msg:
        if i != ' ':
            plain += alphabet[key.find(i)]
        else:
            plain += ' '
    print("CipherText:", msg)
    print("PlainText:", plain)
substitutionDecrypt("gsv jfrxp yildm ulc", "zyxwvutsrqponmlkjihgfedcba")