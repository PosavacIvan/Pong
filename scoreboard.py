from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

# Dodjela bodova igraču koji je osvojio bod
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

# Povečavanje scoreboarda lijevom igraču
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

# Povečavanje scoreboarda desnom igraču
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

# Ispis ako igrač 1 pobjedi
    def player_1_win(self):
        self.goto(0, 0)
        self.write("Player 1 WIN", align=ALIGNMENT, font=FONT)

# Ispis ako igrač 2 pobjedi
    def player_2_win(self):
        self.goto(0, 0)
        self.write("Player 2 WIN", align=ALIGNMENT, font=FONT)


