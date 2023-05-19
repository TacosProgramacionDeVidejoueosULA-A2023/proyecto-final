# game setup
import os

WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64

SPRITES_SYMBOL = {
    "g": "grass",
    "c": "cobble",
    "s": "stone",
    "b": "bush",
    "p": "player",
    "t": "tree",
    "e": "red",
}

ASSETS_PATH = os.getcwd() + "/assets"
GRAPHICS_PATH = ASSETS_PATH + "/graphics"
ENIRONMENT_PATH = GRAPHICS_PATH + "/environment"
ENEMIES_PATH = GRAPHICS_PATH + "/enemies"
MAPS_PATH = ASSETS_PATH + "/maps"

monster_data = {
    "globin": {
        "health": 100,
        "exp": 100,
        "damage": 20,
        "speed": 3,
        "resistance": 3,
        "attack_radius": 80,
        "notice_radius": 360,
    }
}

player_data = {
    "health": 100,
    "exp": 100,
    "damage": 20,
    "speed": 3,
    "resistance": 3,
    "attack_radius": 80,
    "notice_radius": 360,
}

HOME_SCREEN_INSTRUCTIONS = ["Press `Enter` to Start","Press `Esc` to Quit"]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
