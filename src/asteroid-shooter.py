import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.asteroid import Asteroid
from settings import *
import random

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player((WIDTH // 2), (HEIGHT - 10))
player_shot_dt_count = 0

bullets = pygame.sprite.Group()

asteroids = pygame.sprite.Group()
asteroid_dt_count = 0

dt = 0

running = True

while running:
    SCREEN.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    if asteroid_dt_count >= ASTEROID_DT_SPAWN_INTERVAl:
        asteroid = Asteroid(random.randint(0, WIDTH), 0)
        asteroids.add(asteroid)
        asteroid_dt_count = 0
    
    pygame.sprite.groupcollide(bullets, asteroids, True, True)

    player.update(dt, bullets)
    SCREEN.blit(player.image, player.rect)  # ty:ignore[invalid-argument-type]

    bullets.update(dt)
    bullets.draw(SCREEN)

    asteroids.update()
    asteroids.draw(SCREEN)
    
    pygame.display.flip()
    dt = clock.tick(FPS) / 1000
    asteroid_dt_count += dt

pygame.quit()
