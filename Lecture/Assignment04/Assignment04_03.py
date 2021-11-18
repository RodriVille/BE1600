this = open("Lecture/Assignment04/this.txt", 'r')
that = open("Lecture/Assignment04/that.txt", 'w')
thatList = [i for i in this]
for i in range(0, len(thatList), 2):
    that.write(thatList[i])
this.close()
that.close()