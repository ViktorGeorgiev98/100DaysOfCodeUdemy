from turtle import Screen
from zipfile import sizeEndCentDir

from day_21_pong_game.paddle import Paddle
from day_21_pong_game.ball import Ball
import time

from day_21_pong_game.scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
paddle = Paddle((350, 0))
second_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# screen.tracer(1)


screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")
screen.onkey(second_paddle.move_up, "w")
screen.onkey(second_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#     detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#     detect collision with right paddle
    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(second_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#     left player scores
    if ball.xcor() > 380:
        scoreboard.r_point()
        ball.reset_position()

    # rigth player scores
    if ball.xcor() < -380:
        scoreboard.l_point()
        ball.reset_position()



screen.exitonclick()