print()
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

user_input = screen.textinput(title='Make Your Bet',prompt='(red/orange/yellow/green/blue/purple)')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    race_is_on = True
else :
    race_is_on = False

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"Congrats you've won the bet. The winning turtle is {winning_color}")
            else:
                print(f"Awww XD   :/ You lost . The winning turtle is {winning_color}")
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


print()
screen.exitonclick()