import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = image
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
