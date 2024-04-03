import turtle #упражнение1
from random import randint
t=turtle.Turtle()

t.shape('turtle')
t.color("red")
for i in range(0, 200, 1):
    a=randint(0, 360)
    t.left(a)
    b=randint(10, 50)
    t.forward(b)