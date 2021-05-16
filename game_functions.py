import sys
import pygame
from pygame.constants import KEYDOWN

def check_keydown_events(event, spacecraft):
    if event.key == pygame.K_RIGHT:
        spacecraft.moving_right = True
    elif event.key == pygame.K_LEFT:
        spacecraft.moving_left = True

def check_keyup_events(event, spacecraft):
    if event.key == pygame.K_RIGHT:
        spacecraft.moving_right = False
    elif event.key == pygame.K_LEFT:
        spacecraft.moving_left = False

def check_events(spacecraft):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, spacecraft)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spacecraft)

def update_screen(settings, screen, spacecraft):
    screen.fill(settings.bg_color)
    spacecraft.blitme()

    pygame.display.flip()