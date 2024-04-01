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

    def run_game(self):
        """Runs the game"""
        while True:
            if not self._check_events():
                return

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('QUIT received')
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 3
                elif event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 3
                elif event.key == pygame.K_UP:
                    self.ship.rect.y -= 3
                elif event.key == pygame.K_DOWN:
                    self.ship.rect.y += 3
            elif event.type == pygame.KEYUP:
                pass

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
