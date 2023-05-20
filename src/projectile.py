import pygame
from .settings import *
from .enemy import Enemy
from .support import import_folder

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, color, status, attack=10):
        super().__init__([groups[0]])
        self._layer = 2
        self.speed = 10

        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.obstacle_sprites = obstacle_sprites

        self.frame_index = 0
        self.attack = attack
        self.color = color
        self.status = status

        power_name = ""
        if self.color == "red":
            power_name = "fireball"
        else:
            power_name = "whirlwind"

        power_frames = os.path.join(SFX_PATH, power_name)
        self.animations = import_folder(power_frames)
        self.animation_speed = 0.15

        self.image = self.animations[int(self.frame_index)]
        self.rect = self.image.get_rect()
        self.hitbox = self.rect

    def update(self):
        if self.status == "left":
            self.hitbox.x -= self.speed
        if self.status == "right":
            self.hitbox.x += self.speed
        if self.status == "up":
            self.hitbox.y -= self.speed
        if self.status == "down":
            self.hitbox.y += self.speed
        self.animate(self.status)
        self.collision()

    def collision(self):
        for sprite in self.obstacle_sprites:
            if type(sprite).__name__ == "Player":
                continue
            
            if sprite.hitbox.colliderect(self.hitbox):
                self.kill()
                if isinstance(sprite, Enemy):
                    sprite.health -= self.attack

    def animate(self, direction):
        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0

        # set the image
        if direction == "left":
            angle = 90
        elif direction ==  "right":
            angle = 270
        elif direction ==  "up":
            angle = 0
        elif direction ==  "down":
            angle = 180
                
        image = self.animations[int(self.frame_index)]
        self.image = pygame.transform.rotate(image, angle)
        self.rect = self.image.get_rect(center=self.hitbox.center)

