import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.asteroid import Asteroid
from scripts.explosion import Explosion
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
        self.explosions_group = pygame.sprite.Group()
        # defaults so that there is no delay for asteroids to spawn
        self.asteroid_dt_count = 100
        self.asteroid_dt_spawn_interval = 1
        self.dt = 0
        self.running = True
        self.heart_sprite = load_sprite("heart")

        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)

        self.paused = False

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_p:
                        self.paused = not self.paused

            if not self.paused:
                if self.asteroid_dt_count >= self.asteroid_dt_spawn_interval:
                    asteroid = Asteroid(random.randint(0, self.width), 0)
                    self.asteroids_group.add(asteroid)
                    self.asteroid_dt_count = 0
            
                asteroid_hits = pygame.sprite.groupcollide(self.bullets_group, self.asteroids_group, True, True)

                if asteroid_hits:
                    for asteroid in asteroid_hits.values():
                        x, y = asteroid[0].rect.centerx, asteroid[0].rect.centery
                        explosion = Explosion(x, y)
                        self.explosions_group.add(explosion)

                player_collisions = pygame.sprite.spritecollideany(self.player, self.asteroids_group)

                if player_collisions:
                    self.player.lose_life()

                if self.player.lives <= 0:
                    self.game_over()

                self.player.update(self.dt, self.bullets_group, self.width)

                self.bullets_group.update(self.dt, self.height)

                self.asteroids_group.update(self.dt, self.height, self.player.lose_life)

                self.explosions_group.update(self.dt)

            self.draw_all()

            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000
            self.asteroid_dt_count += self.dt

        pygame.quit()

    def draw_ui(self):
        # hearts
        heart_width, heart_height = self.heart_sprite.get_width(), self.heart_sprite.get_height()
        offset = 5
        spacing = 5
        for i in range(self.player.lives):
            rect = pygame.Rect(offset + i * (heart_width + spacing), offset, heart_width, heart_height)
            self.screen.blit(self.heart_sprite, rect)

        # score
        score_text = self.font.render(str(self.score), True, "white")
        score_rect = score_text.get_rect()
        score_rect.centerx = self.width // 2
        score_rect.top = offset
        self.screen.blit(score_text, score_rect)

    def draw_all(self):
        self.player.draw(self.screen)
        self.bullets_group.draw(self.screen)
        self.asteroids_group.draw(self.screen)
        self.explosions_group.draw(self.screen)
        self.draw_ui()
    
    def game_over(self):
        self.running = False

if __name__ == "__main__":
    Game().run()
