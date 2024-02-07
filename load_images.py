import pygame
import os


def load_images(path, square_size):
    images = {}
    for file_name in os.listdir(path):
        if file_name.endswith('.png'):
            piece_name = os.path.splitext(file_name)[0]
            image_path = os.path.join(path, file_name)
            image = pygame.image.load(image_path).convert_alpha()
            images[piece_name] = pygame.transform.scale(image, (square_size, square_size))
    return images
