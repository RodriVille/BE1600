import turtle
import tkinter

t = turtle.Turtle()

def calcNum(t):
    a = 3
    while (1 == 1):
        drawShape(t, a)
        a += 1

            

def drawShape(t, a):
    angle = 360 / a
    for i in range (a):
        t.forward(20)
        t.right(angle)
        a+=1 


calcNum(t)
wn = turtle.Screen()
wn.mainloop()