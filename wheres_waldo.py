import pygame
import random
import os
from pylsl import StreamInlet, resolve_byprop

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Where's waldo")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Global variables
waldo_size = 50
num_sprites_start = 10
font = pygame.font.Font(None, 36)

# Load Waldo sprite
waldo_sprite = pygame.image.load(
    os.path.join("sprites", "waldo_sprite.png")
).convert_alpha()
waldo_sprite = pygame.transform.scale(waldo_sprite, (waldo_size, waldo_size))

# Load other sprites
other_sprite = pygame.image.load(
    os.path.join("sprites", "other_sprite.png")
).convert_alpha()
other_sprite = pygame.transform.scale(other_sprite, (waldo_size, waldo_size))

# Load background GIF
background_sprite = pygame.image.load(
    os.path.join("sprites", "background_sprite.png")
).convert_alpha()
background_sprite = pygame.transform.scale(background_sprite, (WIDTH, HEIGHT))

# Game variables
level = 1
sprites = []
waldo_pos = (0, 0)

# Shuffle_sprites 
def shuffle_sprites():
    global sprites, waldo_pos
    num_sprites = num_sprites_start + (level - 1) * 3
    sprites = []
    
    # Place Waldo first
    waldo_x, waldo_y = random.randint(0, WIDTH - waldo_size), random.randint(0, HEIGHT - waldo_size)
    waldo_pos = (waldo_x, waldo_y)
    sprites.append((waldo_sprite, waldo_x, waldo_y, True))  # True means it's Waldo
    
    # Place other sprites
    for _ in range(num_sprites - 1):
        x, y = random.randint(0, WIDTH - waldo_size), random.randint(0, HEIGHT - waldo_size)
        sprites.append((other_sprite, x, y, False))  # False means it's not Waldo

# Start first shuffle
shuffle_sprites()

running = True
while running:
    screen.fill(WHITE)
    
    # Draw sprites
    for img, x, y, is_waldo in sprites:
        screen.blit(img, (x, y))
    
    # Display level
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(level_text, (10, 10))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if waldo_pos[0] <= mx <= waldo_pos[0] + waldo_size and waldo_pos[1] <= my <= waldo_pos[1] + waldo_size:
                level += 1
                shuffle_sprites()

pygame.quit()

    # # Connect to LSL stream
    # streams = resolve_byprop("name", "obci_eeg1")
    # inlet = StreamInlet(streams[0])

    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             if event.button == 1 and slider_rect.collidepoint(event.pos):
    #                 slider_dragging = True
    #         elif event.type == pygame.MOUSEBUTTONUP:
    #             if event.button == 1:
    #                 slider_dragging = False
    #         elif event.type == pygame.MOUSEMOTION:
    #             if slider_dragging:
    #                 mouse_y = event.pos[1]
    #                 threshold = max(
    #                     0.0, min(15.0, (mouse_y - slider_y) / slider_height * 15.0)
    #                 )

    #     # Fetch EEG data
    #     chunk, _ = inlet.pull_chunk()
    #     if len(chunk) > 0:
    #         alpha_band_power = sum(data[2] for data in chunk) / len(chunk)
    #         if (
    #             alpha_band_power > threshold
    #             and not is_jumping
    #             and player_y > HEIGHT - player_size - jump_height
    #         ):
    #             is_jumping = True

    #     # Jump if triggered
    #     if is_jumping:
    #         if player_y > HEIGHT - player_size - jump_height:
    #             player_y -= player_speed
    #         else:
    #             is_jumping = False

    #     # Update player position
    #     if not is_jumping and player_y < HEIGHT - player_size:
    #         player_y += player_speed

    #     # Generate new cactus obstacle
    #     if len(cacti) == 0 or cacti[-1][0] < WIDTH - 200:
    #         cacti.append(generate_cactus())

    #     # Move obstacles and check for collisions
    #     cacti = [
    #         (cactus_x - player_speed, cactus_y, cactus_width, cactus_height)
    #         for cactus_x, cactus_y, cactus_width, cactus_height in cacti
    #         if cactus_x + cactus_width > 0
    #     ]

    #     for cactus in cacti:
    #         cactus_x, cactus_y, cactus_width, cactus_height = cactus

    #         # Check for collision with player
    #         if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(
    #             pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)
    #         ):
    #             score -= 20
    #             # Game over logic can be added here if needed
    #         else:
    #             score += 1

    #     # Draw elements
    #     draw_elements(waldo_sprite, cacti, slider_rect)
    #     pygame.display.update()
    #     clock.tick(30)

    # pygame.quit()


# if __name__ == "__main__":
#     main()
