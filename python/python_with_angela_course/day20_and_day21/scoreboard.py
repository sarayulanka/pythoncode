from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 20, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open('high_score.txt') as high_score_file:
            self.high_score = high_score_file.read()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_count}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_count += 1
        self.update_scoreboard()

    def reset(self):
        if int(self.high_score) < self.score_count:
            self.high_score = self.score_count
            with open('high_score.txt', mode='w') as high_score_file:
                high_score_file.write(f"{self.high_score}")
            
        self.update_scoreboard()
        self.score_count = 0
