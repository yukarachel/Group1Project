import pygame
import random
import os
import sys
from pylsl import StreamInlet, resolve_byprop

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Where's Waldo")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Global variables
waldo_size = 50
num_other_sprites_start = 7
num_other_sprites1_start = 7
num_other_sprites2_start = 7
num_other_sprites3_start = 7
font = pygame.font.Font(None, 36)

# Load Waldo sprite
waldo_sprite = pygame.image.load(os.path.join("sprites", "waldo_sprite.png")).convert_alpha()
waldo_sprite = pygame.transform.scale(waldo_sprite, (waldo_size, waldo_size))

# Load other sprites
other_sprite = pygame.image.load(os.path.join("sprites", "other_sprite.png")).convert_alpha()
other_sprite = pygame.transform.scale(other_sprite, (waldo_size, waldo_size))

other_sprite1 = pygame.image.load(os.path.join("sprites", "other_sprite1.png")).convert_alpha()
other_sprite1 = pygame.transform.scale(other_sprite1, (waldo_size, waldo_size))

other_sprite2 = pygame.image.load(os.path.join("sprites", "other_sprite2.png")).convert_alpha()
other_sprite2 = pygame.transform.scale(other_sprite2, (waldo_size, waldo_size))

other_sprite3 = pygame.image.load(os.path.join("sprites", "other_sprite3.png")).convert_alpha()
other_sprite3 = pygame.transform.scale(other_sprite3, (waldo_size, waldo_size))

# Load background
background_sprite = pygame.image.load(os.path.join("sprites", "background_sprite.png")).convert_alpha()
background_sprite = pygame.transform.scale(background_sprite, (WIDTH, HEIGHT))

# Game variables
level = 1
sprites = []
waldo_pos = (0, 0)

def shuffle_sprites():
    global sprites, waldo_pos
    num_other_sprites = num_other_sprites_start + (level - 1) * 7  # Increase by 10 each level
    num_other_sprites1 = num_other_sprites1_start + (level - 1) * 7  # Increase by 10 each level
    num_other_sprites2 = num_other_sprites2_start + (level - 1) * 7  # Increase by 10 each level
    num_other_sprites3 = num_other_sprites3_start + (level - 1) * 7  # Increase by 10 each level
    sprites = []
    occupied_positions = set()
    
    # Place Waldo first
    while True:
        waldo_x, waldo_y = random.randint(0, WIDTH - waldo_size), random.randint(0, HEIGHT - waldo_size)
        grid_x, grid_y = waldo_x // waldo_size, waldo_y // waldo_size
        if (grid_x, grid_y) not in occupied_positions:
            occupied_positions.add((grid_x, grid_y))
            break
    
    waldo_pos = (waldo_x, waldo_y)
    sprites.append((waldo_sprite, waldo_x, waldo_y, True))  # True means it's Waldo
    
    # Place other sprites
    for _ in range(num_other_sprites):
        while True:
            x, y = random.randint(0, WIDTH - waldo_size), random.randint(0, HEIGHT - waldo_size)
            grid_x, grid_y = x // waldo_size, y // waldo_size
            if (grid_x, grid_y) not in occupied_positions:
                occupied_positions.add((grid_x, grid_y))
                sprites.append((other_sprite, x, y, False))
                break
    
    for _ in range(num_other_sprites1):
        while True:
            x, y = random.randint(0, WIDTH - waldo_size), random.randint(0, HEIGHT - waldo_size)
            grid_x, grid_y = x // waldo_size, y // waldo_size
            if (grid_x, grid_y) not in occupied_positions:
                occupied_positions.add((grid_x, grid_y))
                sprites.append((other_sprite1, x, y, False))
                break
    
    for _ in range(num_other_sprites2):
        while True:
            x, y = random.randint(0, WIDTH - waldo_size), random.randint(0, HEIGHT - waldo_size)
            grid_x, grid_y = x // waldo_size, y // waldo_size
            if (grid_x, grid_y) not in occupied_positions:
                occupied_positions.add((grid_x, grid_y))
                sprites.append((other_sprite2, x, y, False))
                break
    
    for _ in range(num_other_sprites3):
        while True:
            x, y = random.randint(0, WIDTH - waldo_size), random.randint(0, HEIGHT - waldo_size)
            grid_x, grid_y = x // waldo_size, y // waldo_size
            if (grid_x, grid_y) not in occupied_positions:
                occupied_positions.add((grid_x, grid_y))
                sprites.append((other_sprite3, x, y, False))
                break

def start_screen():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Welcome to Where's Waldo!")
    font = pygame.font.Font(None, 50)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))
    
    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background
        screen.blit(text, text_rect)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                game_body()

def game_body():
    global level
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Screen")
    font = pygame.font.Font(None, 50)
    shuffle_sprites()
    
    running = True
    while running:
        screen.fill(WHITE)
        
        # Draw sprites
        for img, x, y, is_waldo in sprites:
            screen.blit(img, (x, y))
        
        # Display level
        level_text = font.render(f"Level: {level}", True, BLACK)
        screen.blit(level_text, (10, 10))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if waldo_pos[0] <= mx <= waldo_pos[0] + waldo_size and waldo_pos[1] <= my <= waldo_pos[1] + waldo_size:
                    level += 1
                    shuffle_sprites()

if __name__ == "__main__":
    start_screen()
    pygame.quit()
