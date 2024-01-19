import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
point = turtle.Turtle()
point.hideturtle()
score = 0

data = pandas.read_csv("50_states.csv")
state_list = []
guess_state = []

for state in data.state:
    state_list.append(state)
answer = screen.textinput(title="Guess the State", prompt="What's the state name?").title()

while len(guess_state) < 50:
    if answer == "Exit":
        break
    if answer in state_list:
        if answer not in guess_state:
            point.penup()
            point.goto(x=int(data[data.state == answer].x), y=int(data[data.state == answer].y))
            point.write(answer)
            guess_state.append(answer)
            score += 1
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What is another state name?").title()
learn_state = [places for places in state_list if places not in guess_state]

dic_learn_state = {
    "state": learn_state
}

dic_p = pandas.DataFrame(dic_learn_state)
dic_p.to_csv("Learn_States.csv")
