from turtle import Turtle, Screen
import random
import turtle

# Lets's create our etch-a-scketch app!

print("Space to move forward, a to move backward, b to make circles, c to move to right, d to move to left")

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("darkseagreen4")
jimmy.pencolor("lightpink")
jimmy.pensize(5)
jimmy.home()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


screen = Screen()


def move_forward():
    jimmy.forward(25)

def move_backward():
    jimmy.color(random_color())
    jimmy.setheading(180)
    jimmy.forward(25)

def move_left():
    jimmy.color(random_color())
    jimmy.left(90)
    jimmy.forward(25)

def move_right():
    jimmy.color(random_color())
    jimmy.right(90)
    jimmy.forward(25)

def make_circle():
    jimmy.color(random_color())
    jimmy.circle(30)

def clear_screen():
    screen.clear()
    jimmy.home()    

screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.onkey(key='a', fun=move_backward)
screen.onkey(key='d', fun=move_left)
screen.onkey(key='c', fun=move_right)
screen.onkey(key='b', fun=make_circle)
screen.onkey(key='u', fun=clear_screen)

# P.S. onkey is a high order function because it takes a function as one of the arguments
# See high_order_functions.py file to get a definition of high order functions.

screen.exitonclick()