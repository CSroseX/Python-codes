from turtle import Turtle 

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('orange')
        self.goto(0,0)
        self.pu()
        self.shape('circle')
        self.speed(1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def rebound_y(self):
        '''when rebounded with a wall'''
        self.y_move *= -1

    def rebound_x(self):
        '''when rebounded with the paddle'''
        self.x_move *= -1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.x_move*= -1
        self.move_speed = 0.1
