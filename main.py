import ConfigParser
from engine import Engine
import os
import pygame
import sys

from hero import Hero
from menu import Menu

config = ConfigParser.ConfigParser()
config.readfp(open('config/display.cfg'))
config.readfp(open('config/assets.cfg'))
config.readfp(open('config/menu.cfg'))
config.readfp(open('config/game.cfg'))

engine = Engine(config)
menu = Menu(config, engine)
hero = Hero(config, engine)
engine.entities.append(hero)
engine.entities.append(menu)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.dict['key'] == pygame.K_LEFT:
                hero.moving_left = True
            if event.dict['key'] == pygame.K_RIGHT:
                hero.moving_right = True
            if event.dict['key'] == pygame.K_UP:
                hero.moving_up = True
            if event.dict['key'] == pygame.K_DOWN:
                hero.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.dict['key'] == pygame.K_LEFT:
                hero.moving_left = False
            if event.dict['key'] == pygame.K_RIGHT:
                hero.moving_right = False
            if event.dict['key'] == pygame.K_UP:
                hero.moving_up = False
            if event.dict['key'] == pygame.K_DOWN:
                hero.moving_down = False

    engine.update()