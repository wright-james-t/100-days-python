import turtle
import pandas
from writer import Writer


# Screen setup
screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# Turtle setup
turtle.shape(image)
writer = Writer()

# Panda data setup
state_data = pandas.read_csv("50_states.csv")


def drop_state(state):
    state_data.drop(state_data[state_data['state'] == state].index, inplace=True)


game_is_on = True
while game_is_on:
    # Allows us to provide the number of states left
    correct_guesses = len(state_data)

    # User prompt set up
    answer_state = screen.textinput(title=f"Guess the state! {correct_guesses} states remaining.", prompt="What state would you like to guess?").title()

    # Check if the answer is right
    matching_rows = state_data[state_data['state'] == answer_state]
    if not matching_rows.empty:
        answer_x = state_data.query(f"state=='{answer_state}'")["x"].iloc[0]
        answer_y = state_data.query(f"state=='{answer_state}'")["y"].iloc[0]
        drop_state(answer_state)
        print(answer_state, answer_x, answer_y)
        writer.add_state_to_map(answer_state, answer_x, answer_y)

    if answer_state == 'Exit':
        break
        state_data['state'].to_csv("states_to_learn.csv")

turtle.exitonclick()
