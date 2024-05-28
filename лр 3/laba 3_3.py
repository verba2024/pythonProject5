import pygame
from pygame.draw import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 69, 0, 255)
BEIGE = (245, 245, 220, 255)
VIOLET = (238, 130, 238, 255)
GREEN = (0, 255, 0)
BROWN = (100, 40, 0)
RED = (255, 0, 0)
LIGHTBLUE = (173, 216, 230, 255)
BLUE = (0, 0, 255, 255)
YELLOW = (255, 255, 0, 255)
DARKGREEN = (0, 100, 0, 255)

FPS = 30
screen = pygame.display.set_mode((1200, 600))
screen.fill(WHITE)
# ПЕРВЫЙ ЧЕЛОВЕК
ellipse(screen, DARKGREEN, (145, 410, 330, 350))
ellipse(screen, BEIGE, (180, 160, 250, 300))

circle(screen, BLACK, (260, 280), 10)  # глаз слева
circle(screen, BLACK, (350, 280), 10)  # глаз справа
circle(screen, LIGHTBLUE, (260, 280), 25, 15)
circle(screen, LIGHTBLUE, (350, 280), 25, 15)
circle(screen, BLACK, (260, 280), 25, 1)
circle(screen, BLACK, (350, 280), 25, 1)

polygon(screen, BROWN, [(290, 310), (320, 310), (305, 340)])  # нос

polygon(screen, RED, [(230, 350), (380, 350), (305, 400)])  # рот
polygon(screen, BLACK, [(230, 350), (380, 350), (305, 400)], 1)

# плечи
polygon(screen, DARKGREEN, ([(210, 400), (250, 450),
                (210, 510), (155, 490), (155, 420)]))
polygon(screen, BLACK, ([(210, 400), (250, 450),
                (210, 510), (155, 490), (155, 420)]), 1)
polygon(screen, DARKGREEN, ([(401, 400), (451, 420),
                (460, 490), (395, 510), (365, 440)]))
polygon(screen, BLACK, ([(401, 400), (451, 420),
                (460, 490), (395, 510), (365, 440)]), 1)

polygon(screen, BEIGE, ([(175, 412), (195, 405),  # ПРЕДПЛЕЧЬЯ
              (90, 100), (70, 105)]))
polygon(screen, BEIGE, ([(420, 407), (440, 416),
                (520, 100), (500, 93)]))

ellipse(screen, BEIGE, (60, 60, 50, 70))  # левая рука
ellipse(screen, BEIGE, (480, 60, 50, 70))  # правая рука

polygon(screen, YELLOW, [(170, 210), (210, 215), (190, 250)])  # 1
polygon(screen, BLACK, [(170, 210), (210, 215), (190, 250)], 1)
polygon(screen, YELLOW, [(183, 190), (225, 200), (200, 230)])  # 2
polygon(screen, BLACK, [(183, 190), (225, 200), (200, 230)], 1)
polygon(screen, YELLOW, [(196, 170), (240, 185), (210, 215)])  # 3
polygon(screen, BLACK, [(196, 170), (240, 185), (210, 215)], 1)
polygon(screen, YELLOW, [(215, 150), (255, 175), (225, 202)])  # 4
polygon(screen, BLACK, [(215, 150), (255, 175), (225, 202)], 1)
polygon(screen, YELLOW, [(245, 130), (290, 160), (240, 184)])  # 5
polygon(screen, BLACK, [(245, 130), (290, 160), (240, 184)], 1)
polygon(screen, YELLOW, [(295, 115), (325, 160), (270, 164)])  # 6
polygon(screen, BLACK, [(295, 115), (325, 160), (270, 164)], 1)
polygon(screen, YELLOW, [(345, 120), (355, 175), (300, 160)])  # 7
polygon(screen, BLACK, [(345, 120), (355, 175), (300, 160)], 1)
polygon(screen, YELLOW, [(400, 145), (395, 205), (340, 166)])  # 8
polygon(screen, BLACK, [(400, 145), (395, 205), (340, 166)], 1)
polygon(screen, YELLOW, [(440, 190), (420, 245), (380, 190)])  # 9
polygon(screen, BLACK, [(440, 190), (420, 245), (380, 190)], 1)

# ВТОРОЙ ЧЕЛОВЕК
k = 435

ellipse(screen, ORANGE, (145 + k, 410, 330, 350))
ellipse(screen, BEIGE, (180 + k, 160, 250, 300))

