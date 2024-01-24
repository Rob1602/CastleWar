### CASTLE WAR

# Functions

import pygame as CastleWar          # pygame library
from GameConstants import *         # game constants
from GameResources import *         # game resources
from random import randint          # random integer number genrator
from math import inf                # infinite positive value

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# initialize pygame
CastleWar.init()

# refresh all the group depandancies and the relative sprites
def refreshGroups():
    warriors.add(warriors_PL1)  # add a sprites group do an abstract sprites group
    warriors.add(warriors_PL2)
    entities.add(warriors)
    entities.add(arrows)

# empty all the groups
def clearGroups():
    warriors_PL1.empty()        # remove all the entities from a specific group
    warriors_PL2.empty()
    warriors.empty()
    arrows.empty()
    entities.empty()

# upgrade background and cloud function
def updateBackground(images, clouds):

    # print all the background images in their positions
    if CLOUDS and FPS >= 60:

        # add the cloud to the images list
        images = images + clouds

    # for every image in the list
    for n in range(0, len(images)):

        # print the image on the display
        game_screen.blit(images[n][0], images[n][1])

# display the statistics
def updateStatistics(fps, phase):

    # get the text list from the printStatistics() function
    printed_text = printStatistics(fps, phase)

    # for every text in the list
    for n in range(0, len(printed_text)):

        # print the text
        game_screen.blit(printed_text[n][0], printed_text[n][1])

# display the warriors
def updateEntities(type, sprite, position, width):
    refreshGroups()

    # if the entity is not a tower
    if type is not 'tower':

        # print the entity on the display
        game_screen.blit(sprite, (int(position[X] - int(width/2)), int(position[Y])))

# get the worker sprite function
def printWorker(active_workers, active_worker_role, worker_sprite_range, phase):

    # check if the the worker is active
    if active_workers[active_worker_role][ACTIVE] is True:

        # check if we are in wait phase
        if phase is "WORK":

            # update the worker sprite
            active_workers[active_worker_role][SPRITE] += WORKER_SPEED/30

            # worker sprites collection index bounding conditions
            if active_workers[active_worker_role][SPRITE] < worker_sprite_range[FIRST]:
                active_workers[active_worker_role][SPRITE] = worker_sprite_range[FIRST]
            if active_workers[active_worker_role][SPRITE] > worker_sprite_range[LAST]:
                active_workers[active_worker_role][SPRITE] = worker_sprite_range[LAST]
        else:
            active_workers[active_worker_role][SPRITE] = 0

    # return the current sprite index
    return active_workers[active_worker_role][SPRITE]

# print the workers at work if any
def updateWorkers(active_workers, phase):
    if game_statistics[WORKERS_MINE_PL1] > 0: active_workers[MINER_PL1][ACTIVE] = True
    if game_statistics[WORKERS_MINE_PL2] > 0: active_workers[MINER_PL2][ACTIVE] = True
    if game_statistics[WORKERS_WALL_PL1] > 0: active_workers[MASON_PL1][ACTIVE] = True
    if game_statistics[WORKERS_WALL_PL2] > 0: active_workers[MASON_PL2][ACTIVE] = True

    active_worker_role = MINER_PL1      # set the type and the player number for the worker
    worker_sprite_range = (1, 5)        # set the sprites collection range for the index

    # call tthe printWorker() function to update the sprite of the worker
    active_workers[active_worker_role][SPRITE] = printWorker(active_workers, active_worker_role, worker_sprite_range, phase)

    # print the worker sprite to the screen if active
    if active_workers[active_worker_role][ACTIVE]: game_screen.blit(worker_sprites_PL1[int(active_workers[active_worker_role][SPRITE])], (MINE_POS_X - WORKER_WITDH/2, BATTLEFIELD_HEIGHT))

    active_worker_role = MINER_PL2
    worker_sprite_range = (1, 5)
    active_workers[active_worker_role][SPRITE] = printWorker(active_workers, active_worker_role, worker_sprite_range, phase)
    if active_workers[active_worker_role][ACTIVE]: game_screen.blit(worker_sprites_PL2[int(active_workers[active_worker_role][SPRITE])], (SCREEN_WIDTH - MINE_POS_X - WORKER_WITDH/2, BATTLEFIELD_HEIGHT))

    active_worker_role = MASON_PL1
    worker_sprite_range = (5, 7)
    active_workers[active_worker_role][SPRITE] = printWorker(active_workers, active_worker_role, worker_sprite_range, phase)
    if active_workers[active_worker_role][ACTIVE]: game_screen.blit(worker_sprites_PL1[int(active_workers[active_worker_role][SPRITE])], (WALL_POS_X - WALL_WIDTH/2 - WORKER_WITDH/2, BATTLEFIELD_HEIGHT))

    active_worker_role = MASON_PL2
    worker_sprite_range = (5, 7)
    active_workers[active_worker_role][SPRITE] = printWorker(active_workers, active_worker_role, worker_sprite_range, phase)
    if active_workers[active_worker_role][ACTIVE]: game_screen.blit(worker_sprites_PL2[int(active_workers[active_worker_role][SPRITE])], (SCREEN_WIDTH - WALL_POS_X + WALL_WIDTH/2 - WORKER_WITDH/2, BATTLEFIELD_HEIGHT))

    # return the active workers current sprites
    return active_workers

