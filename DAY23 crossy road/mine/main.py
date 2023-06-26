# improements : make it more realistic . make it prettier 
from turtle import Screen
from chicken import Player_turtle
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
user = Player_turtle()
screen.tracer(0)

# For moving forward
screen.listen()
screen.onkey(user.move_forward,key='Up')
screen.onkey(user.move_backward,key='Down')

cars = Cars()
score = Scoreboard()


game_is_on = True
while game_is_on :
    time.sleep(0.1)
    screen.update()

    #spwning and moving of cars
    cars.random_spawn()
    cars.move_cars()

    #detect collision of player_turtle with cars
    for car in cars.all_cars:
        if car.distance(user) < 21:
            score.game_over()
            game_is_on = False


    #detect when player_turtle reaches the other side 
    if user.ycor()>280:
        user.go_to_starting()
        cars.level_up()
        score.plus_point()


screen.exitonclick()
