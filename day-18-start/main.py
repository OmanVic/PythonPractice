import random
import turtle
from turtle import Turtle, Screen
from typing import List
turtle.colormode(255)
tim = Turtle()
# # timmy_the_turtle.shape("turtle")
# # timmy_the_turtle.color("red")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# #
# # for _ in range(4):
# #     tim.forward(100)
# #     tim.right(90)
#
# # for _ in range(15):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
# #
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
# # for side in range(3, 11):
# #     for _ in range(side):
# #
# #         tim.forward(80)
# #         tim.right(360/side)
# #     tim.color(random.choice(color))
#
# tim.pensize(10)
tim.speed(10)
#
# def change_direction():
#     direction = random.randint(0, 1)
#     if direction == 0:
#         tim.right(90)
#     else:
#         tim.left(90)
#
#
# for _ in range(500):
#     tim.forward(20)
#     change_direction()
#     tim.color(random_color())

def draw_circle(gap):
    for times in range(int(360 /gap )):
        tim.circle(100)
        tim.setheading(tim.heading() + 10)
        tim.color(random_color())
draw_circle(10)

screen = Screen()

screen.exitonclick()
