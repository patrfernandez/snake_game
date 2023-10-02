from turtle import Turtle
ALINGMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align=ALINGMENT, font=FONT)