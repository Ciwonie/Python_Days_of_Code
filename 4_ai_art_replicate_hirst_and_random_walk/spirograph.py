import turtle
import random

turtle.colormode(255)
tut = turtle.Turtle()

tut.shape("turtle")
tut.speed("fastest")

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tut.color(random_color())
        tut.circle(radius=100, extent=None, steps=None)
        current_heading = tut.heading()
        tut.setheading(current_heading + size_of_gap)


if __name__ == "__main__":
    draw_spirograph(1)
    screen = turtle.Screen()
    screen.screensize(2000, 1500)
    screen.exitonclick()
