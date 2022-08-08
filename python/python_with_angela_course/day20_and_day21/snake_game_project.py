from snake_class import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(snake.up, key='Up')
screen.onkey(snake.down, key='Down')
screen.onkey(snake.left, key='Left')
screen.onkey(snake.right, key='Right')

game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
        

screen.exitonclick()
