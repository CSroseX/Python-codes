from turtle import Turtle,Screen


FONT = "Impact"
FONT_SIZE = 24
FONT_STYLE = "normal"
FONT_ALIGN = 'center'
GAME_OVER_TEXT = 'game over noob'

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.score_value = 0
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(x=0,y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score_value} || high score : {self.high_score}",align=FONT_ALIGN,font=(FONT,FONT_SIZE,FONT_STYLE))

    def reset(self):
        if self.score_value>self.high_score:
            self.high_score = self.score_value
            with open('data.txt',mode='w') as data:
                data.write(f'{self.high_score}')
        self.score_value = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color('red')
    #     self.write(GAME_OVER_TEXT,align=FONT_ALIGN,font=(FONT,FONT_SIZE,FONT_STYLE))

    def increase_score(self):
        self.score_value+=1
        self.update_score()