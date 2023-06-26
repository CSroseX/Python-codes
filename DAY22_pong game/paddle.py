from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.shapesize(stretch_len=2,stretch_wid=7)
        self.shape('square')
        self.pu()
        self.speed('fastest')
        self.goto(position)

    def move_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
