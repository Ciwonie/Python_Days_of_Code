"""
Thinking about creating this game:
Start by planning the shape of the snake! Start with 3 squares, approx. 20px.

                        Project Goals:
1. Create a snake body          5. create a scoreboard
2. move the snake               6. detect collision with wall
3. create snake food            7. detect collision with tail
4. Detect collision with food
"""
# GOAL 1 COMPLETE 20 APR 21
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()



