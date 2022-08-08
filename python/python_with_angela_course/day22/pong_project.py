from turtle import Screen
from paddle_class import Paddle
from ball_class import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game!')
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')

screen.onkey(l_paddle.go_up,'Left')
screen.onkey(l_paddle.go_down,'Right')

game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        score.increase_score()
    
    if ball.xcor() > 385 or ball.xcor() < -385:
        score.game_over()
        game_is_on = False




screen.exitonclick()