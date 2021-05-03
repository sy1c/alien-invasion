import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, spacecraft):
    screen.fill(settings.bg_color)
    spacecraft.blitme()

    pygame.display.flip()