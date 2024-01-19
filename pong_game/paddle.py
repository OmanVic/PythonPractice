from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create(x, y)

    def create(self, x, y):
        self.color("white")
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=4, stretch_len=1)
        self.goto(x, y)

    def move_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def move_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