# moving clouds function
def moveClouds(clouds):

    # change the clouds positions
    clouds[0][POSITION][X] -= CLOUD_SPEED_UNIT
    clouds[1][POSITION][X] -= CLOUD_SPEED_UNIT*2
    clouds[2][POSITION][X] -= CLOUD_SPEED_UNIT*3

    # if the clouds positions exceed the border reset the positions with new altitudes
    if clouds[0][POSITION][X] <= 0 - CLOUD_WIDTH:
        clouds[0][POSITION][X] = SCREEN_WIDTH
        clouds[0][POSITION][Y] = randint(1, 8) * BORDER
    if clouds[1][POSITION][X] <= 0 - CLOUD_WIDTH:
        clouds[1][POSITION][X] = SCREEN_WIDTH
        clouds[1][POSITION][Y] = randint(1, 8) * BORDER
    if clouds[2][POSITION][X] <= 0 - CLOUD_WIDTH:
        clouds[2][POSITION][X] = SCREEN_WIDTH
        clouds[2][POSITION][Y] = randint(1, 8) * BORDER

    # return clouds positions
    return clouds


# turn function
def getTurn(game_clock, phase):

    # check if the player health is 0
    if game_statistics[WALL_HEALTH_PL1] == 0:

        # lock the timer to 0
        game_clock = 0

        # empty all groups
        clearGroups()

        # enemy player win
        phase = "PL2WIN"

    elif game_statistics[WALL_HEALTH_PL2] == 0:
        game_clock = 0
        phase = "PL1WIN"

    # if no player has health at zero
    else:

        # check the turn phase basing on the clock
        if game_clock >= 0 and game_clock <= FPS*TURN_TIME*(1/3):

            # set the phase
            phase = "TRAIN"

        elif game_clock >= FPS*TURN_TIME*(1/3) and game_clock <= FPS*TURN_TIME*(2/3):
            phase = "DISPATCH"

        elif game_clock >= FPS*TURN_TIME*(2/3) and game_clock <= FPS*TURN_TIME:
            phase = "WORK"

        # check if it is the end of the turn
        elif game_clock > FPS*TURN_TIME:

            # add resources and wall helath basing on workers
            if game_statistics[WORKERS_MINE_PL1] > 0:
                game_statistics[RESOURCES_PL1] += game_statistics[WORKERS_MINE_PL1]
            if game_statistics[WORKERS_WALL_PL1] > 0:
                game_statistics[WALL_HEALTH_PL1] += game_statistics[WORKERS_WALL_PL1]
            if game_statistics[WALL_HEALTH_PL1] > WALL_HEALTH:
                game_statistics[WALL_HEALTH_PL1] = WALL_HEALTH
            if game_statistics[WORKERS_MINE_PL2] > 0:
                game_statistics[RESOURCES_PL2] += game_statistics[WORKERS_MINE_PL2]
            if game_statistics[WORKERS_WALL_PL2] > 0:
                game_statistics[WALL_HEALTH_PL2] += game_statistics[WORKERS_WALL_PL2]
            if game_statistics[WALL_HEALTH_PL2] > WALL_HEALTH:
                game_statistics[WALL_HEALTH_PL2] = WALL_HEALTH

            # update turn
            game_statistics[TURN] += 1

            # reset game clock
            game_clock = 0

    # return game clock and phase
    return game_clock, phase


