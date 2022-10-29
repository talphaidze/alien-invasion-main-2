import pygame
from pygame.sprite import Sprite

class Pow(Sprite):
    """A class to manage powerups fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
       #for alien in self.aliens.sprites():
        #    if alien.check_edges():
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.powerup_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.powerup_width,
            self.settings.powerup_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the powerup's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the powerup.
        self.y -= self.settings.powerup_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_powerup(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
