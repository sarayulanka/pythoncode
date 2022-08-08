# Turtle event listeners are blocks of code that make something 
# that the user does, like a key that the user types, a trigger to start listening or waiting 
# for a specific event to happen.

# We need to be able to listen for a certain key 
# that the user presses and then draw something based on that key

# Let's try using event listeners so that we can get familiarized with them
# First let's import Turtle class and Screen class:
from turtle import Turtle, Screen
import random
import turtle

print("Space to move forward, a to move backward, b to make circles, c to move to right, d to move to left")

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("darkseagreen4")
jimmy.pencolor("lightpink")

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


screen = Screen()


# Now let's try using the listen method to start the listening 
# and the onkey method to specify which key should the user press to start listening

# The onkey method requires a function with no arguments 
# and a key in quotes that should activate the listening:

jimmy.pensize(5)

def move_forward():
    jimmy.forward(25)


screen.onkey(key='a', fun=move_forward)

screen.exitonclick()
