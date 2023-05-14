import pygame
from .settings import *
import os


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, tile_char, layer=1):
        super().__init__(groups)
        sprite_name = SPRITES_SYMBOL[tile_char]
        self.image = pygame.image.load(
            os.path.join(ENIRONMENT_PATH, sprite_name + ".png")
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        if tile_char != "g":
            self.hitbox = self.rect.inflate(0, -10)
        
        self._layer = layer
