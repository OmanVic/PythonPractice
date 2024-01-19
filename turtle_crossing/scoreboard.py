from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(x=-15, y=260)
        self.score.write(f"Level {self.level}", font=FONT, align="center")

    def game_over(self):
        self.score.home()
        self.score.write(f"Game Over", font=FONT, align="center")



    def score_update(self):
        self.score.clear()
        self.level += 1
        self.score.write(f"level {self.level}", font=FONT, align="center")
