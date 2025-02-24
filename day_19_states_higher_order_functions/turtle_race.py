import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [90, 60, 30, 0, -30, -60]
is_race_on = False
all_turtles= []
# 1st way
# tim = Turtle(shape="turtle")
# tim.color(colors[0])
# tim.penup()
# tim1 = Turtle(shape="turtle")
# tim1.color(colors[1])
# tim1.penup()
# tim2 = Turtle(shape="turtle")
# tim2.color(colors[2])
# tim2.penup()
# tim3 = Turtle(shape="turtle")
# tim3.color(colors[3])
# tim3.penup()
# tim4 = Turtle(shape="turtle")
# tim4.color(colors[4])
# tim4.penup()
# tim5 = Turtle(shape="turtle")
# tim5.color(colors[5])
# tim5.penup()
#
#
# tim.goto(x=-240, y=0)
# tim1.goto(x=-240, y=30)
# tim2.goto(x=-240, y=60)
# tim3.goto(x=-240, y=-30)
# tim4.goto(x=-240, y=-60)
# tim5.goto(x=-240, y=90)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! {winning_color} turtle is the winner")
            else:
                print(f"You have lost! {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()