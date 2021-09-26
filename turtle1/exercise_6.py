import turtle as t

t.shape('turtle')
t.speed(50)
n = int(input())
for _ in range(n):
    t.forward(150)
    t.stamp()
    t.backward(150)
    t.left(360 / n)
t.exitonclick()
