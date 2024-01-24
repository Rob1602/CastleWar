# Resources

import pygame as CastleWar      # pygame library
from GameConstants import *     # game constants
import os                       # operative system libray

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# search resources in the CastleWar directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize pygame library
CastleWar.init()

# phase variable start condition
phase = "START"

# variables' list
game_statistics = []

def initializeGameStatistics():

    # clear the list
    game_statistics.clear()

    # set the number of element in the list
    for n in range(0, 24):
        game_statistics.append(0)

    # append all the initial values to the variables
    game_statistics[RESOURCES_PL1], game_statistics[RESOURCES_PL2] = INITIAL_RESOURCES, INITIAL_RESOURCES
    game_statistics[WALL_HEALTH_PL1], game_statistics[WALL_HEALTH_PL2] = WALL_HEALTH, WALL_HEALTH

initializeGameStatistics()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import and set size of all background images

ground = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Background\ground.png'), GROUND_DIMENSIONS)
background = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Background\background.jpg'), SCREEN_DIMENSIONS)
cloud0 = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Background\cloud-0.png'), CLOUD_DIMENSIONS)
cloud1 = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Background\cloud-1.png'), CLOUD_DIMENSIONS)
cloud2 = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Background\cloud-2.png'), CLOUD_DIMENSIONS)
barracks_PL1 = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Buildings\barracks.png'), (BARRACKS_DIMENSIONS))
barracks_PL2 = CastleWar.transform.scale(CastleWar.transform.flip(CastleWar.image.load(r'Resources\Buildings\barracks.png'), flip_x = True, flip_y = False), (BARRACKS_DIMENSIONS))
mine_PL1 = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Buildings\mine.png'), (MINE_DIMENSIONS))
mine_PL2 = CastleWar.transform.scale(CastleWar.transform.flip(CastleWar.image.load(r'Resources\Buildings\mine.png'), flip_x = True, flip_y = False), (MINE_DIMENSIONS))
wall_PL1 = CastleWar.transform.scale(CastleWar.image.load(r'Resources\Buildings\tower.png'), (WALL_DIMENSIONS))
wall_PL2 = CastleWar.transform.scale(CastleWar.transform.flip(CastleWar.image.load(r'Resources\Buildings\tower.png'), flip_x = True, flip_y = False), (WALL_DIMENSIONS))

# background images
background_images = []
background_images.append([background, (0, 0)])                  # 1
background_images.append([ground, GROUND_POSITION])             # 2
background_images.append([barracks_PL1, BARRACKS_POSITION_PL1]) # 3
background_images.append([barracks_PL2, BARRACKS_POSITION_PL2]) # 4
background_images.append([mine_PL1, MINE_POSITION_PL1])         # 5
background_images.append([mine_PL2, MINE_POSITION_PL2])         # 6
background_images.append([wall_PL1, WALL_POSITION_PL1])         # 7
background_images.append([wall_PL2, WALL_POSITION_PL2])         # 8

# swordsman PL1 sprites
swordsman_sprites_PL1 = []
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\ready.png'))     # 0 ready
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\run-0.png'))     # 1 start run
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\run-1.png'))     # 2
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\run-2.png'))     # 3
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\run-3.png'))     # 4
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\run-4.png'))     # 5
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\run-5.png'))     # 6 end run
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\attack-0.png'))  # 7 start attack
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\attack-1.png'))  # 8
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\attack-2.png'))  # 9
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\attack-3.png'))  # 10
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\attack-2.png'))  # 11
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\attack-1.png'))  # 12 end attack
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\fallen-0.png'))  # 13 start fall
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\fallen-1.png'))  # 14
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\fallen-2.png'))  # 15
swordsman_sprites_PL1.append(CastleWar.image.load(r'Resources\Swordsman\PL1\fallen-2.png'))  # 16 end fall

# swordsman PL2 sprites
swordsman_sprites_PL2 = []
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\ready.png'))     # 0 ready
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\run-0.png'))     # 1 start run
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\run-1.png'))     # 2
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\run-2.png'))     # 3
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\run-3.png'))     # 4
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\run-4.png'))     # 5
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\run-5.png'))     # 6 end run
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\attack-0.png'))  # 7 start attack
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\attack-1.png'))  # 8
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\attack-2.png'))  # 9
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\attack-3.png'))  # 10
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\attack-2.png'))  # 11
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\attack-1.png'))  # 12 end attack
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\fallen-0.png'))  # 13 start fall
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\fallen-1.png'))  # 14
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\fallen-2.png'))  # 15
swordsman_sprites_PL2.append(CastleWar.image.load(r'Resources\Swordsman\PL2\fallen-2.png'))  # 16 end fall

# archer PL1 sprites
archer_sprites_PL1 = []
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\ready.png'))       # 0 ready
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-0.png'))       # 1 start run
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-1.png'))       # 2
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-2.png'))       # 3
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-3.png'))       # 4
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-4.png'))       # 5
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-5.png'))       # 6
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-6.png'))       # 7
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-7.png'))       # 8
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-8.png'))       # 9
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-9.png'))       # 10
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-10.png'))      # 11
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\run-11.png'))      # 12 end run
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\shoot-0.png'))     # 13 start shoot
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\shoot-1.png'))     # 14 end shoot
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\fallen-0.png'))    # 15 start fall
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\fallen-1.png'))    # 16
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\fallen-2.png'))    # 17
archer_sprites_PL1.append(CastleWar.image.load(r'Resources\Archer\PL1\fallen-2.png'))    # 18 end fall

# archer PL2 sprites
archer_sprites_PL2 = []
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\ready.png'))       # 0 ready
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-0.png'))       # 1 start run
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-1.png'))       # 2
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-2.png'))       # 3
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-3.png'))       # 4
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-4.png'))       # 5
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-5.png'))       # 6
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-6.png'))       # 7
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-7.png'))       # 8
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-8.png'))       # 9
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-9.png'))       # 10
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-10.png'))      # 11
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\run-11.png'))      # 12 end run
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\shoot-0.png'))     # 13 start shoot
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\shoot-1.png'))     # 14 end shoot
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\fallen-0.png'))    # 15 start fall
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\fallen-1.png'))    # 16
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\fallen-2.png'))    # 17
archer_sprites_PL2.append(CastleWar.image.load(r'Resources\Archer\PL2\fallen-2.png'))    # 18 end fall

# arrow PL1 sprite
arrow_sprite_PL1 = CastleWar.image.load(r'Resources\Archer\PL1\arrow.png')

# arrow PL2 sprite
arrow_sprite_PL2 = CastleWar.image.load(r'Resources\Archer\PL2\arrow.png')

# worker PL1 sprites
worker_sprites_PL1 = []
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\ready.png'))       # 0 ready
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\dig-0.png'))       # 1 start dig
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\dig-1.png'))       # 2
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\dig-2.png'))       # 3
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\dig-3.png'))       # 4 ene dig
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\repair-0.png'))    # 5 start repair
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\repair-1.png'))    # 6
worker_sprites_PL1.append(CastleWar.image.load(r'Resources\Worker\PL1\repair-2.png'))    # 7 wnd repair

# worker PL1 sprites
worker_sprites_PL2 = []
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\ready.png'))       # 0 ready
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\dig-0.png'))       # 1 start dig
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\dig-1.png'))       # 2
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\dig-2.png'))       # 3
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\dig-3.png'))       # 4 ene dig
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\repair-0.png'))    # 5 start repair
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\repair-1.png'))    # 6
worker_sprites_PL2.append(CastleWar.image.load(r'Resources\Worker\PL2\repair-2.png'))    # 7 wnd repair
