from random import randint
import turtle as t


t.shape("turtle")
t.speed(10)
while True:
    t.forward(randint(0, 60))
    t.left(randint(-180, 180))
