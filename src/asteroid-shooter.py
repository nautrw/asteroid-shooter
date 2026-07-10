import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.asteroid import Asteroid
from settings import *
import random

class Game:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.player = Player((WIDTH // 2), (HEIGHT - 10))
        self.bullets_group = pygame.sprite.Group()
        self.asteroids_group = pygame.sprite.Group()
        # defaults so that there is no delay for asteroids to spawn
        self.asteroid_dt_count = 100
        self.dt = 0
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            if self.asteroid_dt_count >= ASTEROID_DT_SPAWN_INTERVAl:
                asteroid = Asteroid(random.randint(0, WIDTH), 0)
                self.asteroids_group.add(asteroid)
                self.asteroid_dt_count = 0

            pygame.sprite.groupcollide(self.bullets_group, self.asteroids_group, True, True)

            self.player_collisions = pygame.sprite.spritecollideany(self.player, self.asteroids_group)

            if self.player_collisions and not self.player.blinking:
                self.player.blinking = True

            self.player.update(self.dt, self.bullets_group)
            self.player.draw(self.screen)

            self.bullets_group.update(self.dt)
            self.bullets_group.draw(self.screen)

            self.asteroids_group.update(self.dt)
            self.asteroids_group.draw(self.screen)

            pygame.display.flip()
            self.dt = self.clock.tick(FPS) / 1000
            self.asteroid_dt_count += self.dt

        pygame.quit()

if __name__ == "__main__":
    Game(WIDTH, HEIGHT).run()
