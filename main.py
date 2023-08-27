import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_dataframe = pandas.read_csv("50_states.csv")
all_states_list = states_dataframe.state.to_list()

missing_states_list = []
guessed_states_list = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states_list)}/50 States Correct",
                                    prompt="Whats another state's name?").title()

    if answer_state == "Exit":
        for state in all_states_list:
            if state not in guessed_states_list:
                missing_states_list.append(state)
        states_to_learn_dataframe = pandas.DataFrame(missing_states_list)
        states_to_learn_dataframe.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states_list and answer_state not in guessed_states_list:
        guessed_states_list.append(answer_state)
        state_name_t = Turtle()
        state_name_t.penup()
        state_name_t.hideturtle()
        guessed_state_data = states_dataframe[states_dataframe.state == answer_state]
        state_name_t.goto(int(guessed_state_data.x), int(guessed_state_data.y))
        state_name_t.write(answer_state)

    if len(guessed_states_list) == len(all_states_list):
        game_is_on = False
        missing_states_list.append("You've managed to guess all of the states. Well done!")

