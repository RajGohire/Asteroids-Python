import pygame as pg
import gc
from dataclasses import dataclass
from math import pi as PI, cos, sin, atan2
from random import randint, random

# Window Dimensions
SCREENWIDTH = 1280
SCREENHEIGHT = 720

# Colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Game Constants
ASTEROID_SPEED = 4
ASTEROID_SPEED_SMALL = 3
ASTEROID_SPEED_MEDIUM = 2
ASTEROID_SPEED_LARGE = 1
MAX_ASTEROIDS = 26

SAUCER_SPEED = 0.6
SAUCER_SPEED_SMALL = 0.4
SAUCER_SPEED_LARGE = 0.3
MAX_SAUCERS = 1
MAX_SAUCERS_SMALL = 1
MAX_SAUCERS_LARGE = 1

SHIP_SPEED = 0.06
DECELERATION_VELOCITY = 0.95
SHIP_DIR_LEFT = -1
SHIP_DIR_RIGHT = 1

BULLET_SPEED = 0.6
SAUCER_BULLET_SPEED = 0.4
MAX_BULLETS = 4
MAX_SAUCER_BULLETS = 1
BULLET_TIMEOUT = 2

NUM_LIVES = 3
SPAWN_TIME_GAP = 5
SAUCER_SPAWN_TIME_GAP = 30

RAND_MAX = 2147483647

@dataclass
class Coords(object):
	def __init__(self, coord):
		self.x = coord[0]
		self.y = coord[1]