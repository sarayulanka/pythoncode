# In this file, we are going to start creating our turtle race game:

from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle do you think will win the race? Choose a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
counter = 0

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[counter])
    new_turtle.goto(x=-235,y=y_positions[counter])
    counter += 1
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on == True:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won the bet! The {winning_color} turtle was the winner!")
            else:
                print(f"You lost the bet. The {winning_color} was the winner.")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            


