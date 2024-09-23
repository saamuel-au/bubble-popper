import sys
import pygame
import random
import time
from bp_bubble import Bubble
#add additional user event
pygame.init()
ADDBUBBLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBUBBLE, 250)

def check_events(game_settings, screen, player, bubbles, stats, play_button, sb):
    """Check keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
        elif event.type == ADDBUBBLE:
            create_bubble(game_settings, screen, bubbles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, sb)

def check_play_button(stats, play_button, mouse_x, mouse_y, sb):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        sb.prepare_score()
        sb.prepare_level()
        sb.prepare_lives()

def create_bubble(game_settings, screen, bubbles):
    if random.randint(1,10) == 1: # 10% chance to spawn an evil bubble
        new_bubble = Bubble(screen, game_settings, True)
    else:
        new_bubble = Bubble(screen, game_settings, False)
    bubbles.add(new_bubble)

def update_bubbles(player, bubbles, stats, sb, game_settings):
    hitted_bubble = pygame.sprite.spritecollideany(player, bubbles)
    if hitted_bubble != None:
        if hitted_bubble.isevil != True:
            stats.score += hitted_bubble.bubble_radius
            sb.prepare_score()
            if (int(stats.score / game_settings.bonus_score)) > stats.bonus:
                stats.level += 1
                sb.prepare_level()
                stats.bonus += 1
            hitted_bubble.kill()
        else:
            if not player.godded:
                player.god_player()
                stats.health -= 1
                sb.prepare_lives()
                hitted_bubble.kill()
            
def stop_game(stats):
    stats.game_active = False #stop the game once the player is dead
    stats.reset_stats()

def update_screen(game_settings, screen, player, bubbles, clock, stats, play_button, sb):
    """Update image on screen and draw new screen"""
    #background
    screen.fill(game_settings.bg_color)
    
    # Handles god mode and the flashing effect
    player.check_god_mode()
    if player.godded and int(pygame.time.get_ticks() / 100) % 2 == 0:
        player.player.set_alpha(128)
    else:
        player.player.set_alpha(255)
    
    #add player to screen
    player.blit_me()
    
    #check if player is dead
    if stats.health < 1:
        stop_game(stats)
        play_button.prepare_msg("Retry")
    
    #add bubbles to screen
    for bubble in bubbles:
        bubble.blit_me()
        
    sb.draw_score()
        
    #game rate is 30 frames per second
    clock.tick(30)
    
    if not stats.game_active:
        play_button.draw_button()
    
    #display the last screen
    pygame.display.flip()
