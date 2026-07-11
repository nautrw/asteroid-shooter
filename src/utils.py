import os
import pygame
from pygame import mixer

SPRITES = os.path.join("src", "assets", "sprites")
SOUNDS = os.path.join("src", "assets", "sounds")


def load_sprite(name: str) -> pygame.Surface:
    return pygame.image.load(os.path.join(SPRITES, f"{name}.png")).convert_alpha()


def load_sound(name: str) -> mixer.Sound:
    return mixer.Sound(os.path.join(SOUNDS, f"{name}.mp3"))


def draw_text(
    text: str,
    font: pygame.font.Font,
    color: str | tuple[int],
    surface: pygame.Surface,
    x: int | float,
    y: int | float,
) -> None:
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)
