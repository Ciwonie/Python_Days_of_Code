import turtle as t
from turtle import Screen
import random

t.colormode(255)

tut = t.Turtle()
tut.shape("turtle")

turtle_colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
                 "SeaGreen"]
directions = [0, 90, 180, 270]
tut.pensize(15)
tut.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(200):
    tut.color(random_color())
    tut.forward(30)
    tut.setheading(random.choice(directions))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Screen()
    screen.screensize(2000,1500)
    screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/











# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tut.forward(100)
#         tut.right(angle)
#
#
# for n in range(3, 11):
#     tut.color(random.choice(turtle_colors))
#     draw_shape(n)
