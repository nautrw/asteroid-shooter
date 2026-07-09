import os
import pygame

SPRITES = os.path.join("src", "assets", "sprites")


def load_sprite(name: str) -> pygame.Surface:
    return pygame.image.load(os.path.join(SPRITES, f"{name}.png")).convert_alpha()