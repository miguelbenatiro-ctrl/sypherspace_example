''' 
Tasks:
- Change window size
- Change background colour
- Change window title

'''

import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Refresher")

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    # 1. Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update

    # 3. Draw
    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()
sys.exit()
