import pygame
from pygame.locals import *

WIDTH = 400
HEIGHT = 800
FPS = 60

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()