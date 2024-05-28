import random
from random import randint
import turtle
import math

MAP_HALF_WIDTH = 300  # ширина сосуда
MAP_HALF_HEIGHT = 300  # высота сосуда


# ОТРИСОВКА СОСУДА ДЛЯ ГАЗА
def draw():
    border = turtle.Turtle()
    border.speed(0)
    border.pensize(2)
    border.hideturtle()
    border.up()
    border.goto(MAP_HALF_WIDTH, MAP_HALF_HEIGHT)
    border.pendown()
    border.goto(MAP_HALF_WIDTH, -MAP_HALF_HEIGHT)
    border.goto(-MAP_HALF_WIDTH, -MAP_HALF_HEIGHT)
    border.goto(-MAP_HALF_WIDTH, MAP_HALF_HEIGHT)
    border.goto(MAP_HALF_WIDTH, MAP_HALF_HEIGHT)


number_of_turtles = 20
balls = []  # список мячей

draw()  # ОТРИСОВКА СОСУДА ДЛЯ ГАЗА

pool = [turtle.Turtle(shape='circle', visible=False) for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(0)
    shape_vecs = unit.get_shapepoly()
    shape_radius = 0
    for vec in shape_vecs:
        shape_radius = max(*vec, shape_radius)
    vx = random.randint(-15, 15)
    vy = random.randint(-15, 15)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.showturtle()
    balls.append([unit, vx, vy, shape_radius])


def check_in_bounds(ball1, ball2):
    return abs(ball2[0].position() - ball1[0].position()) \
        <= ball1[3] + ball2[3]


def clamp(x, bottom, top):
    return max(bottom, min(x, top))  # top-верхний предел значения косинуса угла


def get_angle_between(ball1, ball2):  # считаем угол между векторами через скалярное произведение
    vel1 = (ball1[1], ball1[2])
    vel2 = (ball2[1], ball2[2])

    len1 = math.sqrt(vel1[0]**2 + vel1[1]**2)
    len2 = math.sqrt(vel2[0]**2 + vel2[1]**2)

    scalar = vel1[0] * vel2[0] + vel1[1] * vel2[1]  # скалярное произведение координат мячей
    return math.acos(clamp(scalar / (len1 * len2), -1, 1))  # возвращаем угол между векторами


while True:
    for unit in pool:
        for ball in balls:
            x, y = ball[0].position()
            collided = filter(  # фильтруем мячики на столкновение(ну типа того)
                lambda ball2: ball2 != ball and check_in_bounds(ball, ball2),
                balls
            )
            for ball2 in collided:  # для прошедших отбор
                angle = get_angle_between(ball, ball2)  # читав угол
                vel1 = math.sqrt(ball[1]**2 + ball[2]**2)  # для 1 мяча
                ball[1] = -math.cos(angle) * vel1  # скорость 1 мяча по x
                ball[2] = math.sin(angle) * vel1  # скорость 1 мяча по y
                vel2 = math.sqrt(ball2[1]**2 + ball2[2]**2)  # для 2 мяча
                ball2[1] = math.cos(angle) * vel2  # скорость 2 мяча по x
                ball2[2] = -math.sin(angle) * vel2  # скорость 2 мяча по y
            if x + ball[1] >= MAP_HALF_WIDTH - ball[3] or \
               x + ball[1] <= -MAP_HALF_WIDTH + ball[3]:
                ball[1] *= -1  # vx
            if y + ball[2] >= MAP_HALF_HEIGHT - ball[3] or \
               y + ball[2] <= -MAP_HALF_HEIGHT + ball[3]:
                ball[2] *= -1  # vy
            ball[0].goto(x + ball[1], y + ball[2])

turtle.done()
