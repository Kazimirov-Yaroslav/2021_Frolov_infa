import turtle as t

t.shape('turtle')
t.speed(0)
a = 0
i = 0

while a < 5000:
    t.forward(10 * 1 / 57.3 * (10 + (a / 57.3) ** 2) ** 0.5)
    t.left(1)
    a += 1

t.exitonclick()
