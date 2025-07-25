STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.go_to_start()

        
    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
    

    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def complete_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False