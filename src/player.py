import pygame
from .settings import *
from .support import import_folder
import os
from .entity import Entity
from .projectile import Projectile


class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, layer=2, speed=5):
        super().__init__(groups, obstacle_sprites, layer=layer, speed=speed)
        self.image = pygame.image.load(
            os.getcwd() + "/assets/graphics/player/down/down_0.png"
        ).convert_alpha()
        self.set_pos(pos)

        # assets setup
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = 0.15

        # movement
        self.direction = pygame.math.Vector2()
        self.attacking = False
        self.attack_cooldown = 250
        self.attack_time = None
        self.dead = False

        self.health = player_data["health"]
        self.exp = player_data["exp"]
        self.speed = player_data["speed"]
        self.attack_damage = player_data["damage"]
        self.resistance = player_data["resistance"]
        self.attack_radius = player_data["attack_radius"]
        self.notice_radius = player_data["notice_radius"]

        self.obstacle_sprites = obstacle_sprites
        self._layer = layer

    def set_pos(self, pos):
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

    def import_player_assets(self):
        character_path = os.getcwd() + "/assets/graphics/player/"
        self.animations = {"up": [], "down": [], "left": [], "right": []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

        if not self.attacking:
            if mouse_pressed[0]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                projectile = Projectile(
                    self.rect.topleft, self.groups, self.obstacle_sprites, self.status, 'red'
                )
                projectile.rect.x = self.rect.x + 25
                projectile.rect.y = self.rect.y + 25
            elif mouse_pressed[2]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                projectile = Projectile(
                    self.rect.topleft, self.groups, self.obstacle_sprites, self.status, 'blue'
                )
                projectile.rect.x = self.rect.x + 25
                projectile.rect.y = self.rect.y + 25

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.animate()
        self.move(self.speed)
        if self.health <= 0:
            self.dead = True
