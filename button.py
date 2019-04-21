import pygame.font


class Button():
    """A class to manage button."""

    def __init__(self, screen, ai_settings, msg):
        """Initiate the button's attributes."""

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # give the button its features.
        self.width, self.height = 200, 50
        self.button_color = 0, 255, 0
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)

        # set position of button.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the msg is prepped onlu once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and position it."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """draw button the add msg."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
