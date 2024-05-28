import turtle

f = open('../z.txt', 'r')
writer = [0]*10
for i in range(10):
    s = f.readline()
    s = list(map(int, s.split()))
    print(s, len(s))
    mind = [0]*(len(s)//2)
    print(mind)
    for j in range(0, len(s), 2):
        mind[j//2] = [s[j], s[j+1]]
    writer[i] = mind  # список из всех пар элементов
    print(writer[i])

turtle.shape('turtle')
turtle.tracer(2)
ind = '141100'
mind = [0]*len(ind)
for i in range(len(ind)):
    mind[i] = int(ind[i])  # список чисел, входящих в индекс
print(mind)
x = 0
y = 0
xend = 0

turtle.hideturtle()
for i in range(len(ind)):
    xend = x + 30
    if mind[i] == 1:
        y -= 20
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('blue')
    for j in range(len(writer[mind[i]])): # делим координаты на пары x y
        # writer[mind[i]][j][0] - 1 элемент в паре(x)
        # print(writer[mind[i]][j][1]) - 2 элемент в паре(y)
        turtle.goto(x+writer[mind[i]][j][0], writer[mind[i]][j][1])
    turtle.penup()
    y = 0
    x = xend
turtle.done()
