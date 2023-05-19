from .settings import *
import sys
import pygame
from .level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.level = None

    def render_home_screen(self):
        font = pygame.font.SysFont("arial", 50)
        title = font.render("HENRY SPOTER", True, (255, 255, 255))
        self.screen.blit(
            title,
            (
                WIDTH / 2 - title.get_width() / 2,
                HEIGTH / 2 - title.get_height() / 2,
            ),
        )

        font = pygame.font.SysFont("arial", 20, italic=True)
        for i, instruction_text in enumerate(HOME_SCREEN_INSTRUCTIONS):
            instruction = font.render(instruction_text, True, (255, 255, 255))
            self.screen.blit(
                instruction,
                (
                    WIDTH / 2 - instruction.get_width() / 2,
                    HEIGTH / 2 + instruction.get_height() * (2 * (i + 1)),
                ),
            )

    def render(self, screen):
        if screen == "home_screen":
            self.render_home_screen()
        elif screen == "starter":
            if self.level is None:
                self.level = Level("starter")
            self.level.run()

    def run(self):
        screen = "home_screen"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif  event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    screen = "starter"

            self.screen.fill("black")
            self.render(screen)
            pygame.display.update()
            self.clock.tick(FPS)