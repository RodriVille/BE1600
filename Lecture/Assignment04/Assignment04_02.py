import math
file = open("Lecture/Assignment04/tempconv.txt", 'w')
file.write("Farenheit" + (12-len("Farenheit")) * " " + "Celsius" + (12-len("celsius")) * " " + "\n")
for i in range(-10, 11):
    farenheit = format(float(i), '.2f')
    celsius = round(((i - 32) * 5 / 9), 2)
    file.write(str(farenheit) + (12-len(str(farenheit))) * " " + str(celsius) + (12-len(str(celsius))) * " " + "\n")
file.close()
    