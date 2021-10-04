import turtle

painter = turtle.Turtle()

side = 500
for x in range(10):
    painter.penup()
    painter.goto((-side/2), (-side/2))
    painter.pendown()
    for x in range(4):
        painter.forward(side)
        painter.left(90)
    side -= 10
    
wn = turtle.Screen()
wn.mainloop()