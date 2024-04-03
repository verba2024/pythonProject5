import pygame
from pygame.draw import *
from random import randint,choice
import math

# Инициализация Pygame
pygame.init()

FPS = 60
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (10, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 100)
BLACK = (0, 0, 29)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Параметры шариков
NUM_BALLS = 10
balls = []

# Счетчик очков
click_count = 0

def new_ball():
    '''Создает новый шарик со случайными параметрами.'''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = choice(COLORS)
    dx, dy = randint(-5, 5), randint(-5, 5)
    return [x, y, r, color, dx, dy]

def draw_ball(ball):
    '''Рисует шарик на экране.'''
    circle(screen, ball[3], (ball[0], ball[1]), ball[2])

def move_ball(ball):
    '''Отражает шарик от стен.'''
    ball[0] += ball[4]
    ball[1] += ball[5]

    # Отражение от левой и правой стен
    if ball[0] <= ball[2] or ball[0] >= WIDTH - ball[2]:
        ball[4] = -ball[4]

    # Отражение от верхней и нижней стен
    if ball[1] <= ball[2] or ball[1] >= HEIGHT - ball[2]:
        ball[5] = -ball[5]

def check_click(event,ball):
    '''Проверяет, попала ли мышка по шарику'''
    len_c = math.sqrt((event.pos[0] - ball[0])**2 + (event.pos[1] - ball[1])**2)
    return len_c < ball[2]

def check_click2(event,ball):
    '''Проверяет, не попал ли клик в шарик'''
    len_c = math.sqrt((event.pos[0] - ball[0])**2 + (event.pos[1] - ball[1])**2)
    return len_c > ball[2]

# Создаем начальные шарики
for _ in range(NUM_BALLS):
    balls.append(new_ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if check_click(event, ball):
                    balls.remove(ball)
                    balls.append(new_ball())
                    click_count += 1
            print(click_count)



    screen.fill(BLACK)
    x, y = 10, 20
    clicker = pygame.font.Font(None, 64)
    click = clicker.render(str(click_count), True, (255, 255, 255))
    screen.blit(click, (x, y))
    for ball in balls:
        draw_ball(ball)
        move_ball(ball)
    pygame.display.update()

pygame.quit()