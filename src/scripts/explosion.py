import pygame as pg
from pygame.locals import *
from utils import load_sprite

class Explosion(pg.sprite.Sprite):
    # check player.py
    rect: pg.Rect | pg.FRect

    def __init__(self, x: int | float, y: int | float):
        super().__init__()
        self.image: pg.Surface = load_sprite("explosion")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        self.lifespan = 0.1
        self.lifespan_dt_count = 0

    def update(self, dt: int | float):
        self.lifespan_dt_count += dt
        print(self.lifespan_dt_count)

        if self.lifespan_dt_count >= self.lifespan:
            self.kill()
