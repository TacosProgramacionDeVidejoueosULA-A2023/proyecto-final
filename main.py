from src.settings import *
from src.game import Game
import pygame


if __name__ == "__main__":
    main_sound = pygame.mixer.Sound('./assets/music/main.mp3')
    main_sound.set_volume(0.5)
    main_sound.play(loops = -1)

    game = Game()
    game.run()
