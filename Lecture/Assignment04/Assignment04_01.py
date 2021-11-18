import random as r
userFileName = input("Enter the name of the file to which results should be written: ")
fileLocation = "Lecture/Assignment04/" + userFileName
randFile = open(fileLocation, 'w')
userRandCount = int(input("Enter the number of random numbers to be written to the file: "))
def fileEdit(count, file):
    for i in range(count):
        file.write(str(r.randint(1,100)) + "\n")
fileEdit(userRandCount, randFile)
randFile.close()