import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
guessed_list = []
csv_data = pandas.read_csv("50_states.csv")
all_states = csv_data.state.to_list()
# print(csv_data)

while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_list)} / 50 States Correct', prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_list:
                missing_states.append(state)

                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv('missing_state.csv')

        break

    if answer_state in all_states:
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        state_data = csv_data[csv_data['state'] == answer_state]
        t1.goto(int(state_data['x']), int(state_data['y']))
        t1.write(answer_state)
        if answer_state not in guessed_list:
            guessed_list.append(answer_state)


# def get_mouse_click_cood(x, y):
#     print(x)
#     print(y)
#
#
# turtle.onscreenclick(get_mouse_click_cood)

# keep screen open
# turtle.mainloop()
# screen.exitonclick()
