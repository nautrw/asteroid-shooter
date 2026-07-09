import pygame
from pygame.locals import *
from settings import *
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
    
    def update(self):
        if not 0 < self.rect.top < HEIGHT:
            self.kill()
        else:
            self.rect.bottom -= BULLET_SPEED