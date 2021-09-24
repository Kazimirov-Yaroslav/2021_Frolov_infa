import turtle as t


def move(angle, length, pen):
    if pen == 0:
        t.penup()
    else:
        t.pendown()
    t.left(angle)
    t.forward(length * 40)


A = list(str(input()))

t.shape("turtle")
t.color("blue")
t.speed(5)

t.penup()
t.goto(-280, 0)
t.pendown()
t.right(90)

for i in A:
    with open("ex3.txt") as f:
        code = f.readlines()[int(i)]

    code = code.replace("(", "")
    code = code.replace(")", "")
    code = code.replace("\n", "")
    code = code.split(", ")

    x = t.xcor()
    y = t.ycor()
    for j in range(len(code) // 3):
        move(float(code[j * 3]), float(code[j * 3 + 1]), float(code[j * 3 + 2]))
    t.penup()
    t.goto(x + 80, y)

t.exitonclick()
