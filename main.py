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

engine = Engine(config)
menu = Menu(config, engine)
hero = Hero(config)
engine.entities.append(hero)
engine.entities.append(menu)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.update()
