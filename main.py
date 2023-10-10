from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

WIN_POINTS = 3

# Specifikacije ekrana na kojem se igra prikazuje
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Kreiranje objekata palica, lopte i scoreboarda
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
# Komande upravljanja desnom palicom
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Komande upravljanja lijevom palicom
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detekcija dodira sa zidom
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Odbijanje loptice
        ball.bounce_y()

    # Detekcija dodira sa palicom
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detekcija i radnja nakon što loptica promaši desnu palicu, te povečavanje boda lijevom igraču
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detekcija i radnja nakon što loptica promaši lijevu palicu, te povečavanje boda desnom igraču
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == WIN_POINTS:
        game_is_on = False
        scoreboard.player_1_win()

    if scoreboard.r_score == WIN_POINTS:
        game_is_on = False
        scoreboard.player_2_win()

screen.exitonclick()
