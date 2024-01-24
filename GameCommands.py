### CASTLE WAR

# Commands

import pygame as CastleWar      # pygame library

from Archer import *  # game class Archer
from Swordsman import *  # game class Swordsman
from Tower import *  # game classes and subfunctions
from GameConstants import *     # game constants
from GameResources import *     # game resources
import os                       # operative system functions
import pickle                   # list saving on file

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# initialize pygame library
CastleWar.init()

# set current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# savegame function
def saveGame():

    # create serialization lists to save objects on a file
    serialized_warriors = []
    serialized_arrows = []

    # serialize objects attributes
    for warrior in warriors: # for every warrior

        # append to the serialization list some of its attributes
        serialized_warriors.append((warrior.type, warrior.position, warrior.health_points, warrior.player))

    for arrow in arrows: # for every warrior

        # append to the serialization list some of its attributes
        serialized_arrows.append((arrow.path, arrow.position, arrow.orientation,  arrow.player, arrow.hit_points))

    # create a list of lists
    savelist = (game_statistics, serialized_warriors, serialized_arrows)

    gamesave = open("savegame.cw", 'wb')    # open the savegame file in writing mode
    pickle.dump(savelist, gamesave)         # paste the game statistics list
    gamesave.close()                        # close the savegame file


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load function
def loadGame():

    # open the file if ther is one
    try:

        with open("savegame.cw", 'rb') as gamesave:             # open the savegame file in reading mode
            savelist = pickle.load(gamesave)                    # copy the list in the file to the temporary one

            # call clearGroups() function to remove all the game entities
            clearGroups()

            # re-initialize game through initializeGame() function
            initializeGame()

            # copy the statistics temporary list to game_statistics list
            for value in range(0, len(savelist[STATISTICS])):   # for every value in saved game statistics

                # update the value of current game statistics
                game_statistics[value] = savelist[STATISTICS][value]

            # copy the warriors temporary list to game_statistics list
            for warrior in range(0, len(savelist[WARRIORS])):

                # check if the type of the entity loaded is swordsman
                if savelist[WARRIORS][warrior][TYPE] == 'swordsman':

                    # create a new swordsman with the attributes given
                    warriors.add(Swordsman(savelist[WARRIORS][warrior][POSITION][X], savelist[WARRIORS][warrior][HEALTH_POINTS], savelist[WARRIORS][warrior][PLAYER]))

                # check if the type of the entity loaded is archer
                elif savelist[WARRIORS][warrior][TYPE] == 'archer':

                    # create a new archer with the attributes given
                    warriors.add(Archer(savelist[WARRIORS][warrior][POSITION][X], savelist[WARRIORS][warrior][HEALTH_POINTS], savelist[WARRIORS][warrior][PLAYER]))

            # copy the arrows temporary list to game_statistics list
            for arrow in range(0, len(savelist[ARROWS])):
                arrows.add(Arrow(savelist[2][arrow][POSITION], savelist[ARROWS][arrow][PATH], savelist[ARROWS][arrow][ORIENTATION], savelist[ARROWS][arrow][HIT_POINTS], savelist[ARROWS][arrow][PLAYER]))

            # refresh sprites and group dependancies with refreshGroup function
            refreshGroups()

            # close the savegame file
            gamesave.close()

    except IOError:
        return

# initialization function
def initializeGame():
    entities.add(Tower(1))                  # add player 1 tower
    entities.add(Tower(2))                  # add player 1 tower
    refreshGroups()                         # refresh sprites and group dependancies with refreshGroup function

    # if we are not loading an old game, but starting a new
    initializeGameStatistics()

    CastleWar.mouse.set_visible(False)      # hide the mouse cursor on the screen

    # return start initialization values
    return True, [CastleWar.time.Clock(), 0], [[False, 0], [False, 0], [False, 0], [False, 0]]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# command execution function
