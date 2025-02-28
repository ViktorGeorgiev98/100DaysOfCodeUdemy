from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle(position)

    def create_paddle(self, side):
        self.color("white")
        self.penup()
        self.goto(self.position)
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)