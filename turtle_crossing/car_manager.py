from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

coordinate_list = []
for coordinates in range(-250, 250, 20):
    coordinate_list.append(coordinates)


class CarManager:
    def __init__(self):
        self.all_car = []
        self.more = 0

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y = random.choice(coordinate_list)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random_y)
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE + self.more)

    def more_increment(self):
        self.more += MOVE_INCREMENT
