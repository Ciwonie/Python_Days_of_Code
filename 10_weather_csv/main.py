import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a State: ").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv")
        break
    # If answer_state is one of the states in all the states of the 50_states_csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # conditionals grab rows in data
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


# alternative way of keeping our screen open [screen.exitonclick()]
turtle.mainloop()









#def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)