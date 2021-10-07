word = input("Enter a word: ")
repetitions = int(input("Enter the number of repetitions: "))

def repl(word, reps):
    result = ""
    for x in range(reps):
        result = result + word
    return result

print(repl(word, repetitions))