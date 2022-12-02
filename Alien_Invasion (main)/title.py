import pygame.font

class Title:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.button = ai_game.play_button
        self.button_rect = self.button.rect

        # Set the dimensions of the title.
        self.width, self.height = 600, 150
        self.bg_color = (79, 16, 115)
        self.text_color = (255,255,255)
        self.font = pygame.font.Font('ZenDots-Regular.ttf', 56)

        # Build the title's object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 3*self.button_rect.height
        self.preptitle(msg)

    def preptitle(self, msg):
        self.msg_image = self.font.render(msg,True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_title(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
