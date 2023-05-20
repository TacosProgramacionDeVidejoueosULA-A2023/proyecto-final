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
    "z": "bush",
    "p": "player",
    "t": "tree",
    "w": "wall",
    "l": "pole",
    "y": "tree2",
    "u": "wall2",
    "d": "door",
    "a": "chair_left",
    "b": "chair_up",
    "r": "chair_right",
    "o": "statue",
    "k": "rock",
    "x": "small_pole",
    "j": "sign",
    "i": "broken_pole",
    "f": "rip",
    "-": "blue-ghost",
    "+": "red-ghost"
}

ASSETS_PATH = os.getcwd() + "/assets"
GRAPHICS_PATH = ASSETS_PATH + "/graphics"
ENIRONMENT_PATH = GRAPHICS_PATH + "/environment"
ENEMIES_PATH = GRAPHICS_PATH + "/enemies"
MAPS_PATH = ASSETS_PATH + "/maps"
FONT = os.getcwd() + '/assets/graphics/fonts/H.TTF'
FONT_SIZE = 100

monster_data = {
    "red-ghost": {
        "health": 15,
        "exp": 100,
        "damage": 20,
        "speed": 3,
        "resistance": 2,
        "attack_radius": 80,
        "notice_radius": 360,
    },
    "blue-ghost": {
        "health": 15,
        "exp": 100,
        "damage": 20,
        "speed": 3,
        "resistance": 2,
        "attack_radius": 80,
        "notice_radius": 360,
    }
}

player_data = {
    "health": 100000,
    "exp": 100,
    "damage": 20,
    "speed": 5,
    "resistance": 3,
    "attack_radius": 80,
    "notice_radius": 360,
}

HOME_SCREEN_INSTRUCTIONS = ["Press `Enter` to Start","Press `Esc` to Quit"]