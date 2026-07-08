import pygame
from pygame.locals import *
from settings import *

class Player(pygame.sprite.Sprite):
    # Ty will scream at me because pygame.Sprite defaults it to None
    # A band-aid until it gets fixed
    rect: pygame.Rect | pygame.FRect
    
    def __init__(self, x: int, y: int, image: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = image
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
    
    def update(self):
        pressed = pygame.key.get_pressed()
        pressing_left = pressed[K_a] or pressed[K_LEFT]
        pressing_right = pressed[K_d] or pressed[K_RIGHT]

        if pressing_left and pressing_right:
            pass
        elif pressing_left:
            self.rect.x -= 5
        elif pressing_right:
            self.rect.x += 5