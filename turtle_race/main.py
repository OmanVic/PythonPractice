import random
from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500, height=400)
is_race = False
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
z = 0
new_turtle = []

if user_bet:
    is_race = True

for _ in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(x=-230, y=-100 + z)
    new_turtle.append(tim)
    z += 30

while is_race:
    for turtle in new_turtle:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race = False
            if user_bet == turtle.color():
                print(f"You win, {turtle.pencolor()} is the winner")
            else:
                print(f"You Lost, {turtle.pencolor()} is the winner")
            break




screen.exitonclick()