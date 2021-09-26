import turtle as t
import numpy as np


def circle(radius, x_st, y_st, color):
    t.penup()
    t.goto(x_st, y_st)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    for _ in range(100):
        t.forward(2 * np.pi * radius / 100)
        t.left(360 / 100)
    t.end_fill()


R = 150
t.shape("turtle")
t.speed(50)
circle(R, 0, -R, "yellow")
circle(R / 7.5, R * 0.4, R * 0.4, "blue")
circle(R / 7.5, -R * 0.4, R * 0.4, "blue")
t.penup()
t.goto(0, 0.22 * R)
t.pendown()
t.width(7)
t.right(90)
t.forward(0.44 * R)
t.penup()
t.goto(-0.45 * R, -0.3 * R)
t.pendown()
t.color("red")
for _ in range(50):
    t.forward(2 * np.pi * 0.45 * R / 100)
    t.left(360 / 100)
t.exitonclick()
