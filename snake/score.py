from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}", False, "center", ('Arial', 16, 'normal'))


    def increase_score(self):
        self.score += 1
        self.update()


    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.hideturtle()
        self.color('white')
        self.write(f"Game Over", False, "center", ('Arial', 60, 'normal'))



