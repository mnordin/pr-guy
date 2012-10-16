import ConfigParser
from engine import Engine
import os
import pygame
import sys

config = ConfigParser.ConfigParser()
config.readfp(open('config/display.cfg'))

engine = Engine(config)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    engine.update()
