import os
import pygame

pygame.init()

def loadAssets():
    PLAYER_ASSETS = []
    GAME_ASSETS = []

    # loads big gun assets
    BIG_GUNS_IDLE = []
    BIG_GUNS_WALKING = []
    BIG_GUNS_SOUNDS = []

    BIG_GUNS_IDLE_PATH = os.getcwd() + "/resources/Big_Guns_Sprites/idle/"
    BIG_GUNS_WALKING_PATH = os.getcwd() + "/resources/Big_Guns_Sprites/walking/"

    for img in os.listdir(BIG_GUNS_IDLE_PATH):
        path = BIG_GUNS_IDLE_PATH + img
        BIG_GUNS_IDLE.append(pygame.image.load(path))
    for img in os.listdir(BIG_GUNS_WALKING_PATH):
        path = BIG_GUNS_WALKING_PATH + img
        BIG_GUNS_WALKING.append(pygame.image.load(path))

    # for sound in os.listdir("resources/Big_Guns_Sprites"):
    #     BIG_GUNS_SOUNDS.append(pygame.mixer.music.load(sound))

    BIG_GUNS_ASSETS = [BIG_GUNS_IDLE, BIG_GUNS_WALKING, BIG_GUNS_SOUNDS]

    PLAYER_ASSETS.append(BIG_GUNS_ASSETS)
    GAME_ASSETS.append(PLAYER_ASSETS)
    return GAME_ASSETS

