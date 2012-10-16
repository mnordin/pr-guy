import pygame

class Menu:
    def __init__(self, config, engine):
        self.config = config
        self.engine = engine
        self.surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect()

    def tick(self):
        self.display_title()
        self.display_text()
        #if pygame.key.get_pressed():
        #    self.surface.fill((0,0,0))

    def display_title(self):
        font = pygame.font.Font(None, 240)
        text = font.render(self.config.get('Menu', 'title'), True, (255,255,255,255))
        text_pos = text.get_rect(center=(self.engine.display.get_rect().centerx, 120))
        self.engine.display.blit(text, text_pos)

    def display_text(self):
        font = pygame.font.Font(None, 46)
        text = font.render(self.config.get('Menu', 'text'), True, (255,255,255,255))
        text_pos = text.get_rect(center=(self.engine.display.get_rect().centerx, 550))
        self.engine.display.blit(text, text_pos)
