class Settings:
    """Class for game settings"""
    
    def __init__(self):
        
        #screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 139)
        self.caption = "Bubble Popper"
        
        self.bubble_min_r = 10
        self.bubble_max_r = 50
        
        self.enemy_min_r = 10
        self.enemy_max_r = 50
        
        self.bonus_score = 1000
