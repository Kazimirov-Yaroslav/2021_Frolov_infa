import turtle as t
import numpy as np


def move(angle, length, pen):
    if pen == 0:
        t.penup()
    else:
        t.pendown()
    t.left(angle)
    t.forward(length * 40)


tup = (((0, 2, 1), (90, 1, 1), (90, 2, 1), (90, 1, 1), (90, 0, 1)),
       ((0, 1, 0), (135, np.sqrt(2), 1), (-135, 2, 1)),
       ((90, 1, 1), (-90, 1, 1), (-45, np.sqrt(2), 1), (135, 1, 1), (-90, 0, 1)),
       ((90, 1, 1), (-135, np.sqrt(2), 1), (135, 1, 1), (-135, np.sqrt(2), 1), (45, 0, 1)),
       ((0, 1, 1), (90, 1, 1), (-90, -1, 1), (0, 2, 1)),
       ((90, 1, 1), (0, -1, 1), (-90, 1, 1), (90, 1, 1), (-90, 1, 1), (-90, 1, 1), (90, 0, 1)),
       ((90, 1, 0), (-135, np.sqrt(2), 1), (45, 1, 1), (90, 1, 1), (90, 1, 1), (90, 1, 1), (90, 0, 1)),
       ((90, 1, 1), (-135, np.sqrt(2), 1), (45, 1, 1)),
       ((0, 2, 1), (90, 1, 1), (90, 2, 1), (90, 1, 1), (90, 1, 1), (90, 1, 1), (-90, 0, 1)),
       ((45, np.sqrt(2), 0), (135, 1, 1), (90, 1, 1), (90, 1, 1), (90, 1, 1), (-135, np.sqrt(2), 1), (45, 0, 1)))

A = list(str(input()))

t.shape("turtle")
t.color("blue")
t.speed(5)

t.penup()
t.goto(-280, 0)
t.pendown()
t.right(90)

for i in A:
    x = t.xcor()
    y = t.ycor()
    for j in tup[int(i)]:
        move(j[0], j[1], j[2])
    t.penup()
    t.goto(x + 80, y)
t.exitonclick()
