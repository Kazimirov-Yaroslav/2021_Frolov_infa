from random import randint
import turtle as t


t.shape("turtle")
t.speed(0)
t.penup()
t.goto(-300, -300)
t.pensize(5)
t.pendown()
for _ in range(4):
    t.forward(600)
    t.left(90)

number_of_turtles = 25
dT = 0.01
speed = 250

pool = [[t.Turtle(shape='turtle'), randint(-speed, speed), randint(-speed, speed)] for _ in range(number_of_turtles)]
print(type(pool))
for unit in pool:
    unit[0].penup()
    unit[0].shape("circle")
    size = randint(20, 60) / 100
    unit[0].shapesize(size)
    unit[0].speed(0)
    unit[0].goto(randint(-290, 290), randint(-290, 290))

while True:
    for unit in pool:
        x_cor = unit[0].xcor()
        y_cor = unit[0].ycor()
        if x_cor > 290 or x_cor < -290:
            unit[1] = unit[1] * (-1)
        if y_cor > 290 or y_cor < -290:
            unit[2] = unit[2] * (-1)
        for elem in pool:
            if elem != unit:
                distance = unit[0].distance(elem[0].xcor(), elem[0].ycor())
                if distance <= 10:
                    unit[1] += elem[1]
                    elem[1] = unit[1] - elem[1]
                    unit[1] -= elem[1]
                    unit[2] += elem[2]
                    elem[2] = unit[2] - elem[2]
                    unit[2] -= elem[2]
        unit[0].goto(unit[0].xcor() + dT * unit[1], unit[0].ycor() + dT * unit[2])
