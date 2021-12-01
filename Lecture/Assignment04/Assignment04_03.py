this = open("this.txt", 'r')
that = open("that.txt", 'w')
thatList = [i for i in this]
for i in range(0, len(thatList), 2):
    that.write(thatList[i])
this.close()
that.close()