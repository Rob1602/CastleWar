### CASTLE WAR

# Sprites

from math import *  # mathematics operation library

from pygame.locals import *  # pygame variables

from GameFunctions import *  # game function


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# arrow class
class Arrow(CastleWar.sprite.Sprite):
    def __init__(self, position, path, orientation, hit_points, player):
        super().__init__()
        self.type = "arrow"                # type
        self.position = [0, 0]             # position list
        self.position[X] = position[X]     # x coordinate
        self.position[Y] = position[Y]     # y coordinate
        self.path = path                   # trajectory path (if tower's arrow)
        self.orientation = orientation     # orientation
        self.hit_points = hit_points       # hit points
        self.player = player               # player number
        self.dimension = ARROW_DIMENSION   # dimensions (tuple)
        self.speed = ARROW_SPEED           # speed

        # if the arrow is from player 1
        if self.player is 1:

            # set the sprites collection of player 1 and the rotation degrees of the arrow
            self.sprite = CastleWar.transform.rotate(arrow_sprite_PL1, (degrees(self.orientation)))

        elif self.player is 2:
            self.sprite = CastleWar.transform.rotate(arrow_sprite_PL2, (-degrees(self.orientation)))

        self.update()

    def ready(self):
        self.update()

    # move function
    def move(self):

        # check if the angle is 0
        if self.orientation is 0:
            if self.player is 1:
                if self.position[X] < SCREEN_WIDTH - WALL_POS_X:
                    self.position[X] += self.speed
                else:
                    game_statistics[WALL_HEALTH_PL2] -= self.hit()

            elif self.player is 2:
                if self.position[X] > WALL_POS_X:
                    self.position[X] -= self.speed
                else:
                    game_statistics[WALL_HEALTH_PL1] -= self.hit()

        # if the angle is not 0
        else:
            # check if the arrow position is not lower the ground
            if self.position[Y] < BATTLEFIELD_HEIGHT:

                if self.player is 1:

                    # increase the arrow x coordinates with a mathematical fucntion
                    self.position[X] += (1 * self.path * cos(self.orientation)) / self.path * self.speed

                    # decrease the arrow x coordinates with a mathematical fucntion
                    self.position[Y] -= (1 * self.path * sin(self.orientation)) / self.path * self.speed

                elif self.player is 2:
                    self.position[X] -= (1 * self.path * cos(self.orientation)) / self.path * self.speed
                    self.position[Y] -= (1 * self.path * sin(self.orientation)) / self.path * self.speed

            else:
                self.kill()

        self.update()

    # hit function
    def hit(self):
        self.kill()
        self.update()
        return self.hit_points

    def update(self):
        self.rect = Rect(self.position[X], self.position[Y], self.dimension[WIDTH], self.dimension[HEIGHT])
        updateEntities(self.type, self.sprite, self.position, self.dimension[WIDTH])
