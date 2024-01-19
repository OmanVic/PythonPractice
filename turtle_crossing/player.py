from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.starting_position()
        self.left(90)

    def move(self):
        self.forward(10)

    def starting_position(self):
        self.goto(STARTING_POSITION)

