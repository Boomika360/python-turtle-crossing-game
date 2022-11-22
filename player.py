from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_original()
        self.setheading(90)

    def move_turtle(self):
        new_x = self.xcor() + 0
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def reset_original(self):
        self.goto(STARTING_POSITION)
