import turtle


# In this file, we are going to be experimenting with turtle graphics and the class, Turtle
# We will also be doing challenges


# First, let's create an object from the class turtle:
bobby_the_turtle = turtle.Turtle() 

# Next, let's change the shape and color of our object:
bobby_the_turtle.shape("turtle")
bobby_the_turtle.color("plum")

# Now let's try getting bobby_the_turtle to draw a shape:
# P.S. bobby_the_turtle is going to draw a square

bobby_the_turtle.pencolor('blue')

bobby_the_turtle.forward(100)
bobby_the_turtle.right(90)
bobby_the_turtle.forward(100)
bobby_the_turtle.right(90)
bobby_the_turtle.forward(100)
bobby_the_turtle.right(90)
bobby_the_turtle.forward(100)

bobby_the_turtle.clear()

# Now, let's try getting bobby_the_turtle to draw a dashed line:

for turtle in range(1, 5):
    bobby_the_turtle.pendown()
    bobby_the_turtle.forward(10)
    bobby_the_turtle.penup()
    bobby_the_turtle.forward(10)

bobby_the_turtle.clear()

# Now, let's try to get bobby_the_turtle to draw different shapes:
bobby_the_turtle.pendown()
bobby_the_turtle.pencolor("blue")

bobby_the_turtle.speed(9)

for turtle in range(3, 10):
    angle = 360 / turtle
    for t in range(1, turtle):
        bobby_the_turtle.forward(100)
        bobby_the_turtle.right(angle)

bobby_the_turtle.clear()
bobby_the_turtle.penup()
bobby_the_turtle.home()

# A harder project we can do is to generate a random walk for bobby_the_turtle:
# For this project, let's also try generating random colors using a concept called tuples

# Tuples are lists with elements that cannot be modified
# The only difference is that you can modify elements in lists but you cannot modify elements in tuples
# The syntax for tuples are tuplename = (element, element...)
# Let's create a tuple below:
tuple_intro = (1, 2, 3, 4)

# Now, let's use our knowledge of tuples to generate random rgb colors
# First let's create a function called random_color:


bobby_the_turtle.speed(8)
bobby_the_turtle.pensize(width=6)
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


screen = t.Screen()
coin_flip = ["heads", "tails"]


for r in range(1, 75):
    bobby_the_turtle.pendown()
    if random.choice(coin_flip) == "heads":
        bobby_the_turtle.forward(50)
        bobby_the_turtle.color(random_color())
        bobby_the_turtle.right(random.choice([0, 90, 180, 270]))
    else:
        bobby_the_turtle.forward(50)
        bobby_the_turtle.color(random_color())
        bobby_the_turtle.left(random.choice([0, 90, 180, 270]))

screen.clear()
bobby_the_turtle.home()


# The last exercise we are going to do is create a spirograph:

timmy = t.Turtle()
t.colormode(255)
bobby_the_turtle.speed(0)

for i in range(1,36):
    bobby_the_turtle.color(random_color())
    bobby_the_turtle.circle(50)
    bobby_the_turtle.left(10)



# This should be the last step and should be after all the code you are doing with the object
screen.exitonclick()