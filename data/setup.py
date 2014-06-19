import pygame as py
from . import tools
from . import constants as c

GAME = 'BEGIN GAME'

py.init()
py.event.set_allowed([py.KEYDOWN, py.KEYUP, py.QUIT])

SCREEN = py.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
