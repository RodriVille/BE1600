import turtle as trtl
import random
import math

painter = trtl.Turtle()

painter.shape("turtle")
painter.color("cyan")

global colorList

painter.left(90)

def moveTurtle(painter, x, y):
    colorList = ['blue', 'red', 'cyan', 'magenta', 'orange', 'yellow']
    if (x > 0):
        for l in range(x):
            painter.right(90)
            painter.forward(1)
            painter.left(90)
            num = random.randint(0, 5)
            painter.color(colorList[num])
            if (y > 0):
                if(painter.ycor() != y):
                    painter.forward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            elif (y < 0):
                if(painter.ycor() != y):
                    painter.backward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            
    elif (x < 0):
        for l in range(abs(x)):
            painter.left(90)
            painter.forward(1)
            painter.right(90)
            num = random.randint(0, 5)
            painter.color(colorList[num])
            if (y > 0):
                if(painter.ycor() != y):
                    painter.forward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            elif (y < 0):
                if(painter.ycor() != y):
                    painter.backward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
        else:
            if (y > 0):
                if(painter.ycor() != y):
                    painter.forward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            elif (y < 0):
                print("y is less than 0, ", y)
                if(painter.ycor() != y):
                    painter.backward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            
moveTurtle(painter, -50, 100)

painter.done()