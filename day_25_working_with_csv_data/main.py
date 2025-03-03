import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
# how to add image to turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# end of how to add image to turtle
# figure out coordinates of the states, we do not need it now because we have in the csv file, but it is good to know
# def get_mouse_click_coor(x, y):
#     print(x, y)
# add listener for mouse click event
# turtle.onscreenclick(get_mouse_click_coor)
# this will keep the screen going even when we click

states_guessed = []
game_is_on = True
states_data = pandas.read_csv("50_states.csv")
while game_is_on:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state is None:
        break
    elif answer_state == "Exit":
        all_states_as_list = states_data.state.to_list()
        states_not_guessed = [state for state in all_states_as_list if state not in states_guessed]
        new_data = {
            "states_not_guessed": states_not_guessed
        }
        df = pandas.DataFrame(new_data)
        df.to_csv("states_not_guessed.csv")
        break
    else:
        current_state = states_data[states_data["state"] == answer_state]
        print(current_state.state)
        if not current_state.empty:
            states_guessed.append(answer_state)
            current_state_x_coor = current_state.x.values[0]
            current_state_y_coor = current_state.y.values[0]

            # Create a turtle to mark the state
            marker = turtle.Turtle()
            marker.penup()
            marker.hideturtle()
            marker.goto(current_state_x_coor, current_state_y_coor)
            marker.write(answer_state, align="center", font=("Arial", 10, "normal"))



# there is a second way where we can convert the data to a list
# all_states = states_data.to_list()
# if answer_state in states_data:
#     proceed as before



# turtle.mainloop()








