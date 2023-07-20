import random
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []

turtle_list = []
for turle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turle_index])
    new_turtle.goto(x=-240, y=y_positions[turle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! the {winning_color} turtle is the winner !")
            else:
                print(f"You have lost! the {winning_color} turtle is the winner !")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()