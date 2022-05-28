

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")  # it is a tuple


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # we have inherited from the Turtle class... Now our Scoreboard class can do anything that Turtle class can do.
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # See the use of turtle.write() method

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score += 10
        self.clear()  # so that it clears the scoreboard and new score is not written overlapping previous one
        self.update_scoreboard()