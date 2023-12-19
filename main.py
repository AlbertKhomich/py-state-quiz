import turtle
import pandas
import statelocation

screen = turtle.Screen()
screen.screensize(725, 491)
screen.bgpic("blank_states_img.gif")
screen.title("Name the States")

states = pandas.read_csv("50_states.csv")
correct_answers = []
states_to_learn = []

while len(correct_answers) < 50:
    answer = screen.textinput(f"{len(correct_answers)}/50 States Correct", "What's another State's name?").title()
    if answer == "Exit":
        break
    for state in states.state:
        if state == answer and answer not in correct_answers:
            correct_answers.append(answer)
            correct_state = states[states.state == answer]
            x = correct_state.iloc[0, 1]
            y = correct_state.iloc[0, 2]
            new_state = statelocation.StateLocation(answer, x, y)

states_to_learn = [state for state in states.state if state not in correct_answers]

states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv("to_learn.csv")