# check collision function
def checkCollision(entity):

    # check the player number and set the enemy group
    if entity.player is 1: enemy_group = warriors_PL2
    elif entity.player is 2: enemy_group = warriors_PL1

    # get the list of sprites of the enemy group collided with the sprites
    collided_entities_list = CastleWar.sprite.spritecollide(entity, enemy_group, False)

    # set the collided_entity index at 0
    collided_entity = 0

    # set the initial distance at infinite
    distance = inf

    # if entity type is archer or swordsman
    if entity.type is 'archer' or entity.type is 'swordsman':

        # if the sprite collided some enemies
        if len(collided_entities_list) is not 0:

            # for every enemy collided
            for n in range(0, len(collided_entities_list)):

                # check the distance between the sprite and the enemy
                if abs(entity.position[X] - collided_entities_list[n].position[X]) < distance:

                    # set the lowest enemy distance
                    distance = abs(entity.position[X] - collided_entities_list[n].position[X])

                    # set the index with the enemy one
                    collided_entity = n

        # check if the entity is a swordsman
        if entity.type is 'swordsman':

            # if the entity has health_points
            if entity.health_points > 0:

                # if the sprite collided some enemies
                if len(collided_entities_list) is not 0:

                    # check if the distance between the sprite and the enemy is lower than the range
                    if abs(entity.position[X] - collided_entities_list[collided_entity].position[X]) < entity.range:

                        # subtract the entity hit_points to the collided enemy
                        collided_entities_list[collided_entity].health_points -= entity.attack()

                    else:
                        entity.run()
                else:
                    entity.run()

            # if the entity has no health_points
            else:
                entity.die()

        elif entity.type is 'archer':
            if entity.health_points > 0:
                if len(collided_entities_list) is not 0:
                    if abs(entity.position[X] - collided_entities_list[collided_entity].position[X]) < entity.range:
                        entity.shoot()
                    else:
                        entity.run()
                else:
                    entity.run()
            else:
                entity.die()

    elif entity.type is 'arrow':
        if len(collided_entities_list) is not 0:
            if abs(entity.position[X] - collided_entities_list[collided_entity].position[X]) <= collided_entities_list[collided_entity].dimension[WIDTH]/2 and abs(entity.position[Y] - collided_entities_list[collided_entity].position[Y]) <= collided_entities_list[collided_entity].dimension[HEIGHT]/2:
                collided_entities_list[0].health_points -= entity.hit()
            else:
                entity.move()
        else:
            entity.move()

    elif entity.type is 'tower':
        collided_entities_list = CastleWar.sprite.spritecollide(entity, enemy_group, False)
        if len(collided_entities_list) is not 0:

            # select a random target in the tower ranges every cycle
            collided_entity = randint(0, len(collided_entities_list) - 1)
            if abs(entity.position[X] - collided_entities_list[collided_entity].position[X]) <= entity.range:
                entity.shoot(collided_entities_list[collided_entity].position)




