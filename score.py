from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-20, 270)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.display()

    def increase_left_score(self):
        self.l_score += 1
        self.clear()
        self.display()

    def increase_right_score(self):
        self.r_score += 1
        self.clear()
        self.display()

    def display(self):
        self.write(f" {self.l_score} | {self.r_score}", align=ALIGNMENT, font=FONT)
