### CASTLE WAR

# Constants

import pygame as CastleWar       # pygame library

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# MODIFI ONLY THESE CONSTANTS
FPS = 60            # 24/30/60/120/144                       # frames per second
SHOW_FPS = True     # True/False                             # show FPS on screen
CLOUDS = True       # True/False                             # enable clouds: FPS must be >= 60
TURN_TIME = 4       # train, dispatch, wait                  # measured in seconds

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# sprites groups
entities = CastleWar.sprite.AbstractGroup()
warriors = CastleWar.sprite.AbstractGroup()
warriors_PL1 = CastleWar.sprite.Group()
warriors_PL2 = CastleWar.sprite.Group()
arrows = CastleWar.sprite.Group()

# initialize pygame library
CastleWar.init()

# screen constants
screen_info = CastleWar.display.Info()                  # get info from current display
SCREEN_WIDTH = screen_info.current_w                    # width of the CastleWar window
SCREEN_HEIGHT = screen_info.current_h                   # height of the CastleWar window
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)       # dimensions of the screen
game_screen = CastleWar.display.set_mode(SCREEN_DIMENSIONS, CastleWar.FULLSCREEN, vsync = True)

# fonts constants
FONT_BIG = CastleWar.font.Font(None, 56)                # big font settings
FONT_MEDIUM = CastleWar.font.Font(None, 44)             # medium font settings
FONT_SMALL = CastleWar.font.Font(None, 32)              # small font settings

# colors constants
WHITE = (255, 255, 255)                                 # color white rgb
BLACK = (0, 0, 0)                                       # color black rgb
RED = (255, 0, 0)                                       # color red rgb
BLUE = (0, 0, 255)                                      # color blue rgb
GREEN = (55, 126, 71)                                     # color green rgb
YELLOW = (255, 255, 0)                                  # color yellow rgb
ORANGE = (255, 140, 0)                                  # color orange rgb

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# game constants
INITIAL_RESOURCES = 10                                  # initial amount of resources

# ground constants
GROUND_HEIGHT = SCREEN_HEIGHT/12                        # height of the ground
GROUND_DIMENSIONS = (SCREEN_WIDTH, GROUND_HEIGHT)       # ground dimensions
GROUND_POSITION = (0, SCREEN_HEIGHT - GROUND_HEIGHT)    # ground coordinates

# battlefield constants
BATTLEFIELD_HEIGHT = SCREEN_HEIGHT - GROUND_HEIGHT      # battlefield height

# clouds constants
CLOUD_HEIGHT = 100                                      # cloud height (dimension)
CLOUD_WIDTH = 300                                       # cloud width (dimension)
CLOUD_DIMENSIONS = (CLOUD_WIDTH, CLOUD_HEIGHT)          # cloud dimensions
CLOUD_SPEED_UNIT = 50/FPS                               # cloud velocity unity

# walls constants
WALL_POS_X = 270                                        # wall center x coordinate
WALL_POS_Y = GROUND_HEIGHT/2 + 5                        # wall bottom y coordinate
WALL_WIDTH = 100                                        # wall width
WALL_HEIGHT = 200                                       # wall height
WALL_DIMENSIONS = (WALL_WIDTH, WALL_HEIGHT)             # wall dimensions
WALL_POSITION_PL1 = (WALL_POS_X - WALL_WIDTH/2, SCREEN_HEIGHT - WALL_HEIGHT - WALL_POS_Y)
WALL_POSITION_PL2 = (SCREEN_WIDTH - WALL_POS_X - WALL_WIDTH/2, SCREEN_HEIGHT - WALL_HEIGHT - WALL_POS_Y)

# mine constants
MINE_POS_X = 70                                         # mine center x coordinate
MINE_POS_Y = GROUND_HEIGHT/2 + 10                       # mine bottom y coordinate
MINE_WIDTH = 100                                        # mine width
MINE_HEIGHT = 100                                       # mine height
MINE_DIMENSIONS = (MINE_WIDTH, MINE_HEIGHT)
MINE_POSITION_PL1 = (MINE_POS_X - MINE_WIDTH/2, SCREEN_HEIGHT - MINE_HEIGHT - MINE_POS_Y)
MINE_POSITION_PL2 = (SCREEN_WIDTH - MINE_POS_X - MINE_WIDTH/2, SCREEN_HEIGHT - MINE_HEIGHT - MINE_POS_Y)

# barracks constants
BARRACKS_POS_X = 170                                    # barracks bottom y coordinate
BARRACKS_POS_Y = GROUND_HEIGHT/2 + 2                    # barracks bottom y coordinate
BARRACKS_WIDTH = 100                                    # barracks width
BARRACKS_HEIGHT = 150                                   # barracks height
BARRACKS_DIMENSIONS = (BARRACKS_WIDTH, BARRACKS_HEIGHT) # barracks dimensions
BARRACKS_POSITION_PL1 = (BARRACKS_POS_X - BARRACKS_WIDTH/2, SCREEN_HEIGHT - BARRACKS_HEIGHT - BARRACKS_POS_Y)
BARRACKS_POSITION_PL2 = (SCREEN_WIDTH - BARRACKS_POS_X - BARRACKS_WIDTH/2, SCREEN_HEIGHT - BARRACKS_HEIGHT - BARRACKS_POS_Y)

