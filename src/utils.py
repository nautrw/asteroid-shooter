import os
import pygame

SPRITES = os.path.join("src", "assets", "sprites")


def load_sprite(name: str) -> pygame.Surface:
    return pygame.image.load(os.path.join(SPRITES, f"{name}.png")).convert_alpha()

def draw_text(text: str, font: pygame.font.Font, color: str | tuple[int], surface: pygame.Surface, x: int | float, y: int | float) -> None:
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)
