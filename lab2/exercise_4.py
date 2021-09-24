import turtle as t
import numpy as np


def par(sp_x, sp_y, acceleration):
    while t.ycor() > 0:
        t.goto(t.xcor() + 0.05 * sp_x, t.ycor() + 0.05 * sp_y - acceleration * 0.05 ** 2 / 2)
        sp_y -= 0.01 * acceleration


k = float(input())
theta = float(input())
theta = theta * np.pi / 180
v = 30
ay = 15
vx = v * np.cos(theta)
vy = v * np.sin(theta)

t.shape("circle")
t.speed(0)
t.forward(500)
t.backward(1000)
i = 0
while True:
    t.goto(t.xcor(), t.ycor() + 1)
    par(vx * np.sqrt(k) ** i, vy * np.sqrt(k) ** i, ay)
    i += 1
