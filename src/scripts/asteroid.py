import pygame
from settings import *
from pygame.locals import *

class Asteroid(pygame.sprite.Sprite):
    # player.py
    rect: pygame.Rect | pygame.FRect
    
    def __init__(self, x: int | float, y: int | float, image: pygame.Surface):
        super().__init__()
        self.image: pygame.Surface = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
    
    def update(self):
        if self.rect.bottom >= HEIGHT:
            self.kill()
        else:
            self.rect.bottom += ASTEROID_SPEED