def printStatistics(fps, phase):
    # render list that contain pygame surfaces and text
    printed_text = []

    text_PL1 = FONT_MEDIUM.render(" PLAYER 1 ", True, RED, WHITE)       # set the text
    textRect_PL1 = text_PL1.get_rect()                                  # get the rectangle surface
    textRect_PL1.topleft = (BORDER, BORDER)                             # get the display starting point
    printed_text.append([text_PL1, textRect_PL1])               # 0

    text_PL2 = FONT_MEDIUM.render(" PLAYER 2 ", True, BLUE, WHITE)
    textRect_PL2 = text_PL2.get_rect()
    textRect_PL2.topright = (SCREEN_WIDTH - BORDER, BORDER)
    printed_text.append([text_PL2, textRect_PL2])               # 1

    text_res_PL1 = FONT_SMALL.render(" RESOURCES: " + str(game_statistics[RESOURCES_PL1]) + " ", True, RED, WHITE)
    textRect_res_PL1 = text_res_PL1.get_rect()
    textRect_res_PL1.topleft = (BORDER, 5*BORDER)
    printed_text.append([text_res_PL1, textRect_res_PL1])       # 2

    text_res_PL2 = FONT_SMALL.render(" RESOURCES: " + str(game_statistics[RESOURCES_PL2]) + " ", True, BLUE, WHITE)
    textRect_res_PL2 = text_res_PL2.get_rect()
    textRect_res_PL2.topright = (SCREEN_WIDTH - BORDER, 5*BORDER)
    printed_text.append([text_res_PL2, textRect_res_PL2])       # 3

    text_worker_PL1 = FONT_SMALL.render(" WORKERS AVAIBLE: " + str(game_statistics[WORKERS_AVAIBLE_PL1]) + " ", True, RED, WHITE)
    textRect_worker_PL1 = text_worker_PL1.get_rect()
    textRect_worker_PL1.topleft = (BORDER, 8*BORDER)
    printed_text.append([text_worker_PL1, textRect_worker_PL1]) # 4

    text_worker_PL2 = FONT_SMALL.render(" WORKERS AVAIBLE: " + str(game_statistics[WORKERS_AVAIBLE_PL2]) + " ", True, BLUE, WHITE)
    textRect_worker_PL2 = text_worker_PL2.get_rect()
    textRect_worker_PL2.topright = (SCREEN_WIDTH - BORDER, 8*BORDER)
    printed_text.append([text_worker_PL2, textRect_worker_PL2]) # 5

    text_sword_PL1 = FONT_SMALL.render(" SWORDSMEN AVAIBLE: " + str(game_statistics[SWORDSMEN_AVAIBLE_PL1]) + " ", True, RED, WHITE)
    textRect_sword_PL1 = text_sword_PL1.get_rect()
    textRect_sword_PL1.topleft = (BORDER, 11*BORDER)
    printed_text.append([text_sword_PL1, textRect_sword_PL1])   # 6

    text_sword_PL2 = FONT_SMALL.render(" SWORDSMEN AVAIBLE: " + str(game_statistics[SWORDSMEN_AVAIBLE_PL2]) + " ", True, BLUE, WHITE)
    textRect_sword_PL2 = text_sword_PL2.get_rect()
    textRect_sword_PL2.topright = (SCREEN_WIDTH - BORDER, 11*BORDER)
    printed_text.append([text_sword_PL2, textRect_sword_PL2])   # 7

    text_archer_PL1 = FONT_SMALL.render(" ARCHERS AVAIBLE: " + str(game_statistics[ARCHERS_AVAIBLE_PL1]) + " ", True, RED, WHITE)
    textRect_archer_PL1 = text_archer_PL1.get_rect()
    textRect_archer_PL1.topleft = (BORDER, 14*BORDER)
    printed_text.append([text_archer_PL1, textRect_archer_PL1]) # 8

    text_archer_PL2 = FONT_SMALL.render(" ARCHERS AVAIBLE: " + str(game_statistics[ARCHERS_AVAIBLE_PL2]) + " ", True, BLUE, WHITE)
    textRect_archer_PL2 = text_archer_PL2.get_rect()
    textRect_archer_PL2.topright = (SCREEN_WIDTH - BORDER, 14*BORDER)
    printed_text.append([text_archer_PL2, textRect_archer_PL2]) # 9

    text_turn = FONT_BIG.render(" TURN: " + str(int(game_statistics[TURN])) + " ", True, BLACK, WHITE)
    textRect_turn = text_turn.get_rect()
    textRect_turn.center = (SCREEN_WIDTH/2, 3*BORDER)
    printed_text.append([text_turn, textRect_turn])             # 10

    text_mine_PL1 = FONT_SMALL.render(" " + str(game_statistics[WORKERS_MINE_PL1]) + " ", True, RED, WHITE)
    textRect_mine_PL1 = text_mine_PL1.get_rect()
    textRect_mine_PL1.center = (MINE_POS_X, SCREEN_HEIGHT - 2*BORDER)
    if game_statistics[WORKERS_MINE_PL1] > 0: printed_text.append([text_mine_PL1, textRect_mine_PL1])       # 11

    text_mine_PL2 = FONT_SMALL.render(" " + str(game_statistics[WORKERS_MINE_PL2]) + " ", True, BLUE, WHITE)
    textRect_mine_PL2 = text_mine_PL2.get_rect()
    textRect_mine_PL2.center = (SCREEN_WIDTH - MINE_POS_X, SCREEN_HEIGHT - 2*BORDER)
    if game_statistics[WORKERS_MINE_PL2] > 0:printed_text.append([text_mine_PL2, textRect_mine_PL2])        # 12

    text_wall_PL1 = FONT_SMALL.render(" " + str(game_statistics[WORKERS_WALL_PL1]) + " ", True, RED, WHITE)
    textRect_wall_PL1 = text_wall_PL1.get_rect()
    textRect_wall_PL1.center = (WALL_POS_X - WALL_WIDTH/2, SCREEN_HEIGHT - 2*BORDER)
    if game_statistics[WORKERS_WALL_PL1] > 0: printed_text.append([text_wall_PL1, textRect_wall_PL1])       # 13

    text_wall_PL2 = FONT_SMALL.render(" " + str(game_statistics[WORKERS_WALL_PL2]) + " ", True, BLUE, WHITE)
    textRect_wall_PL2 = text_wall_PL2.get_rect()
    textRect_wall_PL2.center = (SCREEN_WIDTH - WALL_POS_X + WALL_WIDTH/2, SCREEN_HEIGHT - 2*BORDER)
    if game_statistics[WORKERS_WALL_PL2] > 0: printed_text.append([text_wall_PL2, textRect_wall_PL2])       # 14

    text_phase = FONT_BIG.render(" " + phase + " ", True, BLACK, YELLOW)
    textRect_phase = text_phase.get_rect()
    textRect_phase.center = (SCREEN_WIDTH/2, 8*BORDER)
    printed_text.append([text_phase, textRect_phase])                   # 15

    text_fps = FONT_SMALL.render(" FPS: " + str(int(fps)) + " ", True, WHITE, ORANGE)
    textRect_fps = text_fps.get_rect()
    textRect_fps.center = (SCREEN_WIDTH/2, 12*BORDER)
    if SHOW_FPS: printed_text.append([text_fps, textRect_fps])          # 16

    # set the hp text background color basing on player hp and print
    if game_statistics[WALL_HEALTH_PL1] <= WALL_HEALTH and game_statistics[WALL_HEALTH_PL1] > WALL_HEALTH*(2/3):
        text_hp_PL1 = FONT_SMALL.render("   HP: " + str(int(game_statistics[WALL_HEALTH_PL1])) + "   ", True, WHITE, GREEN)
    elif game_statistics[WALL_HEALTH_PL1] <= WALL_HEALTH*(2/3) and game_statistics[WALL_HEALTH_PL1] > WALL_HEALTH*(1/3):
        text_hp_PL1 = FONT_SMALL.render("   HP: " + str(int(game_statistics[WALL_HEALTH_PL1])) + "   ", True, WHITE, ORANGE)
    elif game_statistics[WALL_HEALTH_PL1] <= WALL_HEALTH*(1/3):
        text_hp_PL1 = FONT_SMALL.render("   HP: " + str(int(game_statistics[WALL_HEALTH_PL1])) + "   ", True, WHITE, RED)
    textRect_hp_PL1 = text_hp_PL1.get_rect()
    textRect_hp_PL1.center = (WALL_POS_X, SCREEN_HEIGHT - GROUND_HEIGHT - TOWER_HEIGHT - 3*BORDER)
    printed_text.append([text_hp_PL1, textRect_hp_PL1])                 # 17

    if game_statistics[WALL_HEALTH_PL2] <= WALL_HEALTH and game_statistics[WALL_HEALTH_PL2] > WALL_HEALTH*(2/3):
        text_hp_PL1 = FONT_SMALL.render("   HP: " + str(int(game_statistics[WALL_HEALTH_PL2])) + "   ", True, WHITE, GREEN)
    elif game_statistics[WALL_HEALTH_PL2] <= WALL_HEALTH*(2/3) and game_statistics[WALL_HEALTH_PL2] > WALL_HEALTH*(1/3):
        text_hp_PL1 = FONT_SMALL.render("   HP: " + str(int(game_statistics[WALL_HEALTH_PL2])) + "   ", True, WHITE, ORANGE)
    elif game_statistics[WALL_HEALTH_PL2] <= WALL_HEALTH*(1/3):
        text_hp_PL1 = FONT_SMALL.render("   HP: " + str(int(game_statistics[WALL_HEALTH_PL2])) + "   ", True, WHITE, RED)
    textRect_hp_PL1 = text_hp_PL1.get_rect()
    textRect_hp_PL1.center = (SCREEN_WIDTH - WALL_POS_X, SCREEN_HEIGHT - GROUND_HEIGHT - TOWER_HEIGHT - 3*BORDER)
    printed_text.append([text_hp_PL1, textRect_hp_PL1])                 # 18

    # return the text displaying
    return printed_text

# starting and ending screen
def blackScreen(text):

    # print on display black background
    game_screen.fill(BLACK)

    text_wall_PL2 = FONT_BIG.render(text, True, WHITE, BLACK)
    textRect_wall_PL2 = text_wall_PL2.get_rect()
    textRect_wall_PL2.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_screen.blit(text_wall_PL2, textRect_wall_PL2)
