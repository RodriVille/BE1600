import math
file = open("tempconv.txt", 'w')
file.write("{0:12s}{1:12s}{2}".format("Farenheit", "Celcius", "\n"))
for i in range(-10, 11):
    farenheit = format(float(i), '.2f')
    celsius = str(round(((i - 32) * 5 / 9), 2))
    farenheit = str(farenheit)
    file.write("{0:12s}{1:12s}{2}".format(farenheit, celsius, "\n"))
file.close()
    