### CASTLE WAR

########### ROBERTA GAROFANO ############

# main


import pygame as CastleWar  # pygame library
from GameFunctions import *  # game functions
from GameFunctions import *  # game functions
from GameConstants import *  # game constants
from GameCommands import *  # game functions

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# initialize pygame library
CastleWar.init()

# initialize this function that gives us 3 values, that we are assigning to 3 different variables
# setting up the game state and returning some initial values
# such as a new game clock, the current status of whether the game is running or not, and a list of active workers
# initialize function
game_running, game_clock, active_workers = initializeGame()

# set starting cloud coordinates
clouds = [[cloud0, [SCREEN_WIDTH, BORDER]], [cloud1, [SCREEN_WIDTH / 3, 4 * BORDER]],
          [cloud2, [SCREEN_WIDTH / 2, 8 * BORDER]]]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# start the loop cycle
while game_running:

    # set screen updates per second using game clock (pygame built-in function)
    game_clock[CONTINUE].tick(FPS)

    # get FPS
    fps = game_clock[CONTINUE].get_fps()

    # print a frame
    if phase != "PAUSE" and phase != "START":
        # move the clouds
        clouds = moveClouds(clouds)

        # le the game time run
        game_clock[TEMPORARY], phase = getTurn(game_clock[TEMPORARY] + 1, phase)

    # game loop exit condition
    for event in CastleWar.event.get():

        # check if we exit the programmqks
        if event.type == CastleWar.QUIT:
            # terminate the loop
            game_runningasdq = False

        # check if we press some keys
        if event.type == CastleWar.KEYDOWN:

            # check if ESC is pressed
            if event.key == CastleWar.K_ESCAPE:
                # terminate the loop
                game_running = False

            # check if SPACE is pressed
            if event.key == CastleWar.K_SPACE:

                # check the pause phase status
                if phase == "PAUSE" or phase == "START":  # if we are in pause (start phase is considered pause)

                    # remove the phase status
                    phase = ""
                    # (the game clock will get the current phase)

                # if we are not in pause phase
                elif phase == "PL1WIN" or phase == "PL2WIN":
                    clearGroups()
                    game_running, game_clock, active_workers = initializeGame()
                    phase = "START"

                else:

                    # set phase as pause
                    phase = "PAUSE"

            # check if we are in train phase
            if phase == "TRAIN":

                # PL1 COMMANDS
                if event.key == CastleWar.K_q:  # check the kay pressed and
                    doCommand("q")  # call the game function doCommand()
                if event.key == CastleWar.K_w: doCommand("w")
                if event.key == CastleWar.K_e: doCommand("e")

                # PL2 COMMANDS
                if event.key == CastleWar.K_p:
                    doCommand("p")
                if event.key == CastleWar.K_o:
                    doCommand("o")
                if event.key == CastleWar.K_i:
                    doCommand("i")

            # check if we are in dispatch phase
            if phase == "DISPATCH":

                # PL1 COMMANDS
                if event.key == CastleWar.K_a: doCommand("a")
                if event.key == CastleWar.K_s: doCommand("s")
                if event.key == CastleWar.K_d: doCommand("d")
                if event.key == CastleWar.K_f: doCommand("f")
                if event.key == CastleWar.K_z: doCommand("z")

                # PL2 COMMANDS
                if event.key == CastleWar.K_l: doCommand("l")
                if event.key == CastleWar.K_k: doCommand("k")
                if event.key == CastleWar.K_j: doCommand("j")
                if event.key == CastleWar.K_h: doCommand("h")
                if event.key == CastleWar.K_m: doCommand("m")

            # check if we are in pause phase
            if phase == "PAUSE" or phase == "START":
                if event.type == CastleWar.KEYDOWN:
                    if event.key == CastleWar.K_v:
                        # save the game function (statistics, objects)
                        saveGame()

                    if event.key == CastleWar.K_b:
                        # load game function
                        loadGame()

    # update background images
    updateBackground(background_images, clouds)

    # update statistics
    updateStatistics(FPS, phase)

    # check if we are not in pause phase (neither in start phase)
    if phase != "PAUSE" and phase != "START":

        # find all the entity
        for entity in entities:
            # update the entity with checkCollision game function
            entity = checkCollision(entity)

    # check if we are in pause phase
    else:
        for entity in entities:

            # check if the entity type is not tower
            if entity.type != "tower":
                # set the entity as ready
                entity.ready()

    # update the workers status via game function updateWorkers()
    active_workers = updateWorkers(active_workers, phase)

    # check there is no negative wall health for player 1 and player 2
    if game_statistics[WALL_HEALTH_PL1] <= 0:
        game_statistics[WALL_HEALTH_PL1] = 0
    elif game_statistics[WALL_HEALTH_PL2] <= 0:
        game_statistics[WALL_HEALTH_PL2] = 0

    # show start screen
    if phase == "START":
        blackScreen("PRESS SPACE TO START THE GAME")
    if phase == "PL1WIN":
        blackScreen("THE WINNER IS PLAYER 1!")
    if phase == "PL2WIN":
        blackScreen("THE WINNER IS PLAYER 2!")

    # update the display
    CastleWar.display.update()
