import pygame
from pygame.locals import *
from player import Player

WIDTH = 400
HEIGHT = 800
FPS = 60

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

rocket_sprite = pygame.image.load("sprites/rocket.png").convert()
player = Player((WIDTH // 2), (HEIGHT - 10), rocket_sprite)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    entities = pygame.sprite.Group()
    entities.add(player)
    
    entities.draw(SCREEN)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()