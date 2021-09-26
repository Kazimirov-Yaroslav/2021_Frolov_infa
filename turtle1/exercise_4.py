import numpy as np
import turtle as t

t.shape('turtle')
t.speed(0)
for _ in range(100):
    t.forward(np.pi * 150 / 100)
    t.left(360 / 100)
t.exitonclick()
