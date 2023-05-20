import pygame
from .settings import *
from .tile import Tile
from .player import Player
from .debug import debug
from .enemy import Enemy
import os


class Level:
    def __init__(self, map_name):
        self.level_map = None
        self.load_map_from_file(os.path.join(MAPS_PATH, map_name + ".txt"))

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.LayeredUpdates()

        # sprite setup
        self.create_map()

    def create_map(self):
        self.player = Player(
            (0, 0), [self.visible_sprites], self.obstacle_sprites
        )
        for row_index, row in enumerate(self.level_map):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                Tile((x, y), [self.visible_sprites], "g")

                if col == "p":
                    self.player.set_pos((x,y))
                elif col in ("-", "+"):
                    Enemy((x, y), [self.visible_sprites, self.obstacle_sprites], self.obstacle_sprites, col)
                elif col != " ":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], col)

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
        self.visible_sprites.enemy_update(self.player)
        if self.player.health <= 0:
            self.player.kill()
            return True

        return False

        


class CameraGroup(pygame.sprite.LayeredUpdates):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
		# getting the offset 
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

		# for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery and sprite._layer):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
