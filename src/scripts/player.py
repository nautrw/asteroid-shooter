from pygame.mixer_music import play
from scripts.bullet import Bullet
import pygame
from pygame import mixer
from pygame.locals import *
from utils import load_sprite, load_sound
from scripts.sounds import play_sound

class Player(pygame.sprite.Sprite):
    # Ty will scream at me because pygame.Sprite defaults it to None
    # A band-aid until it gets fixed
    rect: pygame.Rect | pygame.FRect
    
    def __init__(self, x: int | float, y: int | float):
        super().__init__()
        self.image: pygame.Surface = load_sprite("rocket")
        self.visible = True
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.movespeed = 275
        
        self.bullet_y_offset = 5

        self.shot_dt_count = 0
        self.shot_dt_interval = 0.5

        self.hit = False
        self.blinking = False
        self.blinks = 0
        self.blinks_dt_count = 0
        self.blinks_dt_interval = 0.3

        self.lives = 3
    
    def update(self, dt: int | float, bullet_group: pygame.sprite.Group, screen_width: int, audio_paused: bool):
        self.shot_dt_count += dt

        pressed = pygame.key.get_pressed()
        pressing_left = pressed[K_a] or pressed[K_LEFT]
        pressing_right = pressed[K_d] or pressed[K_RIGHT]

        if pressing_left and pressing_right:
            pass
        elif pressing_left and self.rect.left > 0:
            self.rect.x -= round(self.movespeed * dt)
        elif pressing_right and self.rect.right < screen_width:
            self.rect.x += round(self.movespeed * dt)
        
        if pressed[K_SPACE] and self.shot_dt_count >= self.shot_dt_interval:
            bullet = self.shoot()
            bullet_group.add(bullet)
            self.shot_dt_count = 0
            play_sound("fire")

        if self.blinking:
            self.blinks_dt_count += dt
        
            if self.blinks_dt_count >= self.blinks_dt_interval:
                self.visible = not self.visible
                self.blinks += 1
                self.blinks_dt_count = 0
            
            if self.blinks >= 6:
                self.blinking = False
                self.visible = True
                self.blinks = 0
                self.blinks_dt_count = 0

    def draw(self, screen: pygame.Surface):
        if self.visible:
            screen.blit(self.image, self.rect) # ty:ignore[invalid-argument-type]
    
    def lose_life(self, reset_callback: function):
        if not self.blinking:
            self.blinking = True
            self.lives -= 1
            reset_callback()  # ty:ignore[call-non-callable]
    
    def shoot(self):
        x = self.rect.centerx
        y = self.rect.top + self.bullet_y_offset
        return Bullet(x, y)
        
