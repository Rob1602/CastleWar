### CASTLE WAR

# Sprites

import pygame as CastleWar  # pygame library
from pygame.locals import *  # pygame variables
from GameFunctions import *  # game function
from math import *  # mathematics operation library


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# swordsman class
class Swordsman(CastleWar.sprite.Sprite):
    def __init__(self, position, health_points, player):
        super().__init__()
        self.type = "swordsman"  # type
        self.position = [position, BATTLEFIELD_HEIGHT]  # position (y constant)
        self.health_points = health_points  # health points
        self.player = player  # player number
        self.range = SWORDSMAN_RANGE  # range
        self.hit_points = SWORDSMAN_HIT  # hit points
        self.speed = SWORDSMAN_SPEED  # speed
        self.rest = SWORDSMAN_REST  # rest time (used as counter)
        self.dimension = SWORDSMAN_DIMENSION  # dimensionso of the sprite (tuple)

        # check if player number is 1
        if self.player is 1:

            # set sprites collection
            self.sprites = swordsman_sprites_PL1

            # add the sprite to the respective collision group
            self.add(warriors_PL1)

        # check if player number is 2
        elif self.player is 2:
            self.sprites = swordsman_sprites_PL2
            self.add(warriors_PL2)

        # set the current sprite index as 0 (ready sprite)
        self.current_sprite = 0

        # call class update() function
        self.update()

    # ready function
    def ready(self):
        self.current_sprite = 0
        self.update()

    # run function
    def run(self):
        if self.player is 1:

            # check if the entity position is before the enemy wall
            if self.position[X] < SCREEN_WIDTH - WALL_POS_X - self.range:

                # update the entity position
                self.position[X] += self.speed

                # update the sprite index
                self.current_sprite += self.speed / 5

                # if the sprites exceed the range of run sprites reset the index
                if self.current_sprite < 1 or self.current_sprite >= 7:
                    self.current_sprite = 1

            # if the entity has reached the enemy wall
            else:

                # reduce the health of the enemy wall by the entity attack function
                game_statistics[WALL_HEALTH_PL2] -= self.attack()

        if self.player is 2:
            if self.position[X] > WALL_POS_X + self.range:
                self.position[X] -= self.speed
                self.current_sprite += self.speed / 5
                if self.current_sprite < 1 or self.current_sprite >= 7:
                    self.current_sprite = 1
            else:
                game_statistics[WALL_HEALTH_PL1] -= self.attack()

        self.update()

    def attack(self):
        self.current_sprite += self.speed / 10

        # check when the sprite index reach the last sprite
        if self.current_sprite < 7 or self.current_sprite >= 13:
            self.current_sprite = 7

            # return the entity hit points (as damage)
            return self.hit_points

        self.update()

        # return no damage
        return 0

    # die function
    def die(self):
        self.current_sprite += self.speed / 10
        if self.current_sprite < 13:
            self.current_sprite = 13
        elif self.current_sprite >= 17:
            self.current_sprite = 16

            # remove the sprite from all the sprites groups
            self.kill()

        self.update()

    # update function
    def update(self):

        # set the rect attribute to the entity (for collision)
        self.rect = Rect(self.position[X] - self.range, self.position[Y], self.range * 2, self.dimension[HEIGHT])

        # call updateEntities() function to print the sprite
        updateEntities(self.type, self.sprites[int(self.current_sprite)], self.position, self.dimension[WIDTH])
