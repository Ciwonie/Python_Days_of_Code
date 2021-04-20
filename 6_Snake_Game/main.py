"""
Thinking about creating this game:
Start by planning the shape of the snake! Start with 3 squares, approx. 20px.

                        Project Goals:
1. Create a snake body          5. create a scoreboard
2. move the snake               6. detect collision with wall
3. create snake food            7. detect collision with tail
4. Detect collision with food
"""

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_is_on = True

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
# GOAL 1 COMPLETE 20 APR 21

screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()



