import turtle
# construct object class name start with capital letter
# create a object
timmy = turtle.Turtle()
print(timmy)
# changing attributes value
timmy.shape('turtle')
# changing attributes value
timmy.forward(30)
timmy.color('green')
# access screen method
screen = turtle.Screen()
# acccessing attributes
print(screen.canvheight)
print(screen.canvwidth)
# accessing methods
screen.exitonclick()

import prettytable

prettytable  = prettytable.PrettyTable()
# add column
prettytable.add_column("Pokemon Name",['Pikachu','Squirtle','Charmander'])
# ADD  another columns
prettytable.add_column("Type",['Electric','Water','Fire'])
prettytable.align = 'r'


print(prettytable)

