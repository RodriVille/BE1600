def morse():
    #Dictionary for morse code
    file = open('morse.txt', 'r')
    file = file.readlines()
    morseDict = {}
    for i in file:
        i = i.split()
        morseDict[i[0]] = i[1]
    return morseDict

def main():#Main Menu
    print("Hello, this program allows you to translate text to morse code or translate morse code to text.\n\n",
          "Please, select one of the below options:\n\n",
          "*** Enter 't' for encoding text\n",
          "*** Enter 'm' for decoding morse code\n",
          "*** Enter 'e' to exit the program.\n")
    user = input("My input: ")#Taking in user input to determine what he program should do
    menuChoice(user)

def menuChoice(choice):#Calls on the correct program based on user input
    match choice:
        case "t":
            encoding()
        case"m":
            decoding()
        case "e":
            print("Thank you for using this program")
        case _:#Calls on the function again if the input is invalid
            print("** invalid option")
            user = input("Please enter a valid option: ")
            menuChoice(user)

def encoding():
    print("Please enter text to translate: \n")
    user = input("")#Taking message to be encoded
    user  = user.upper()#Converting message into upper case
    msg = ""
    morseD = morse()
    for i in user:#Translating into morse code with one space in between letters and three in between words
        if i != " ":
            msg += str(morseD[i])
            msg += " "
        else:
            msg += "   "
    print(msg, "\n\n")
    main()#calls on main


def decoding():
    print("Please enter morse to translate: \n")
    user = input("")#Taking message to be encoded
    engD = morse()
    user = user.split("    ")
    print(user)
    msg = ""
    for word in user:#Converting morse code into regular text
        word = word.split(" ")#eliminating spaces in words
        for char in word:
            msg += list(engD.keys())[list(engD.values()).index(char)]#searching for corresponding letter to each morse code character
        msg += " "
    print(msg)
    print("\n\n")
    main()#calls on main

main()