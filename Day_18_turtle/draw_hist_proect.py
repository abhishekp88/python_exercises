import random
import turtle as t

import colorgram
t.colormode(255)
rgbcolors = []
colors = colorgram.extract('image.webp', 30)
tim = t.Turtle()
number_of_dots = 101
tim.speed(10)
tim.penup()
tim.hideturtle()
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgbcolors.append(new_color)

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
for dot_count in range(1,number_of_dots):
    color1 = random.choice(rgbcolors)
    tim.dot(20,color1)
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










screen = t.Screen()
screen.exitonclick()