import pygame
from pygame.sprite import Sprite
import random


class Ball(Sprite):
    """A class to manage every ball."""

    def __init__(self, ai_settings, screen):
        """Initiate the ball class."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image and get its rect.
        self.image = pygame.image.load('../images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set starting position near the top let corner
        self.rect.x = random.randint(self.rect.width, (self.ai_settings.screen_width - self.rect.width))
        self.rect.y = 0

        # store y position as decimal.
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.ai_settings.ball_drop_speed
        self.rect.y = self.y

    def blitme(self):
        """Draw image to screen."""
        self.screen.blit(self.image, self.rect)
