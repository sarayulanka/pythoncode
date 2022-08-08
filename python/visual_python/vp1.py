import pygame
import sys
from pygame.locals import *

# initialize pygame
pygame.init()

window_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("my board")

# Define colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
PINK = (255, 192, 203)
RED = (240, 128, 128)
PURPLE = (230, 230, 250)
window_surface.fill(WHITE)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            center = pygame.mouse.get_pos()
            if center[0] <= 250 and center[1] <= 250:
                pygame.draw.circle(window_surface, PURPLE, center, 10, 0)
                pygame.display.update()
            if center[0] > 250 and center[1] <= 250:
                pygame.draw.circle(window_surface, BLUE, center, 10, 0)
                pygame.display.update()
            if center[0] <= 250 and center[1] > 250:
                pygame.draw.circle(window_surface, RED, center, 10, 0)
                pygame.display.update()
            if center[0] > 250 and center[1] > 250:
                pygame.draw.circle(window_surface, PINK, center, 10, 0)
                pygame.display.update()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
