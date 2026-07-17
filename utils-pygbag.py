import sys, os
import pygame
from pygame import mixer

# needed for pyinstaller to work
def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def load_sprite(name: str) -> pygame.Surface:
    file = resource(f"assets/sprites/{name}.png")
    return pygame.image.load(file).convert_alpha()


def load_sound(name: str) -> mixer.Sound:
    file = resource(f"assets/sounds/{name}.ogg")
    return mixer.Sound(file)

def load_icon() -> pygame.Surface:
    file = resource(f"assets/icons/icon.png")
    return pygame.image.load(file)

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
