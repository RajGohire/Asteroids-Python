import turtle
from Constants import *

window = turtle.Screen()
window.setup(width = WIDTH, height = HEIGHT)
window.title("Asteroisds")
window.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
# pen.shape()
# pen.color("white")
pen.penup()
pen.hideturtle()

# Clear the screen
# pen.clear()
window.tracer(0)
window.update()

# window.mainlooop()