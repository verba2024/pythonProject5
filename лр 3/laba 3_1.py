import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((225, 225, 225))
circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 2)
rect(screen, (0, 0, 0),(125, 270, 150, 25))
circle(screen, (255, 0, 0), (275, 150), 35)
circle(screen, (255, 0, 0), (125, 150), 40)
circle(screen, (0, 0, 0), (275, 150), 35, 2)
circle(screen, (0, 0, 0), (125, 150), 40, 2)
circle(screen, (0, 0, 0), (275, 150), 15)
circle(screen, (0, 0, 0), (125, 150), 20)
line(screen, (0, 0, 0), (225, 125), (350, 90), width = 20)
line(screen, (0, 0, 0), (20, 60), (200, 125), width=20)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
