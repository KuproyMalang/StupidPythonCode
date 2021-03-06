#=============VALORANT SYMBOL=======================#

import turtle
turtle.color("#d94b4b")

window=turtle.Screen()

turtle.bgcolor("black")
turtle.speed(5)
turtle.pensize(3)

#Right Symbol
turtle.begin_fill()
turtle.goto(200,200)
turtle.right(90)
turtle.forward(150)
turtle.right(45)
turtle.forward(70)
turtle.right(45)
turtle.forward(150)
turtle.end_fill()

#Remove Cursor
turtle.penup()
turtle.forward(80)
turtle.pendown()

#Left Symbol
turtle.begin_fill()
turtle.right(45)
turtle.forward(250)
turtle.left(135)
turtle.forward(150)
turtle.left(45)
turtle.forward(200)
turtle.left(45)
turtle.forward(150)
turtle.left(135)
turtle.forward(150)
turtle.end_fill()

#Remove Symbol
turtle.penup()
turtle.left(45)
turtle.forward(250)
turtle.pendown()

#Frame in Symbol
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(200)

#Remove Cursor
turtle.penup()
turtle.forward(500)
turtle.pendown()

window.exitonclick()
#===================================================#