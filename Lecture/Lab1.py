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
        print("x is more than 0, ", x)
        for l in range(x):
            painter.right(90)
            painter.forward(1)
            painter.left(90)
            num = random.randint(0, 5)
            painter.color(colorList[num])
            if (y > 0): 
                print("y is more than 0, ", y)
                for l in range(y):
                    painter.forward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            elif (y < 0):
                print("y is less than 0, ", y)
                for l in range(abs(y)):
                    painter.backward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            
    elif (x < 0):
        print("x is less than 0, ", x)
        for l in range(abs(x)):
            painter.left(90)
            painter.forward(1)
            painter.right(90)
            num = random.randint(0, 5)
            painter.color(colorList[num])
            if (y > 0):
                print("y is more than 0, ", y)
                for l in range(y):
                    painter.forward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            elif (y < 0):
                print("y is less than 0, ", y)
                for l in range(abs(y)):
                    painter.backward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
        else:
            print("x is zero")
            if (y > 0):
                print("y is more than 0, ", y)
                while(painter.ycor() != y):
                    painter.forward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            elif (y < 0):
                print("y is less than 0, ", y)
                while(painter.ycor() != y):
                    painter.backward(1)
                    num = random.randint(0, 5)
                    painter.color(colorList[num])
            
moveTurtle(painter, 50, 50)

wn = trtl.Screen()
wn.mainloop()