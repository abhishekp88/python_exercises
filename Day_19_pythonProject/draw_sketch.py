from turtle import Turtle, Screen

tim = Turtle()

def move_forward() :
    tim.forward(10)

def move_backward() :
    tim.backward(10)

def clockwise():
    tim.right(10)

def anticlockwise():
    tim.left(10)

def clearturtle() :
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=clockwise)
screen.onkey(key="d",fun=anticlockwise)
screen.onkey(key='c', fun=clearturtle)
screen.exitonclick()