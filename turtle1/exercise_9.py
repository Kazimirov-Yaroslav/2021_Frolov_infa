import turtle as t
import numpy as np


def draw(n, radius):
    t.left(90 * (n - 2) / n)
    for _ in range(n):
        t.left(360 / n)
        t.forward(2 * radius * np.sin(np.pi / n))
    t.right(90 * (n - 2) / n)


t.shape("turtle")
t.speed(5)
n = 3
r = 20
for i in range(11):
    draw(n + i, r + 12 * i)
    t.penup()
    t.forward(12)
    t.pendown()
t.exitonclick()
