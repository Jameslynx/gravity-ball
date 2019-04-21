import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Initialize the game."""
    filename = "Highscore.json"

    pygame.init()
    ai_settings = Settings()
    # Create screen.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Set title
    pygame.display.set_caption('Ball')

    # Create an instance of game stats.
    stats = GameStats(ai_settings, filename)

    # create ball and pad.
    balls = Group()
    pads = Group()
    gf.create_ball(ai_settings, screen, balls)
    gf.create_pad(ai_settings, screen, pads)

    play_button = Button(screen, ai_settings, 'Play')
    sb = Scoreboard(ai_settings, stats, screen)

    while True:
        """Initiate the game loop."""
        gf.check_events(pads, stats, ai_settings, screen, balls, play_button, sb)
        if stats.game_active:
            gf.pad_update(ai_settings, screen, balls, pads, stats, sb, filename)
            gf.ball_update(ai_settings, balls, stats, pads, screen, sb)
        gf.screen_update(ai_settings, screen, balls, pads, play_button, stats, sb)


run_game()
