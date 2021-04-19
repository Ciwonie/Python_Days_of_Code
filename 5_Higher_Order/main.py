# this is a higher order and event listener test
# higher order functions are functions that work with other functions

"""
A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an
output i.e, the functions that operate with another function are known as Higher order Functions. It is worth knowing
that this higher order function is applicable for functions and methods as well that takes functions as a parameter
or returns a function as a result. Python too supports the concepts of higher order functions.

Properties of higher-order functions:

    A function is an instance of the Object type.
    You can store the function in a variable.
    You can pass the function as a parameter to another function.
    You can return the function from a function.
    You can store them in data structures such as hash tables, lists, …
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()