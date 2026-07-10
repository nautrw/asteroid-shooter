import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.asteroid import Asteroid
import random
from utils import load_sprite

class Game:
    def __init__(self, width: int = 400, height: int = 800, fps: int = 60):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.player = Player((self.width // 2), (self.height - 10))
        self.bullets_group = pygame.sprite.Group()
        self.asteroids_group = pygame.sprite.Group()
        # defaults so that there is no delay for asteroids to spawn
        self.asteroid_dt_count = 100
        self.asteroid_dt_spawn_interval = 1
        self.dt = 0
        self.running = True
        self.heart_sprite = load_sprite("heart")

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            if self.asteroid_dt_count >= self.asteroid_dt_spawn_interval:
                asteroid = Asteroid(random.randint(0, self.width), 0)
                self.asteroids_group.add(asteroid)
                self.asteroid_dt_count = 0

            pygame.sprite.groupcollide(self.bullets_group, self.asteroids_group, True, True)

            player_collisions = pygame.sprite.spritecollideany(self.player, self.asteroids_group)

            if player_collisions:
                self.player.lose_life()

            if self.player.lives <= 0:
                self.game_over()

            self.player.update(self.dt, self.bullets_group, self.width)
            self.player.draw(self.screen)

            self.bullets_group.update(self.dt, self.height)
            self.bullets_group.draw(self.screen)

            self.asteroids_group.update(self.dt, self.height, self.player.lose_life)
            self.asteroids_group.draw(self.screen)

            self.draw_ui()

            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000
            self.asteroid_dt_count += self.dt

        pygame.quit()

    def draw_ui(self):
        heart_width, heart_height = self.heart_sprite.get_width(), self.heart_sprite.get_height()
        offset = 5
        spacing = 5
        for i in range(self.player.lives):
            rect = pygame.Rect(offset + i * (heart_width + spacing), offset, heart_width, heart_height)
            self.screen.blit(self.heart_sprite, rect)
    
    def game_over(self):
        self.running = False

if __name__ == "__main__":
    Game().run()
