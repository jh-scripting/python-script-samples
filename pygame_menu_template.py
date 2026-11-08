import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Indie Game Menu Template")

# Colors
DARK_BG = (24, 24, 30)
WHITE = (255, 255, 255)
GREEN = (46, 204, 113)
HOVER_GREEN = (39, 174, 96)

# Fonts
font_title = pygame.font.SysFont("arial", 48, bold=True)
font_btn = pygame.font.SysFont("arial", 28)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    start_btn = pygame.Rect(300, 250, 200, 50)
    quit_btn = pygame.Rect(300, 330, 200, 50)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(DARK_BG)

        # Title
        draw_text("GAME TITLE", font_title, WHITE, screen, WIDTH // 2, 150)

        # Start Button Hover Effect
        if start_btn.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_GREEN, start_btn, border_radius=8)
        else:
            pygame.draw.rect(screen, GREEN, start_btn, border_radius=8)

        # Quit Button Hover Effect
        if quit_btn.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (231, 76, 60), quit_btn, border_radius=8)
        else:
            pygame.draw.rect(screen, (192, 57, 43), quit_btn, border_radius=8)

        # Button Labels
        draw_text("Start Game", font_btn, WHITE, screen, start_btn.centerx, start_btn.centery)
        draw_text("Quit", font_btn, WHITE, screen, quit_btn.centerx, quit_btn.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    print("Start button clicked! Load game logic here.")
                if quit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
