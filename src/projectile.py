import pygame
from .settings import *
from .enemy import Enemy


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, status, color, attack=10):
        super().__init__(groups)
        self._layer = 2
        self.speed = 10

        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.obstacle_sprites = obstacle_sprites

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect
        self.status = status
        self.attack = attack

    def update(self):
        self.collision()
        if self.status == "left":
            self.rect.x -= self.speed
        if self.status == "right":
            self.rect.x += self.speed
        if self.status == "up":
            self.rect.y -= self.speed
        if self.status == "down":
            self.rect.y += self.speed

    def collision(self):
        for sprite in self.obstacle_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                self.kill()
                if isinstance(sprite, Enemy):
                    sprite.health -= self.attack
