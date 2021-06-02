import pygame
from pygame.locals import *

import sys


pygame.init()

RED = (239, 71, 111)
YELLOW = (255, 209, 102)
GREEN = (6, 214, 160)
BLUE = (0, 0, 178)
BLACK = (0, 0, 0)


HEIGHT = 450
WIDTH = 400


FramePerSec = pygame.time.Clock()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


def drawText(win, letter: str, pos, color):
    font = pygame.font.SysFont(None, 90)
    img = font.render(letter, True, color)
    img_rect = img.get_rect(
        center=pygame.Rect(50 + pos[0] * 100, 100 + pos[1] * 100, 100, 100).center
    )
    win.blit(img, img_rect)

poses = []
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            print(event)
            pos = ((event.pos[0] - 50) // 100, (event.pos[1] - 100) // 100)
            if (pos[0] in range(3)) and (pos[1] in range(3)) and not(pos in poses):
                poses.append(pos)

    pygame.draw.rect(win, BLACK, (0, 0, WIDTH, HEIGHT))
    pygame.draw.rect(win, GREEN, (50, 100, 300, 300), 3, 30)
    pygame.draw.line(win, GREEN, (150, 100), (150, 400), 3)
    pygame.draw.line(win, GREEN, (250, 100), (250, 400), 3)
    pygame.draw.line(win, GREEN, (50, 200), (350, 200), 3)
    pygame.draw.line(win, GREEN, (50, 300), (350, 300), 3)

    for pos in poses:
        drawText(win, "X", pos, RED)


    pygame.display.update()
