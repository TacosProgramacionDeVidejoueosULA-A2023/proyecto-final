import pygame
from .settings import *
from .entity import Entity
from .support import *
import os


class Enemy(Entity):
    def __init__(self, pos, groups, obstacle_sprites, sprite_symbol):
        # general setup
        super().__init__(groups, obstacle_sprites)
        self.sprite_type = "enemy"
        self.monster_name = SPRITES_SYMBOL[sprite_symbol]

        self.status = "idle"
        self.image = pygame.image.load(
			os.path.join(ENEMIES_PATH, self.monster_name + ".png")
        ).convert_alpha()

        # movement
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -10)
        self.obstacle_sprites = obstacle_sprites

        # stats
        monster_info = monster_data[self.monster_name]
        self.health = monster_info["health"]
        self.exp = monster_info["exp"]
        self.speed = monster_info["speed"]
        self.attack_damage = monster_info["damage"]
        self.resistance = monster_info["resistance"]
        self.attack_radius = monster_info["attack_radius"]
        self.notice_radius = monster_info["notice_radius"]

        # player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

        self._layer = 2

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if player.rect.colliderect(self.rect) and self.can_attack:
            self.status = "attack"
        elif distance <= self.notice_radius:
            self.status = "move"
        else:
            self.status = "idle"

        

    def actions(self, player):
        if self.status == "attack":
            self.attack_time = pygame.time.get_ticks()
            player.health -= self.attack_damage
            self.can_attack = False
        elif self.status == "move":
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def update(self):
        self.move(self.speed)
        self.cooldown()
        if self.health <= 0:
            self.kill()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)

