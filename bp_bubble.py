import random
import pygame
from bp_player import Player

class Bubble(pygame.sprite.Sprite):
    """Class for bubble object"""
    
    
    
    def __init__(self, screen, game_settings, isBubbleEvil):
        super(Bubble, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect() 
        
        self.isevil = isBubbleEvil # does the bubble damage the player?
        if self.isevil == True:
            self.color = (255, 0, 0)
        else:
            self.color = (255, 255, 255)
        
        self.bubble_radius = random.randint(game_settings.bubble_min_r, game_settings.bubble_max_r)
        
        self.bubble = pygame.Surface((self.bubble_radius * 2, self.bubble_radius * 2), pygame.SRCALPHA)
        
        self.bubble.set_colorkey(game_settings.bg_color)
        
        self.bubble.set_alpha(128)
        
        self.rect = pygame.draw.circle(
            self.bubble,
            self.color,
            (self.bubble_radius, self.bubble_radius),
            self.bubble_radius,
            2)
        
        self.rect = self.bubble.get_rect(
            center=(
                random.randint(game_settings.screen_height + 20, game_settings.screen_width + 100),
                random.randint(0, game_settings.screen_height),
                )
            )
        self.speed = random.randint(1, 5)
        
        self.evilspeed = random.randint(8, 12)
    
    def update(self):
        if self.isevil:
            self.rect.move_ip(-self.evilspeed, 0)
        else:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
    def blit_me(self):
        self.screen.blit(self.bubble, self.rect)
        
def increase_evil_bubble_speed(bubbles):
        for bubble in bubbles:
            if bubble.isevil:
                bubble.evilspeed *= 1.02
