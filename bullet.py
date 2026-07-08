import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    # Check player.py
    rect: pygame.Rect | pygame.FRect
    
    def __init__(self, x: int, y: int, image: pygame.Surface):
        super().__init__()
        self.image: pygame.Surface = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
    
    def update(self):
        self.rect.bottom += 5