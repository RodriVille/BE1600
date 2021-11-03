roomDict = {"CS101": 3004, "CS102": 4501, "CS103": 6755, "NT110": 1244, "CM241": 1411}
profDict = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
timeDict = {"CS101": "8:00am", "CS102": "9:00am", "CS103": "10:00am", "NT110": "11:00am", "CM241": "1:00pm"}

course = input("Ender a course number: ")
if course in roomDict:
    print("The details for course", course, "are: \n",
          "Room: ", roomDict[course], "\n",
          "Instructor: ", profDict[course], "\n",
          "Time: ", timeDict[course])
else:
    print(course, "is an invalid course number")