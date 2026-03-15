import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goblin Battle")

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
GREEN = (50, 180, 50)
BLUE = (50, 100, 255)
GREY = (200, 200, 200)

player_hp = 30
enemy_hp = 97
enemy_max_hp = 97
message = "A wild Goblin appears!"

attack_button = pygame.Rect(100, 500, 150, 50)
heal_button = pygame.Rect(300, 500, 150, 50)

running = True
game_over = False

while running:
    screen.fill(WHITE)

    # Draw text
    player_text = font.render(f"Player HP: {player_hp}", True, BLACK)
    enemy_text = font.render(f"Goblin HP: {enemy_hp}/{enemy_max_hp}", True, BLACK)
    message_text = small_font.render(message, True, BLACK)

    screen.blit(player_text, (50, 50))
    screen.blit(enemy_text, (500, 50))
    screen.blit(message_text, (50, 400))

    # Draw goblin as a simple rectangle placeholder
    pygame.draw.rect(screen, GREEN, (550, 150, 120, 120))
    goblin_label = small_font.render("GOBLIN", True, BLACK)
    screen.blit(goblin_label, (575, 280))

    # Draw buttons
    pygame.draw.rect(screen, RED, attack_button)
    pygame.draw.rect(screen, BLUE, heal_button)

    attack_text = small_font.render("Attack", True, WHITE)
    heal_text = small_font.render("Heal", True, WHITE)

    screen.blit(attack_text, (attack_button.x + 40, attack_button.y + 15))
    screen.blit(heal_text, (heal_button.x + 50, heal_button.y + 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()

            if attack_button.collidepoint(mouse_pos):
                damage = random.randint(4, 8)
                enemy_hp -= damage
                message = f"You dealt {damage} damage!"

                if enemy_hp > 0:
                    enemy_damage = random.randint(3, 7)
                    player_hp -= enemy_damage
                    message += f" Goblin dealt {enemy_damage} damage!"
                else:
                    message = "You defeated the Goblin!"
                    game_over = True

            if heal_button.collidepoint(mouse_pos):
                heal = random.randint(3, 6)
                player_hp += heal
                message = f"You healed {heal} HP!"

                if enemy_hp > 0:
                    enemy_damage = random.randint(3, 7)
                    player_hp -= enemy_damage
                    message += f" Goblin dealt {enemy_damage} damage!"

        if player_hp <= 0:
            message = "You were defeated..."
            game_over = True

    pygame.display.update()

pygame.quit()
