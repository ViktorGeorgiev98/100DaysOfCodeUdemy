import turtle as t
import heroes
import villains
import random


timmy_the_turtle = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# draw square 1st way
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# draw square 2nd way
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# draw a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


# draw 9 different shapes
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)


# draw a random walk

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed"]
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))


# draw a spirograpgh
# timmy_the_turtle.color(random_color())
# timmy_the_turtle.circle(100)

# how to extract rgb values from images

















screen = t.Screen()
screen.exitonclick()