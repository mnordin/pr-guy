import pygame
import ConfigParser
from entity import Entity

class Hero(Entity):
    def __init__(self, config, engine):
        self.config = config
        self.surface = pygame.image.load(self.config.get('Assets', 'image_path') + "hero.gif")
        self.rect = self.surface.get_rect(center=(400, 250))
        self.engine = engine
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def tick(self):
        if self.moving_left:
            self.rect.left -= self.config.getint('Game', 'speed')
        if self.moving_right:
            self.rect.left += self.config.getint('Game', 'speed')
        if self.moving_up:
            self.rect.top -= self.config.getint('Game', 'speed')
        if self.moving_down:
            self.rect.top += self.config.getint('Game', 'speed')