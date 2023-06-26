from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-280,250)
        self.score_number = 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f'score : {self.score_number}',move=False,align='left',font=('Arial',15,'normal'))

    def plus_point(self):
        self.score_number+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER NOOB',move=False,font=('Courier',20,'bold'),align='center')

        