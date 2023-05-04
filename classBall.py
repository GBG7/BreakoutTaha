# This is ball class, responsible for ball movement, collision and creation
import pygame
from random import randint
black = (0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # Pass in brick color and X & Y position
        # Set color to black
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        # Draw  ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # chooses random number for velocity
        self.velocity = [randint(4,8),randint(-8,8)]
        # Get rectangle object with img dimensions
        self.rect = self.image.get_rect()

    # Controls bounce
    # if collision is detected with the wall,
    # velocity is reversed.
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    # Location of ball is correlated with velocity
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

