import pygame
from bp_settings import Settings
from bp_button import Button
from bp_player import Player
from bp_bubble import Bubble
from bp_scoreboard import Scoreboard
from bp_game_stats import GameStats
import bp_game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()

    # Set up drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    play_button = Button(gm_settings, screen, "Play")
    stats = GameStats()
    sb = Scoreboard(gm_settings, screen, stats)
    clock = pygame.time.Clock()

    # Instantiate a player
    player = Player(screen)

    # Create groups to hold bubbles
    bubbles = pygame.sprite.Group()

    # Run until user asks to quit
    while True:
        gf.check_events(gm_settings, screen, player, bubbles, stats, play_button, sb)
        if stats.game_active:
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb, gm_settings)
            bubbles.update()
        else:
            bubbles.empty()
        gf.update_screen(gm_settings, screen, player, bubbles, clock, stats, play_button, sb)
        
run_game()
