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
            if event.key == K_SPACE and player_shot_dt_count >= PLAYER_SHOOT_COOLDOWN:
                bullet = player.shoot()
                bullets.add(bullet)
                entities.add(bullet)
                player_shot_dt_count = 0
    
    if asteroid_dt_count >= ASTEROID_DT_SPAWN_INTERVAl:
        asteroid = Asteroid(random.randint(0, WIDTH), 0)
        asteroids.add(asteroid)
        entities.add(asteroid)
        asteroid_dt_count = 0
    
    pygame.sprite.groupcollide(bullets, asteroids, True, True)
    
    entities.update()
    entities.draw(SCREEN)
    
    pygame.display.flip()
    dt = clock.tick(FPS)
    asteroid_dt_count += dt
    player_shot_dt_count += dt

pygame.quit()