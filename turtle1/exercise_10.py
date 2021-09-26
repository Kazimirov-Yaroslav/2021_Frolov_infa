import turtle as t
import numpy as np


def circle(radius):
    for _ in range(100):
        t.forward(np.pi * 2 * radius / 100)
        t.left(360 / 100)


t.shape("turtle")
t.speed(50)
r = 40

for _ in range(6):
    circle(r)
    t.left(60)
t.exitonclick()
