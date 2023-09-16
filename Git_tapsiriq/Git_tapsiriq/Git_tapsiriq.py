from turtle import *

a = Turtle()

a.hideturtle()

a.left(50)

a.forward(200)

for i in range(0,20) :
    a.left(9)
    a.forward(12)

a.forward(10)
a.penup()
a.left(40)
a.forward(230)
a.right(140)
a.pendown()
a.forward(200)

for i in range(0,20) :
    a.right(9)
    a.forward(12)
a.forward(10)
a.penup()
a.forward(100)
a.right(150)
a.forward(70)
a.left(110)
a.pendown()
a.forward(100)
a.back(100)
a.penup()
a.back(20)
a.pendown()
a.back(10)
a.getscreen()._root.mainloop()
