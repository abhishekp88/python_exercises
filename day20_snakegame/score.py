from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color('white')
        self.printScore()

    def printScore(self):
        self.write(f'Score = {self.score}', move=True, align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.printScore()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=True, align=ALIGNMENT, font=FONT)