def doCommand(key):

    # check the key input
    if key == "q":

        # check if the resources are enough
        if game_statistics[RESOURCES_PL1] >= WORKER_COST:

            # reduce the resources by the entity cost
            game_statistics[RESOURCES_PL1] -= WORKER_COST

            # increase the entity counter
            game_statistics[WORKERS_AVAIBLE_PL1] += 1

    if key == "w":
        if game_statistics[RESOURCES_PL1] >= SWORDSMAN_COST:
            game_statistics[RESOURCES_PL1] -= SWORDSMAN_COST
            game_statistics[SWORDSMEN_AVAIBLE_PL1] += 1

    if key == "e":
        if game_statistics[RESOURCES_PL1] >= ARCHER_COST:
            game_statistics[RESOURCES_PL1] -= ARCHER_COST
            game_statistics[ARCHERS_AVAIBLE_PL1] += 1

    if key == "p":
        if game_statistics[RESOURCES_PL2] >= WORKER_COST:
            game_statistics[RESOURCES_PL2] -= WORKER_COST
            game_statistics[WORKERS_AVAIBLE_PL2] += 1

    if key == "o":
        if game_statistics[RESOURCES_PL2] >= SWORDSMAN_COST:
            game_statistics[RESOURCES_PL2] -= SWORDSMAN_COST
            game_statistics[SWORDSMEN_AVAIBLE_PL2] += 1

    if key == "i":
        if game_statistics[RESOURCES_PL2] >= ARCHER_COST:
            game_statistics[RESOURCES_PL2] -= ARCHER_COST
            game_statistics[ARCHERS_AVAIBLE_PL2] += 1

    if key == "a":
        if game_statistics[WORKERS_AVAIBLE_PL1] >= 1:
            game_statistics[WORKERS_AVAIBLE_PL1] -= 1
            game_statistics[WORKERS_MINE_PL1] += 1

    if key == "s":
        if game_statistics[WORKERS_AVAIBLE_PL1] >= 1:
            game_statistics[WORKERS_AVAIBLE_PL1] -= 1
            game_statistics[WORKERS_WALL_PL1] += 1

    if key == "d":
        if game_statistics[SWORDSMEN_AVAIBLE_PL1] >= 1:
            game_statistics[SWORDSMEN_AVAIBLE_PL1] -= 1
            game_statistics[SWORDSMEN_DISPATCHED_PL1] += 1
            warriors_PL1.add(Swordsman(BARRACKS_POS_X, SWORDSMAN_HEALTH, 1))    # add entity to its game group

    if key == "f":
        if game_statistics[ARCHERS_AVAIBLE_PL1] >= 1:
            game_statistics[ARCHERS_AVAIBLE_PL1] -= 1
            game_statistics[ARCHERS_DISPATCHED_PL1] += 1
            warriors_PL1.add(Archer(BARRACKS_POS_X, ARCHER_HEALTH, 1))

    if key == "z":

        # add entities until the counter is 0
        while game_statistics[SWORDSMEN_AVAIBLE_PL1] > 0:
            game_statistics[SWORDSMEN_AVAIBLE_PL1] -= 1
            game_statistics[SWORDSMEN_DISPATCHED_PL1] += 1
            warriors_PL1.add(Swordsman(BARRACKS_POS_X, SWORDSMAN_HEALTH, 1))

        while game_statistics[ARCHERS_AVAIBLE_PL1] > 0:
            game_statistics[ARCHERS_AVAIBLE_PL1] -= 1
            game_statistics[ARCHERS_DISPATCHED_PL1] += 1
            warriors_PL1.add(Archer(BARRACKS_POS_X, ARCHER_HEALTH, 1))

    if key == "l":
        if game_statistics[WORKERS_AVAIBLE_PL2] >= 1:
            game_statistics[WORKERS_AVAIBLE_PL2] -= 1
            game_statistics[WORKERS_MINE_PL2] += 1

    if key == "k":
        if game_statistics[WORKERS_AVAIBLE_PL2] >= 1:
            game_statistics[WORKERS_AVAIBLE_PL2] -= 1
            game_statistics[WORKERS_WALL_PL2] += 1

    if key == "j":
        if game_statistics[SWORDSMEN_AVAIBLE_PL2] >= 1:
            game_statistics[SWORDSMEN_AVAIBLE_PL2] -= 1
            game_statistics[SWORDSMEN_DISPATCHED_PL2] += 1
            warriors_PL2.add(Swordsman(SCREEN_WIDTH - BARRACKS_POS_X, SWORDSMAN_HEALTH, 2))

    if key == "h":
        if game_statistics[ARCHERS_AVAIBLE_PL2] >= 1:
            game_statistics[ARCHERS_AVAIBLE_PL2] -= 1
            game_statistics[ARCHERS_DISPATCHED_PL2] += 1
            warriors_PL2.add(Archer(SCREEN_WIDTH - BARRACKS_POS_X, ARCHER_HEALTH, 2))

    if key == "m":
        while game_statistics[SWORDSMEN_AVAIBLE_PL2] > 0:
            game_statistics[SWORDSMEN_AVAIBLE_PL2] -= 1
            game_statistics[SWORDSMEN_DISPATCHED_PL2] += 1
            warriors_PL2.add(Swordsman(SCREEN_WIDTH - BARRACKS_POS_X, SWORDSMAN_HEALTH, 2))

        while game_statistics[ARCHERS_AVAIBLE_PL2] > 0:
            game_statistics[ARCHERS_AVAIBLE_PL2] -= 1
            game_statistics[ARCHERS_DISPATCHED_PL2] += 1
            warriors_PL2.add(Archer(SCREEN_WIDTH - BARRACKS_POS_X, ARCHER_HEALTH, 2))