import turtle
from turtle import Turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


file = pandas.read_csv("50_states.csv")
state_file = pandas.DataFrame(file)

guessed_states = []


def check():
    for num in range(0, 50):
        if answer_state == state_file["state"][num]:
            name = Turtle()
            name.hideturtle()
            name.penup()
            name.goto(state_file["x"][num], state_file["y"][num])
            name.write(arg=state_file["state"][num])
            guessed_states.append(answer_state)


on = True

while on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in state_file["state"] if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    check()
for state in guessed_states:
    pandas.DataFrame.drop(state_file, labels=state, axis=0)
pandas.DataFrame.to_csv(state_file, "learn.csv")
