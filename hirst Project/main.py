import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
turtle.mode("world")
screen = Screen()

# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# # rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(227, 236, 230), (198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27)]


tim = Turtle()
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dot_number = 100
tim.speed("fastest")

for dot in range(1, dot_number + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen.exitonclick()