import pygame
import chess
from load_images import load_images
from draw_pieces import draw_pieces

pygame.init()

# Define colors and setup screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chessboard")
square_size = screen_width // 8

# Load images
images = load_images("pieces", square_size)
print(images.keys())

# Initialize the chess board
board = chess.Board()

# Main game loop
running = True
while running:
    # Draw chessboard (same as before)
    for row in range(8):
        for col in range(8):
            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

            # Draw pieces
    draw_pieces(screen, board, images, square_size)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
