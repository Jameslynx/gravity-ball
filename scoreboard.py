import pygame.font
from pygame.sprite import Group
from ball import Ball


class Scoreboard():
    """A class to manage the games dashboard."""

    def __init__(self, ai_settings, stats, screen):
        """Initialize scoreboard's attributes."""
        self.ai_settings = ai_settings
        self.stats = stats
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = 30, 30, 30
        self.font = pygame.font.SysFont(None, 48)

        # prep score.
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_balls()

    def prep_score(self):
        """Render score image and position it."""
        rounded_score = int(round(self.stats.score, -1))
        score = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score, True, self.text_color, self.ai_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = self.screen_rect.top

    def prep_highscore(self):
        """Render highscore image and position it."""
        rounded_highscore = int(round(self.stats.high_score, -1))
        high_score = "{:,}".format(rounded_highscore)
        self.high_score_image = self.font.render(high_score, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.screen_rect.top

    def prep_level(self):
        """Render level image and position it below scores."""
        level = "{:,}".format(self.stats.level)
        self.level_image = self.font.render(level, True, self.text_color, self.ai_settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = 50

    def prep_balls(self):
        """Create balls and postion them."""
        self.bs = Group()
        for ball in range(self.stats.pads_left):
            new_ball = Ball(self.ai_settings, self.screen)
            new_ball.rect.top = self.screen_rect.top
            new_ball.rect.x = 10 + new_ball.rect.width * ball
            self.bs.add(new_ball)

    def show_score(self):
        """Draw score to screen."""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.bs.draw(self.screen)
