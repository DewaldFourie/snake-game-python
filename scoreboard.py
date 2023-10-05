
from turtle import Turtle

with open("data.txt") as data:
    DATA = data.read()


ALIGN = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = DATA
        self.score = 0
        self.hideturtle()
        self.goto(x=0, y=270)
        self.pencolor("white")
        self.update_scoreboard()
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data_w:
                data_w.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
