# This is paddle class, responsible for paddle movement and collision
import pygame
black = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # Pass in brick color and X & Y position
        # Set color to black
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        # Draw brack a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # Get rectangle object with img dimensions
        self.rect = self.image.get_rect()
    # Detects left and right movement
    def moveRight(self, units):
        self.rect.x += units
        # If paddle does off the right edge of the screen
        # bring it back on screen
        if self.rect.x > 1100:
          self.rect.x = 1100
    # Detects left and right movement
    def moveLeft(self, units):
        self.rect.x -= units
        # If paddle does off the left edge of the screen
        # bring it back on screen
        if self.rect.x < 0:
          self.rect.x = 0


