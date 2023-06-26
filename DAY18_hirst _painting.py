from import_function import color_list
import random
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed("fastest")
t.pu()
t.hideturtle()
t.goto(-255,-200)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#to draw a line
no_of_dots = 0
for dots in range(0,100):
    t.dot(20,random_color())
    no_of_dots+=1
    t.forward(50)
    #to go back to initial position but above once drawn a line
    if no_of_dots % 10 ==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen.exitonclick()