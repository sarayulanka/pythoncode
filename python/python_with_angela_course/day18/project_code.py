import turtle as turtle_module
import random

bob = turtle_module.Turtle()
turtle_module.colormode(255)
bob.shape("turtle")
bob.color("SkyBlue1")
bob.speed(8)
bob.penup()


color_list = [(102,204,255), (221,153,255), (128,128,255), (0,0,153), (255,179,255), (0,213,255)]

bob.setheading(225)
bob.forward(300)
bob.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    bob.dot(20, random.choice(color_list))
    bob.forward(50)

    if dot_count % 10 == 0:
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()