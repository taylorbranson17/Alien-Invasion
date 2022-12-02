import pygame
from game_stats import GameStats

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        #Ship settings
        self.ship_limit = 3

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 17
        self.bullet_color = (242, 33, 10)
        self.bullets_allowed = 5

        # Alien settings.
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.ufo_speed = 1.5

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.ufo_direction = 1

        # Scoring
        self.alien_points = 50
        self.ufo_points = 500


    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ufo_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        self.ufo_points = int(self.ufo_points * self.score_scale)