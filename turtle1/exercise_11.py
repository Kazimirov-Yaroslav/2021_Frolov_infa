import turtle as t
import numpy as np


def circle(radius, direction):
    for _ in range(100):
        t.forward(np.pi * 2 * radius / 100)
        t.left(360 / 100 * direction)


t.shape("turtle")
t.speed(0)
r = 20
t.left(90)

for i in range(10):
    circle(r + 10 * (i // 2), (-1) ** i)
t.exitonclick()
