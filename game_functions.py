import sys
import json
import pygame
from ball import Ball
from pad import Pad
from time import sleep


def check_keydown_events(event, ai_settings, screen, stats, balls, pads):
    """Check which key has been pressed."""
    if event.key == pygame.K_RIGHT:
        for pad in pads.sprites():
            pad.moving_right = True
    elif event.key == pygame.K_LEFT:
        for pad in pads.sprites():
            pad.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, balls, pads)


def check_keyup_events(event, pads):
    """Check which key has been unpressed."""
    if event.key == pygame.K_RIGHT:
        for pad in pads.sprites():
            pad.moving_right = False
    elif event.key == pygame.K_LEFT:
        for pad in pads.sprites():
            pad.moving_left = False


def check_events(pads, stats, ai_settings, screen, balls, play_button, sb):
    """Check for key events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, balls, pads)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pads)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, play_button, stats, ai_settings, screen, balls, pads, sb)


def start_game(ai_settings, screen, stats, balls, pads, sb):
    # make mouse invisible
    pygame.mouse.set_visible(False)

    # Reset game.
    stats.game_active = True
    stats.reset_stats()
    sb.prep_score()
    sb.prep_highscore()
    sb.prep_level()
    sb.prep_balls()
    ai_settings.initialize_dynamic_settings()

    # clear all sprites.
    balls.empty()
    pads.empty()

    # create pad and ball
    create_ball(ai_settings, screen, balls)
    create_pad(ai_settings, screen, pads)


def check_play_button(mouse_x, mouse_y, play_button, stats, ai_settings, screen, balls, pads, sb):
    mouse_button = play_button.rect.collidepoint(mouse_x, mouse_y)
    if mouse_button and not stats.game_active:
        start_game(ai_settings, screen, stats, balls, pads, sb)


def create_ball(ai_settings, screen, balls):
    """Create new ball."""
    new_ball = Ball(ai_settings, screen)
    balls.add(new_ball)


def create_pad(ai_settings, screen, pads):
    """Create new pad."""
    new_pad = Pad(ai_settings, screen)
    pads.add(new_pad)


def screen_update(ai_settings, screen, balls, pads, play_button, stats, sb):
    "Update the screen."
    screen.fill(ai_settings.bg_color)
    sb.show_score()
    balls.draw(screen)
    for pad in pads.sprites():
        pad.draw_pad()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def ball_update(ai_settings, balls, stats, pads, screen, sb):
    """Update ball position."""
    balls.update()
    for ball in balls.sprites():
        if ball.rect.top >= ball.screen_rect.bottom:
            balls.remove(ball)
    check_ball_bottom(ai_settings, stats, balls, pads, screen, sb)


def ball_crash(ai_settings, stats, balls, pads, screen, sb):
    # Clear all balls and center pad.
    if stats.pads_left > 0:
        stats.pads_left -= 1
        sb.prep_balls()
        balls.empty()
        create_ball(ai_settings, screen, balls)
        for pad in pads.sprites():
            pad.center_pad()
        sleep(0.5)
    else:
        stats.game_active = False
        # make mouse visible
        pygame.mouse.set_visible(True)


def check_ball_bottom(ai_settings, stats, balls, pads, screen, sb):
    """Check if ball has reached bottom of screen."""
    screen_rect = screen.get_rect()
    for ball in balls.sprites():
        if ball.rect.bottom >= screen_rect.bottom:
            ball_crash(ai_settings, stats, balls, pads, screen, sb)


def pad_update(ai_settings, screen, balls, pads, stats, sb, filename):
    """update pads position."""
    pads.update()
    check_collision(ai_settings, screen, balls, pads, stats, sb, filename)


def check_collision(ai_settings, screen, balls, pads, stats, sb, filename):
    collisions = pygame.sprite.groupcollide(pads, balls, False, True)
    if len(balls) == 0:
        stats.score += ai_settings.ball_score
        stats.level += 1
        sb.prep_level()
        sb.prep_score()
        check_highscore(stats, filename, sb)
        ai_settings.speed_up()
        create_ball(ai_settings, screen, balls)


def check_highscore(stats, filename, sb):
    """Update high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        with open(filename, 'w') as f_obj:
            json.dump(stats.score, f_obj)
        sb.prep_highscore()
