import pygame
from pygame.locals import *
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, image: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = image
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
    
    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[K_a] and self.rect.left > 0:
            self.rect.x -= 5
        elif pressed[K_d] and self.rect.right < WIDTH:
            self.rect.x += 5