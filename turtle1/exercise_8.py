import turtle as t

t.shape('turtle')
t.speed(10)
for i in range(40):
    t.forward(10 + i * 10)
    t.left(90)
t.exitonclick()
