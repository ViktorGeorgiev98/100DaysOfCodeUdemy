from turtle import Screen
import time

from day_20_build_snake_game.scoreboard import Scoreboard
from day_20_build_snake_game.snake import Snake
from day_20_build_snake_game.food  import Food


snake_moving = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

#     collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()


#     collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()


#   detect collision with tail
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        scoreboard.reset()
        snake.reset()




screen.exitonclick()