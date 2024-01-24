### CASTLE WAR

# Sprites

from Arrow import *       # game class Arrow


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# archer class
class Archer(CastleWar.sprite.Sprite):
    def __init__(self, position, health_points, player):
        super().__init__()
        self.type = "archer"
        self.position = [position, BATTLEFIELD_HEIGHT]
        self.health_points = health_points
        self.player = player
        self.range = ARCHER_RANGE
        self.hit_points = ARCHER_HIT
        self.speed = ARCHER_SPEED
        self.rest = ARCHER_REST
        self.dimension = ARCHER_DIMENSION
        if self.player is 1:
            self.sprites = archer_sprites_PL1
            self.add(warriors_PL1)
        elif self.player is 2:
            self.sprites = archer_sprites_PL2
            self.add(warriors_PL2)
        self.current_sprite = 0
        self.update()

    def ready(self):
        self.current_sprite = 0
        self.update()

    def run(self):
        if self.player is 1:
            if self.position[X] < SCREEN_WIDTH - WALL_POS_X - self.range:
                self.position[X] += self.speed
                self.current_sprite += self.speed / 7
                if self.current_sprite < 1 or self.current_sprite >= 13: self.current_sprite = 1
            else:

                # call the class shoot() function
                self.shoot()

        if self.player is 2:
            if self.position[X] > WALL_POS_X + self.range:
                self.position[X] -= self.speed
                self.current_sprite += self.speed / 7
                if self.current_sprite < 1 or self.current_sprite >= 13: self.current_sprite = 1

            else:
                self.shoot()

        self.update()

    # shoot function
    def shoot(self):
        self.current_sprite += self.speed / 45
        if self.current_sprite < 13 or self.current_sprite >= 15:
            self.current_sprite = 13

            # add an arrow instance to the arrows sprites group
            arrows.add(Arrow([self.position[X], self.position[Y] + 7], 0, 0, self.hit_points, self.player))

        self.update()

    def die(self):
        self.current_sprite += self.speed / 7
        if self.current_sprite < 14: self.current_sprite = 14
        elif self.current_sprite >= 19:
            self.current_sprite = 18
            self.kill()

        self.update()

    def update(self):
        self.rect = Rect(self.position[X] - self.range, self.position[Y], self.range * 2, self.dimension[HEIGHT])
        updateEntities(self.type, self.sprites[int(self.current_sprite)], self.position, self.dimension[WIDTH])
