from turtle import Turtle
STARTING_POINT = (0,-280)

class Player_turtle(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.shape('turtle')
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POINT)
        
    def move_forward(self):
        self.pu
        self.setheading(90)
        self.forward(20)
    
    def move_backward(self):
        self.pu()
        self.backward(20)

    def go_to_starting(self):
        self.goto(STARTING_POINT)
    