# other constants
BORDER = 10                                             # minimum distance of the buildings from the border
BUILDING_SEPARATION = 5                                 # minimum distance between the buildings
CORRECTIVE_FACTOR = 144/FPS                             # correct the entities speed basing on fps (calculated with respect to 144 FPS)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# worker constants
WORKER_COST = 1                         # amount of resources to train a new worker
WORKER_TRAIN = 10                       # amount of turns to train a new worker
WORKER_SPEED = 1*CORRECTIVE_FACTOR     # distance covered in one turn by a running worker
WORKER_PROD = 1                         # amount of resources per turn mined by a worker in mine
WORKER_REPAIR = 1                       # amount of HP restored per turn by a worker in wall
WORKER_WITDH = 22                       # worker sprite width
WORKER_HEIGHT = 26                      # worker sprite height
WORKER_DIMENSION = (WORKER_WITDH, WORKER_HEIGHT)
MINER = 'miner'
MASON = 'mason'

# swordsman constants
SWORDSMAN_COST = 5                      # amount of resources to train a new swordsman
SWORDSMAN_TRAIN = 20                    # amount of turns to train a new swordsman
SWORDSMAN_SPEED = 1/2*CORRECTIVE_FACTOR         # distance covered in one turn by a running swordsman
SWORDSMAN_RANGE = 12                    # maximum distance at which a swordsman can hit an unit
SWORDSMAN_HIT = 2                       # damage caused by of a swordsman per turn
SWORDSMAN_REST = 10                     # amount of turns of inactivity of a swordman after an attack
SWORDSMAN_HEALTH = 30                   # initial amount of HP of a swordsman
SWORDSMAN_HEIGHT = 20                   # swordsman sprite height
SWORDSMAN_WIDTH = 24                    # swordsman sprite width
SWORDSMAN_DIMENSION = (SWORDSMAN_WIDTH, SWORDSMAN_HEIGHT)

# archer constants
ARCHER_COST = 5                         # amount of resources to train a new archer
ARCHER_TRAIN = 20                       # amount of turns to train a new archer
ARCHER_SPEED = 2/3*CORRECTIVE_FACTOR            # distance covered in one turn by a running archer
ARCHER_RANGE = 100                      # maximum distance at which an archer can send an arrow
ARCHER_REST = 10                        # amount of turns of inactivity of an archer after shooting
ARCHER_HEALTH = 20                      # initial amount of HP of an archer
ARCHER_HIT = 1                          # damage caused by of an arrow shoot by an archer
ARCHER_HIGHT = 22                       # archer sprite height
ARCHER_WIDTH = 30                       # archer sprite width
ARCHER_DIMENSION = (ARCHER_WIDTH, ARCHER_HIGHT)

# arrow constants
ARROW_SPEED = 2*CORRECTIVE_FACTOR                        # distance covered in one turn by an arrow
ARROW_HEIGHT = 5                        # arrow sprite height
ARROW_WIDTH = 16                        # arrow sprite width
ARROW_DIMENSION = (ARROW_WIDTH, ARROW_HEIGHT)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# wall constants
WALL_HEALTH = 1000                      # maximum amount of HP af the wall

# tower constants
TOWER_RANGE = 220                       # maximum distance at which the tower can send an arrow
TOWER_HIT = 5                           # damage caused by of an arrow shoot by the tower
TOWER_REST = 50                         # amount of turns of inactivity of the tower after shooting
TOWER_HEIGHT = 160                      # height of the tower
TOWER_WIDTH = 52                        # height of the tower
TOWER_DIMENSION = (TOWER_WIDTH, TOWER_HEIGHT)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# game_statistics list indexes
RESOURCES_PL1 = 0
RESOURCES_PL2 = 1
WALL_HEALTH_PL1 = 2
WALL_HEALTH_PL2 = 3
WORKERS_AVAIBLE_PL1 = 4
WORKERS_AVAIBLE_PL2 = 5
SWORDSMEN_AVAIBLE_PL1 = 6
SWORDSMEN_AVAIBLE_PL2 = 7
ARCHERS_AVAIBLE_PL1 = 8
ARCHERS_AVAIBLE_PL2 = 9
WORKERS_MINE_PL1 = 10
WORKERS_MINE_PL2 = 11
WORKERS_WALL_PL1 = 12
WORKERS_WALL_PL2 = 13
SWORDSMEN_BARRACKS_PL1 = 14
SWORDSMEN_BARRACKS_PL2 = 15
ARCHERS_BARRACKS_PL1 = 16
ARCHERS_BARRACKS_PL2 = 17
SWORDSMEN_DISPATCHED_PL1 = 18
SWORDSMEN_DISPATCHED_PL2 = 19
ARCHERS_DISPATCHED_PL1 = 20
ARCHERS_DISPATCHED_PL2 = 21
TURN = 22
CLOCK = 23

# dimensions game indexes
WIDTH = 0
HEIGHT = 1

# range indexes
FIRST = 0
LAST = 1

# coordinates indexes
X = 0
Y = 1

# game clock indexes
CONTINUE = 0
TEMPORARY = 1

# loadgame lists indexes
STATISTICS = 0
WARRIORS = 1
ARROWS = 2
TYPE = 0
PATH = 0
POSITION = 1
HEALTH_POINTS = 2
ORIENTATION = 2
PLAYER = 3
HIT_POINTS = 4

# worker indexes
ACTIVE = 0
SPRITE = 1
MINER_PL1 = 0
MINER_PL2 = 1
MASON_PL1 = 2
MASON_PL2 = 3