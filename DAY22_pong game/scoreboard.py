from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.l_score= 0
        self.r_score= 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.pu()
        self.goto(0,240)
        self.write(f'{self.l_score} : {self.r_score}',move=False,align='center',font=('Arial',20,'normal'))
    
    def update_l_score(self):
        self.l_score+=1
        self.update_score()
    
    def update_r_score(self):
        self.r_score+=1
        self.update_score()
