import pygame

class Hero:
    def __init__(self, config):
        self.config = config
        self.surface = pygame.image.load(self.config.get('Assets', 'image_path') + "hero.gif")
        self.rect = self.surface.get_rect()

    def tick(self):
        pass