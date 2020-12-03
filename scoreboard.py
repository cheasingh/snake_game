from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

    def update_score(self):
        self.counter += 1

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.counter}", False, align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.display_score()
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT,
                   font=("Courier", 24, "normal"))
