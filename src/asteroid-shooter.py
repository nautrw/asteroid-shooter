import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.bullet import Bullet
from settings import *
import os

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SPRITES = os.path.join('src', 'assets', 'sprites')

bullet_sprite = pygame.image.load(os.path.join(SPRITES, 'bullet.png')).convert()
rocket_sprite = pygame.image.load(os.path.join(SPRITES, "rocket.png")).convert()
player = Player((WIDTH // 2), (HEIGHT - 10), rocket_sprite)

entities = pygame.sprite.Group()
entities.add(player)

bullets = pygame.sprite.Group()

running = True

while running:
    SCREEN.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.shoot(bullet_sprite, bullets)
    
    bullets.update()
    bullets.draw(SCREEN)
    
    entities.update()
    entities.draw(SCREEN)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()