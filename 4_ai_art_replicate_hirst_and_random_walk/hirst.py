# damien hirst replica program
import turtle as stroke
import random
import colorgram

# change color scheme to rgb
stroke.colormode(255)
brush = stroke.Turtle()
# brush.pensize(15)
brush.shape("arrow")
brush.speed("fastest")
brush.penup()
brush.hideturtle()

'''removed the colorgram code because the most common colors from the jpg have been extracted in color_list'''
# colors = colorgram.extract('image.jpg', 13)
# palette = [(x.rgb[0], x.rgb[1], x.rgb[2]) for x in colors]

color_list = [(26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132)]
number_of_dots = 100

brush.setheading(225)
brush.forward(300)
brush.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    brush.dot(20, random.choice(color_list))
    brush.forward(50)

    if dot_count % 10 == 0:
        brush.setheading(90)
        brush.forward(50)
        brush.setheading(180)
        brush.forward(500)
        brush.setheading(0)


if __name__ == "__main__":
    screen = stroke.Screen()
    screen.screensize(2000, 1500)
    screen.exitonclick()

