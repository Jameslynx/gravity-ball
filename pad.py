import pygame
from pygame.sprite import Sprite


class Pad(Sprite):
    """A class to manage the pad"""

    def __init__(self, ai_settings, screen):
        """Initiate the pads class."""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Create pad and set its position.
        self.rect = pygame.Rect(0, 0, self.ai_settings.pad_width, self.ai_settings.pad_height)
        self.screen_rect = screen.get_rect()

        # Set its position.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.color = self.ai_settings.pad_color

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # store the x position a decimal.
        self.x = self.rect.x

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.pad_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.pad_speed_factor

        self.rect.x = self.x

    def center_pad(self):
        self.x = self.screen_rect.centerx

    def draw_pad(self):
        """Draw pad to screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
