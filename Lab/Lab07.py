phrase = input("Enter a string: ")

def replaceCons(phrase):
    newPhrase = ""
    phrase = phrase.upper()
    print("Old String: ", phrase)
    consonantList = 'BCDFGHJKLMNPQRSTVWXYZ'
    consonantCount = 0
    phrase = phrase[1:len(phrase)-1]
    for i in range(len(phrase)):
        if phrase[i] in consonantList:
            newPhrase = newPhrase + "*"
            consonantCount += 1
        else:
            newPhrase = newPhrase + phrase[i]
    newPhrase = newPhrase.upper()
    print("New String: ", newPhrase)
    print("Number of consonants: ", consonantCount)
    
replaceCons(phrase)