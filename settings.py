class Settings():
    """A class to manage all our settings"""

    def __init__(self):
        # Static game settings.
        """Screen settings"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = 255, 255, 255

        """Pad settings."""
        self.pads_limit = 3
        self.pad_width = 60
        self.pad_height = 10
        self.pad_color = 60, 60, 60

        # Game speed increase rate.
        self.speedup_scale = 1.05
        self.score_scale = 1.1

        self.initialize_dynamic_settings()
        self.speed_up()

    def initialize_dynamic_settings(self):
        self.ball_drop_speed = 0.6
        self.pad_speed_factor = 1.5
        self.ball_score = 10

    def speed_up(self):
        """Speed up game."""
        self.ball_drop_speed *= self.speedup_scale
        self.pad_speed_factor *= self.speedup_scale
        self.ball_score *= self.score_scale
