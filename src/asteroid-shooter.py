from signal import pause
import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.asteroid import Asteroid
from scripts.explosion import Explosion
import random
from utils import load_sprite, draw_text

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
        self.main_menu = True
        self.player_lost = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN and not self.player_lost:
                    if event.key == K_ESCAPE and not self.main_menu:
                        self.paused = not self.paused
                    elif event.key == K_SPACE and self.main_menu:
                        self.main_menu = False

            if not self.paused and not self.main_menu and not self.player_lost:
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
                        self.score += 1

                player_collisions = pygame.sprite.spritecollideany(self.player, self.asteroids_group)

                if player_collisions:
                    self.player.lose_life(self.reset)

                if self.player.lives <= 0:
                    self.player_lost = True

                self.player.update(self.dt, self.bullets_group, self.width)

                self.bullets_group.update(self.dt, self.height)

                self.asteroids_group.update(self.dt, self.height, self.player.lose_life, self.reset)

                self.explosions_group.update(self.dt)

            self.draw_all()

            pygame.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000
            self.asteroid_dt_count += self.dt

        pygame.quit()

    def draw_ui(self):
        if not self.main_menu and not self.player_lost:
            # hearts
            heart_width, heart_height = self.heart_sprite.get_width(), self.heart_sprite.get_height()
            offset = 5
            spacing = 5
            for i in range(self.player.lives):
                rect = pygame.Rect(offset + i * (heart_width + spacing), offset, heart_width, heart_height)
                self.screen.blit(self.heart_sprite, rect)

            # score
            draw_text(str(self.score), self.font, "white", self.screen, self.width // 2, 25)

            # paused
            if self.paused:
                # pygame.draw.rect will not draw with alpha
                # passing the SRCALPHA flag is required
                pause_surface = pygame.Surface((self.width, self.height), SRCALPHA)
                # pause_surface.set_alpha(128)
                # pause_surface.fill((50, 50, 50))
                pause_surface.fill((50, 50, 50, 128)) # grey, 50% transparency

                # Text can be drawn on pause surface or the main screen
                draw_text("PAUSED", self.font, "white", pause_surface, self.width // 2, self.height // 2)
                self.screen.blit(pause_surface, (0, 0))
        elif self.player_lost:
            # game over
            draw_text("GAME OVER", self.font, "red", self.screen, self.width // 2, self.height // 2)
        else:
            # main menu
            draw_text("ASTEROID SHOOTER", self.font, "red", self.screen, self.width // 2, self.height * .25)
            draw_text("Press space to play", self.font, "white", self.screen, self.width // 2, self.height * .5)

    def draw_all(self):
        self.screen.fill((0, 0, 0))

        if not self.main_menu and not self.player_lost:
            self.player.draw(self.screen)
            self.bullets_group.draw(self.screen)
            self.asteroids_group.draw(self.screen)
            self.explosions_group.draw(self.screen)

        self.draw_ui()

    def reset(self):
        self.player.rect.centerx = self.width // 2
        self.asteroids_group.empty()

if __name__ == "__main__":
    Game().run()
