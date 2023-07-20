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
# tim.shape('arrow')
# tim.color('#4169E1')
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)
# tim.right(90)
# tim.forward(200)
# for x in range(0,20) :
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# tim2 = t.Turtle()
#
# def draw_shape(sides):
#     angle = 360 / sides
#     for d in range(sides):
#         tim2.forward(100)
#         tim2.right(angle)
#
#
# for num in range(3,11):
#     tim2.color(random.choice(colours))
#     draw_shape(num)


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