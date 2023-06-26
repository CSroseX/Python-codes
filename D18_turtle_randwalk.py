from turtle import Turtle,Screen
import random

t = Turtle()
screen = Screen()

t.shape("arrow")
t.pensize(10)
t.speed(100)

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

turn = [0,90,180,270]

def random_walk():
    for _  in range(1000):
        if t.xcor() >= screen.window_width() / 2:
            t.setheading(180) 
        elif t.xcor() <= -screen.window_width() / 2:
            t.setheading(0)  
        elif t.ycor() >= screen.window_height() / 2:
            t.setheading(270)  
        elif t.ycor() <= -screen.window_height() / 2:
            t.setheading(90)
        t.color(rand_color())
        t.forward(random.randint(20,60))
        t.right(random.choice(turn))
random_walk()



screen.exitonclick()