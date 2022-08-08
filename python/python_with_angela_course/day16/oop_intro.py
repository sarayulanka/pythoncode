# We are doing more and more complex programs that require a lot more code
# So much code will cause de-organization in our programs and make it impossible to find the bugs
# This is called procedural programming
# While coding programs that need a lot of code, we are making our job complex
# That's where object oriented programming comes in handy.
# OOP is a concept that creates objects that can create solutions for components in our programs
# Once the objects are created, you won't have to tell it how to create solutions for components

# This will make our code easier to understand, more organized, and simpler


# Now to create these objects, we would need two things: attributes and methods
# Attributes are basically variables used to program the objects,
# and Methods are functions used to program the objects

# Now from an object blue print, we can create many versions of the object
# An object blueprint is called a class and the different versions are called the objects
# Classes are used to build objects.

# Now let's try actually constructing objects and creating attributes and methods

# turtle module contains a class called Turtle
# let's access it
# First we have to import turtle:
from turtle import Turtle, Screen

# The syntax for creating an object using a class is this: classname()
# Next, Let's create an object from the class turtle

another_variable = 12

timmy = Turtle()
print(timmy)

# let's access a method for timmy to change the shape of timmy
# let's change it into a turtle below:
timmy.shape("turtle")

# Let's also change the color of timmy below:
timmy.color("LightSkyBlue")

# Let's move timmy 100 paces forward:
timmy.forward(100)

# Below this line, we accessed attributes of an object called my_screen:
my_screen = Screen()
print(my_screen.canvheight)

# Now each object is supposed to do something and to do these things the methods need to be accessed:
# Just a reminder, methods mean functions involved with objects

# Let's try tapping into methods:
# P.S. the syntax for accessing methods is objectname.methodname()

# Let's tap into a method for my_screen called exitonclick()
# The exitonclick() method means that the tab will only close when we click on the screen
my_screen.exitonclick()
