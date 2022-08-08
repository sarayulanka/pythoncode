from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 20, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level_count = 1
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=('courier', 30, 'bold'))
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level_count}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level_count += 1
        self.update_scoreboard()