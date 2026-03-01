'''
Tasks:

'''

import pygame
import sys

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Part 2 - Player Movement")

    clock = pygame.time.Clock()

    player = pygame.Rect(100, 100, 50, 50)
    speed = 5

    running = True
    while running:
        clock.tick(60)

        # 1) EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2) UPDATE
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

        # Keep player inside screen
        player.left = max(player.left, 0)
        player.right = min(player.right, WIDTH)
        player.top = max(player.top, 0)
        player.bottom = min(player.bottom, HEIGHT)

        # 3) DRAW
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (0, 200, 255), player)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
