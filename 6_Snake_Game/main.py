"""
Thinking about creating this game:
Start by planning the shape of the snake! Start with 3 squares, approx. 20px.

                        Project Goals:
1. Create a snake body          5. create a scoreboard
2. move the snake               6. detect collision with wall
3. create snake food            7. detect collision with tail
4. Detect collision with food
"""
# GOAL 1 COMPLETE 20 APR 21 WITH OOP
# GOAL 2 COMPLETE 20 APR 21
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()


screen.exitonclick()



