#BUG : when the ball touches the paddle,weird dancing of the ball happens.. probably something wrong with collision co-ordinates
#TWEAKS : instead of making the ball rebound in an expected fashion, make it rebound i.e, its rebound is unexpected. 

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong game')
screen.tracer(0)

l_paddle= Paddle((-380,0))
r_paddle= Paddle((380,0))
ball = Ball()

score = Score()

screen.listen()
screen.onkeypress(l_paddle.move_up,'w')
screen.onkeypress(l_paddle.move_down,'s')
screen.onkeypress(r_paddle.move_up,'Up')
screen.onkeypress(r_paddle.move_down,'Down')

game_is_on = True
right_score = 0
left_score = 0
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detection with upper walls
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.rebound_y()

    #detection with paddle 
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.rebound_x()

    #detect when paddle misses the ball
    if ball.xcor()>400 :
        ball.reset_position()
        score.update_l_score()

    if ball.xcor()<-400:
        ball.reset_position()
        score.update_r_score()

screen.exitonclick()