import turtle as t

t.shape('turtle')
t.speed(0)
for i in range(10):
    for _ in range(4):
        t.forward(50 + 20 * i)
        t.left(90)
    t.penup()
    t.right(135)
    t.forward(10 * 2 ** 0.5)
    t.left(135)
    t.pendown()
t.exitonclick()
