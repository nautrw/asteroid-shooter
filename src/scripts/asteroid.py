import pygame
from pygame.locals import *
from utils import load_sprite
from random import randint

class Asteroid(pygame.sprite.Sprite):
    # player.py
    rect: pygame.Rect | pygame.FRect
    
    def __init__(self, x: int | float, y: int | float):
        super().__init__()
        self.image: pygame.Surface = load_sprite(f"asteroid{randint(1, 3)}")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.speed = 250

    
    def update(self, dt: int | float, screen_height: int, damage_callback: function, reset_callback: function):
        if self.rect.bottom >= screen_height:
            damage_callback(reset_callback)
            self.kill()
        else:
            self.rect.bottom += self.speed * dt
