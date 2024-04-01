import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """The game!"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("03 Alien Invasion")
        self.ship = Ship(self)
        
        # Desired ship motion per loop
        self.dx = 0
        self.dy = 0

    def run_game(self):
        """Runs the game"""
        while True:
            if not self._check_events():
                return

            # Always move the ship by dx,dy
            self.ship.rect.x += self.dx
            self.ship.rect.y += self.dy

            # Keep ship on screen
            if self.ship.rect.x < 0:
                self.ship.rect.x = 50
                self.dx = 0
            if self.ship.rect.y < 50:
                self.ship.rect.y = 0
                self.dx = 0
            if self.ship.rect.right > self.screen.get_width():
                self.ship.rect.right = self.screen.get_width()-50
            if self.ship.rect.bottom > self.screen.get_height():
                self.ship.rect.bottom = self.screen.get_height()-50


            # Now let's speed it up (unless dx == 0)
            self.dx *= 1.05
            self.dy *= 1.05

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('QUIT received')
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.dx = -3
                elif event.key == pygame.K_RIGHT:
                    self.dx = 3
                elif event.key == pygame.K_UP:
                    self.dy = -3
                elif event.key == pygame.K_DOWN:
                    self.dy = 3
            elif event.type == pygame.KEYUP:
                self.dx = 0
                self.dy = 0

        return True
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    print("Create game object...")
    ai = AlienInvasion()

    print("Running game...")
    ai.run_game()

    print("Game complete")
