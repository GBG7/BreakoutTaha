# This is the brick class, responsible for brick creation

import pygame
black = (0,0,0)

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # Pass in brick color and X & Y position
        # Set color to black
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        # Draw brick
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # Get rectangle object with img dimensions
        self.rect = self.image.get_rect()
