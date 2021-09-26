import turtle as t
import numpy as np


def circle(r):
    for _ in range(50):
        t.forward(np.pi * 2 * r / 100)
        t.left(360 / 100)


t.shape("turtle")
t.speed(0)
t.penup()
t.forward(100)
t.pendown()
r1 = 40
r2 = 10
t.left(90)
i = 0

for _ in range(5):
    circle(r1)
    circle(r2)

t.exitonclick()
