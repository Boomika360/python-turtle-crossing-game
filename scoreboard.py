from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write(f"game over", align=ALIGNMENT, font=FONT)
