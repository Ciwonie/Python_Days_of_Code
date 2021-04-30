from turtle import Screen, Turtle

import scoreboard
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()

    # detect collision with walls (600x800)
    if pong.ycor() > 280 or pong.ycor() < -270:
        pong.bounce_y()

    # detect collision with r_paddle
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()

    # detect R paddle misses
    if pong.xcor() > 380:
        pong.reset_position()
        pong.bounce_x()
        score.l_point()

    # detect L paddle misses
    if pong.xcor() < -390:
        pong.reset_position()
        pong.bounce_x()
        score.r_point()


screen.exitonclick()

