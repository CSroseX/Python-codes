from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
screen.listen()
snake.make_snake()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

food = Food()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        score.reset()
        snake.reset()

    #detect collision with body/tail 
    #USING SLICING TECHNIQUE
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()

screen.exitonclick()