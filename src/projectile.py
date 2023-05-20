import pygame
from .settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, groups, status, color):
        super().__init__(groups)
        self._layer = 2
        self.speed = 10

        self.image = pygame.Surface([4, 10])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.status = status

    def update(self):
            if self.status == "left":
                self.rect.x -= self.speed
            if self.status == "right":
                self.rect.x += self.speed
            if self.status == "up":
                self.rect.y -= self.speed
            if self.status == "down":
                self.rect.y += self.speed
        