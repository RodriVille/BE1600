word = input("Enter a string: ")

def checkLetters(word):
    vowels = 0
    consonants = 0
    vowelList = ['a', 'e', 'i', 'o', 'u']
    consonantList = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    for x in vowelList:
        vowels += word.count(x)
    for x in consonantList:
        consonants += word.count(x)
    
    print("The string you entered has", vowels, "and", consonants, "consonants")
    
checkLetters(word)