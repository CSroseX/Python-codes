from turtle import Turtle,Screen

t = Turtle()

screen = Screen()
screen.listen()

def move():
    t.forward(10)

def turn_180():
    heading = t.heading() + 180
    t.setheading(heading)

def tilt_up():
    heading = t.heading() + 10
    t.setheading(heading)

def tilt_down():
    heading = t.heading() - 10
    t.setheading(heading)

def clear():
    t.goto(0,0)
    t.clear()

screen.onkey(key='w',fun =move)
screen.onkey(key='d',fun =turn_180)
screen.onkey(key='p',fun =tilt_down)
screen.onkey(key='o',fun =tilt_up)
screen.onkey(key='c',fun =clear)

screen.exitonclick()