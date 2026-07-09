from scripts.bullet import Bullet
import pygame
from pygame.locals import *
from settings import *
from utils import load_sprite

class Player(pygame.sprite.Sprite):
    # Ty will scream at me because pygame.Sprite defaults it to None
    # A band-aid until it gets fixed
    rect: pygame.Rect | pygame.FRect
    
    def __init__(self, x: int | float, y: int | float):
        super().__init__()
        self.image: pygame.Surface = load_sprite("rocket")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.movespeed = 250
        
        self.bullet_y_offset = 5

        self.shot_dt_count = 0
        self.shot_dt_interval = 0.25
    
    def update(self, dt: int | float, bullet_group: pygame.sprite.Group):
        self.shot_dt_count += dt

        pressed = pygame.key.get_pressed()
        pressing_left = pressed[K_a] or pressed[K_LEFT]
        pressing_right = pressed[K_d] or pressed[K_RIGHT]

        if pressing_left and pressing_right:
            pass
        elif pressing_left and self.rect.left > 0:
            self.rect.x -= self.movespeed * dt
        elif pressing_right and self.rect.right < WIDTH:
            self.rect.x += self.movespeed * dt
        
        if pressed[K_SPACE] and self.shot_dt_count >= self.shot_dt_interval:
            bullet = self.shoot()
            bullet_group.add(bullet)
            self.shot_dt_count = 0
    
    def shoot(self):
        x = self.rect.centerx
        y = self.rect.top + self.bullet_y_offset
        return Bullet(x, y)
        
