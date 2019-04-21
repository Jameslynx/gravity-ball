import json


class GameStats():
    """Track statistics of ball game."""

    def __init__(self, ai_settings, filename):
        """Initialize statistics."""

        self.game_active = False
        self.ai_settings = ai_settings
        self.reset_stats()
        with open(filename) as f_obj:
            self.high_score = json.load(f_obj)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.pads_left = self.ai_settings.pads_limit
        self.score = 0
        self.level = 1
