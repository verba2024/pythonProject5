import turtle
border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.penup()
border.goto(-600, 0)
border.pendown()
border.goto(600, 0)

turtle.shape("circle")
turtle.tracer(0)
x, y = 0, 0
vx, vy = 5, 80
a = -9.81
for i in range(60000):
    if y <= 0:
        vy = abs(vy) * 0.8
    x += vx * 0.01
    y += vy * 0.01 + a * 0.01**2 / 2
    vy += a * 0.01
    turtle.goto(x, y)
turtle.update()

turtle.getscreen()._root.mainloop()
