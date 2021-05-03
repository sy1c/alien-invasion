import pygame

import game_functions as functions

from settings import Settings
from objects import Spacecraft

def run():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    spacecraft = Spacecraft(screen)

    while True:
        functions.check_events()
        functions.update_screen(settings, screen, spacecraft)

run()