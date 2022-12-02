import pygame
from pygame.sprite import Sprite

class UFO(Sprite):

    def __init__(self, ai_game):
        """Initialize the UFO, and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship.rect

        #Load the ufo image, and get its rectangle.
        self.image = pygame.image.load('alien_yel.png')
        self.rect = self.image.get_rect()

        #Start each UFO near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the UFO's exact horizontal position.
        self.x = float(self.rect.x)
        self.start_ufo()

    def check_edges(self):
        """Check if the UFO is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the UFO left and right."""
        self.x += (self.settings.ufo_speed * self.settings.ufo_direction)
        self.rect.x = self.x

    def start_ufo(self):
        """Initialize UFO outside screen and move into view."""
        self.rect.top += self.ship.height
        self.rect.right = 0
        self.update()

    def blitme(self):
        self.screen.blit(self.image, self.rect)