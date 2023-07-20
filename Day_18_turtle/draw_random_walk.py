import random
# from turtle import Turtle, Screen
import turtle as t

tim = t.Turtle()
directions = [0,90,180,270]
# colours = ['brown','coral','peru','linen','lime','gold','blue','maroon']
# generate random color
def random_color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

t.colormode(255)

# draw a random walk
tim.pensize(15)
tim.speed(10)

for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()