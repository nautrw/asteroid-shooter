import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.bullet import Bullet
from scripts.asteroid import Asteroid
from settings import *
import os
import random

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SPRITES = os.path.join('src', 'assets', 'sprites')
bullet_sprite = pygame.image.load(os.path.join(SPRITES, 'bullet.png')).convert_alpha()
rocket_sprite = pygame.image.load(os.path.join(SPRITES, "rocket.png")).convert_alpha()
asteroid_sprite = pygame.image.load(os.path.join(SPRITES, 'asteroid.png')).convert_alpha()

player = Player((WIDTH // 2), (HEIGHT - 10), rocket_sprite)

entities = pygame.sprite.Group()
entities.add(player)

bullets = pygame.sprite.Group()

asteroids = pygame.sprite.Group()
asteroid_dt_count = 0

running = True

while running:
    SCREEN.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.shoot(bullet_sprite, bullets)
    
    if asteroid_dt_count >= ASTEROID_DT_SPAWN_INTERVAl:
        asteroid = Asteroid(random.randint(0, WIDTH), 0, asteroid_sprite)
        asteroids.add(asteroid)
        asteroid_dt_count = 0
    
    asteroids.update()
    asteroids.draw(SCREEN)
    
    bullets.update()
    bullets.draw(SCREEN)
    
    entities.update()
    entities.draw(SCREEN)
    
    pygame.display.flip()
    dt = clock.tick(FPS)
    asteroid_dt_count += dt

pygame.quit()