circle(screen, BLACK, (260 + k, 280), 10)  # глаз слева
circle(screen, BLACK, (350 + k, 280), 10)  # глаз справа
circle(screen, BLUE, (260 + k, 280), 25, 15)
circle(screen, BLUE, (350 + k, 280), 25, 15)
circle(screen, BLACK, (260 + k, 280), 25, 1)
circle(screen, BLACK, (350 + k, 280), 25, 1)

polygon(screen, BROWN, [(290 + k, 310), (320 + k, 310), (305 + k, 340)])  # нос

polygon(screen, RED, [(230 + k, 350), (380 + k, 350), (305 + k, 400)])  # рот
polygon(screen, BLACK, [(230 + k, 350), (380 + k, 350), (305 + k, 400)], 1)

# плечи
polygon(screen, ORANGE, ([(210 + k, 400), (250 + k, 450),
                (210 + k, 510), (155 + k, 490), (155 + k, 420)]))
polygon(screen, BLACK, ([(210 + k, 400), (250 + k, 450),
                (210 + k, 510), (155 + k, 490), (155 + k, 420)]), 1)
polygon(screen, ORANGE, ([(401 + k, 400), (451 + k, 420),
                (460 + k, 490), (395 + k, 510), (365 + k, 440)]))
polygon(screen, BLACK, ([(401 + k, 400), (451 + k, 420),
                (460 + k, 490), (395 + k, 510), (365 + k, 440)]), 1)

polygon(screen, BEIGE, ([(175 + k, 412), (195 + k, 405),  # ПРЕДПЛЕЧЬЯ
              (90 + k, 100), (70 + k, 105)]))
polygon(screen, BEIGE, ([(420 + k, 407), (440 + k, 416),
                (520 + k, 100), (500 + k, 93)]))

ellipse(screen, BEIGE, (60 + k, 60, 50, 70))  # левая рука
ellipse(screen, BEIGE, (480 + k, 60, 50, 70))  # правая рука

polygon(screen, VIOLET, [(170 + k, 210), (210 + k, 215), (190 + k, 250)])  # 1
polygon(screen, BLACK, [(170 + k, 210), (210 + k, 215), (190 + k, 250)], 1)
polygon(screen, VIOLET, [(183 + k, 190), (225 + k, 200), (200 + k, 230)])  # 2
polygon(screen, BLACK, [(183 + k, 190), (225 + k, 200), (200 + k, 230)], 1)
polygon(screen, VIOLET, [(196 + k, 170), (240 + k, 185), (210 + k, 215)])  # 3
polygon(screen, BLACK, [(196 + k, 170), (240 + k, 185), (210 + k, 215)], 1)
polygon(screen, VIOLET, [(215 + k, 150), (255 + k, 175), (225 + k, 202)])  # 4
polygon(screen, BLACK, [(215 + k, 150), (255 + k, 175), (225 + k, 202)], 1)
polygon(screen, VIOLET, [(245 + k, 130), (290 + k, 160), (240 + k, 184)])  # 5
polygon(screen, BLACK, [(245 + k, 130), (290 + k, 160), (240 + k, 184)], 1)
polygon(screen, VIOLET, [(295 + k, 115), (325 + k, 160), (270 + k, 164)])  # 6
polygon(screen, BLACK, [(295 + k, 115), (325 + k, 160), (270 + k, 164)], 1)
polygon(screen, VIOLET, [(345 + k, 120), (355 + k, 175), (300 + k, 160)])  # 7
polygon(screen, BLACK, [(345 + k, 120), (355 + k, 175), (300 + k, 160)], 1)
polygon(screen, VIOLET, [(400 + k, 145), (395 + k, 205), (340 + k, 166)])  # 8
polygon(screen, BLACK, [(400 + k, 145), (395 + k, 205), (340 + k, 166)], 1)
polygon(screen, VIOLET, [(440 + k, 190), (420 + k, 245), (380 + k, 190)])  # 9
polygon(screen, BLACK, [(440 + k, 190), (420 + k, 245), (380 + k, 190)], 1)

line(screen, GREEN, (50, 60), (965, 60), width=75)
polygon(screen, BLACK, [(50, 23), (965, 23), (965, 98), (50, 98)], 1)
# текст на табличке
font = pygame.font.SysFont("comicsansms", 61)
text = font.render("PYTHON is REALLY AMAZING!", 1,  BLACK)
screen.blit(text, (50, 25))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
