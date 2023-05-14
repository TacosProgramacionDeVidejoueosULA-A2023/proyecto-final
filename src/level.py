import pygame
from .settings import *
from .tile import Tile
from .player import Player
from .debug import debug
import os


class Level:
    def __init__(self, map_name):
        self.level_map = None
        self.load_map_from_file(os.path.join(MAPS_PATH, map_name + ".txt"))

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(self.level_map):
            for col_index, col in enumerate(row):
                if col != "p":
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    groups = [self.visible_sprites]
                    if col != "g":
                        groups.append(self.obstacle_sprites)
                        
                    Tile((x, y), groups, col)
                else:
                    Tile((x, y), [self.visible_sprites], 'g')
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites
                    )

    def load_map_from_file(self, filepath):
        print(filepath)
        self.level_map = []
        with open(filepath, "r") as map_file:
            for line in map_file:
                self.level_map.append(line.strip("\n").split(","))

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
