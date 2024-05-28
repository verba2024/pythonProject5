import pygame
from pygame.draw import *
from random import randint,choice
import math

pygame.init()

FPS = 60
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (10, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 100)
BLACK = (0, 0, 29)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls_count = 9
balls = []

# Счетчик очков
click_count = 0

def new_ball():
    '''создаем новый шарик'''
    x = randint(100, 1000)
    y = randint(100, 800)
    r = randint(10, 90)
    color = choice(COLORS)
    dx, dy = randint(-8, 8), randint(-8, 8)
    return [x, y, r, color, dx, dy]

def draw_ball(ball):
    '''Рисует шарик'''
    circle(screen, ball[3], (ball[0], ball[1]), ball[2])

def dball(ball):
    '''Отражает шар'''
    ball[0] += ball[4]
    ball[1] += ball[5]

    # По x
    if ball[0] <= ball[2] or ball[0] >= WIDTH - ball[2]:
        ball[4] = -ball[4]

    # По y
    if ball[1] <= ball[2] or ball[1] >= HEIGHT - ball[2]:
        ball[5] = -ball[5]

def check_mouse(event, ball):
    '''
    Проверяет, попала ли мышка в шарик
    '''
    vec_x = (event.pos[0] - ball[0])**2
    vec_y = (event.pos[1] - ball[1]) ** 2
    len_c = math.sqrt(vec_x + vec_y)
    if len_c <= ball[2]:
        return 1
    else:
        return 0

# Создаем шарики на экране
for i in range(balls_count):
    balls.append(new_ball())  # берем параметры мячей из функции

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # если мышка по мячу
            for ball in balls:  # для мячей
                if check_mouse(event, ball):  # если попал мышкой
                    balls.remove(ball)
                    balls.append(new_ball())
                    click_count += 1
            print(click_count)

    screen.fill(BLACK)
    x, y = 10, 20  # корды для счетчика
    clicker = pygame.font.Font(None, 64)
    click = clicker.render(str(click_count), True, (255, 255, 255))
    screen.blit(click, (x, y))
    for ball in balls:
        draw_ball(ball)
        dball(ball)
    pygame.display.update()

pygame.quit()