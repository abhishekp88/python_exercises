import random
import turtle as t
tim = t.Turtle()

# generate random color
def random_color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

t.colormode(255)





tim.speed(0)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()