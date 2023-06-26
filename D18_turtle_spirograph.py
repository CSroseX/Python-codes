from turtle import Turtle,Screen
import random

t = Turtle()
screen = Screen()

t.speed("fastest")

def rand_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return t.color(r,g,b)

n = 0
initial_heading = t.heading()
def make_spirograph(gap_size):
    for _ in range (int(360/gap_size)):
        rand_color()
        t.circle(100)
        t.setheading(t.heading() + gap_size)
make_spirograph(1)

screen.exitonclick #exit on click not working //Fix it
