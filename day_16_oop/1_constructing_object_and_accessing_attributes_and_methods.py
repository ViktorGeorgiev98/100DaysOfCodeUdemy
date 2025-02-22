# external library turtle
# first way
# import turtle
# second way
from turtle import Turtle, Screen

# create a new turtle object
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkOliveGreen4")
timmy.forward(100)

# create another object
my_screen = Screen()
# access attribute
print(my_screen.canvheight)

# object methods
my_screen.exitonclick()
