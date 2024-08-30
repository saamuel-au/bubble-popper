import pygame.font


class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        """Init scoreboard attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        self.prepare_score()
        self.prepare_level()
        self.prepare_lives()
        
        
        
        
    def prepare_score(self):
        """Convert score to graphics component"""
        score_str = str(f"Score: {self.stats.score}")
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 21
        self.score_image_rect.top = 20
        
    def prepare_level(self):
        """Convert level to graphics component"""
        level_str = str(f"Level: {self.stats.level}")
        self.level_image = self.font.render(level_str, True, self.text_color, self.game_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_image_rect.right
        self.level_rect.top = self.score_image_rect.bottom + 10
        
    def prepare_lives(self):
        """Convert lives to graphics component"""
        lives_str = str(f"Lives: {self.stats.health}")
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.game_settings.bg_color)
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.score_image_rect.right
        self.lives_rect.top = self.score_image_rect.bottom + 50
            
            
    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
