### CASTLE WAR

# Sprites

import pygame as CastleWar      # pygame library
from pygame.locals import *     # pygame variables
from GameFunctions import *     # game function
from Arrow import *       # game class Arrow
from math import *              # mathematics operation library

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# tower class
class Tower(CastleWar.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.type = "tower"
        self.player = player
        self.range = TOWER_RANGE
        self.hit_points = TOWER_HIT
        self.rest = TOWER_REST
        self.dimension = TOWER_DIMENSION

        # set the tower position basing on the player number
        if self.player is 1: self.position = (WALL_POS_X , SCREEN_HEIGHT - self.dimension[HEIGHT])
        elif self.player is 2: self.position = (SCREEN_WIDTH - WALL_POS_X, SCREEN_HEIGHT - self.dimension[HEIGHT])

        self.rect = Rect(self.position[X] + self.dimension[WIDTH] / 2 - self.range, self.position[Y], SCREEN_HEIGHT, 2 * self.range)

    # shoot function
    def shoot(self, target_position):

        # check if the tower rest counter has reach 0
        if self.rest is 0:

            # calculate the orientation of the arrow with respect to the enemy warrior
            orientation = asin((abs(self.position[Y] - target_position[Y])) / dist(self.position, target_position))

            # calculate the distance between the tower archer and the enemy warrior
            path = dist(target_position, self.position)

            arrows.add(Arrow(self.position, path, -orientation, self.hit_points, self.player))

            # reset the counter to the max
            self.rest = TOWER_REST

        # if not reduce the counter
        else: self.rest -= 1