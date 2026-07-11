import pygame
from pygame.locals import *
from utils import load_sprite

class Bullet(pygame.sprite.Sprite):
    # Check player.py
    rect: pygame.Rect | pygame.FRect
    
    def __init__(self, x: int | float, y: int | float):
        super().__init__()
        self.image: pygame.Surface = load_sprite('bullet')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        # I multiply this by 100 because it bothers me to have such high
        # arbitrary values; delta-time is very low
        self.speed = 5
    
    def update(self, dt: int | float, screen_height: int):
        if not 0 < self.rect.top < screen_height:
            self.kill()
        else:
            self.rect.bottom -= self.speed * 100 * dt
