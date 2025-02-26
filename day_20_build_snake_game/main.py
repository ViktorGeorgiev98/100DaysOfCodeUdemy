from turtle import Screen, Turtle
import time

from day_20_build_snake_game.snake import Snake


snake_moving = True
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




while snake_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()








screen.exitonclick()