import random
# from turtle import Turtle, Screen
import turtle as t


directions = [0,90,180,270]
colours = ['brown','coral','peru','linen','lime','gold','blue','maroon']
# generate random color

tim2 = t.Turtle()

def draw_shape(sides):
    angle = 360 / sides
    for d in range(sides):
        tim2.forward(100)
        tim2.right(angle)


for num in range(3,11):
    tim2.color(random.choice(colours))
    draw_shape(num)



screen = t.Screen()
screen.exitonclick()