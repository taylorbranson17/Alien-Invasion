import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position in decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def level_up(self):
        if self.stats.level == 5:
            self.color = (10, 200, 242)
            self.settings.bullet_width = 100
            self.settings.bullets_allowed = 2
        elif self.stats.level == 10:
            self.color = (242, 230, 10)
            self.settings.bullet_width = 200
            self.settings.bullets_allowed = 2
        else: 
            self.settings.bullet_width = 3
            self.color = (242, 33, 10)
            self.settings.bullets_allowed = 5

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)