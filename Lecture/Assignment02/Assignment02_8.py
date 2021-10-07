phrase = input("Enter a word of phrase: ")

def word_count(phrase):
    
    wordList = []
    start = 0
    end = 0
    for x in range(0, len(phrase)):
        if ((phrase[x] != " ") and (phrase[x-1] == " ")):
            start = x
        elif(phrase[x] == " "):
            if(x == 0):
                continue
            elif(phrase[(x-1)] == " "):
                continue
            end = x
            wordList.append(phrase[start:end])
        elif(x == len(phrase)-1):
            end = x + 1
            wordList.append(phrase[start:end])
    print(wordList)
    print("This phrase has", len(wordList), "words")
            
word_count(phrase)