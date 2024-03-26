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
        pygame.display.set_caption("04 Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Runs the game"""
        while True:
            if not self._check_events():
                return

            self.ship.update()
            self._update_screen()
            self.clock.tick(160)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT received")
                return False
            elif event.type == pygame.KEYDOWN:
                if not self._check_keydown_events(event):
                    print("'q' pressed")
                    return False
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

        return True
    
    def _check_keydown_events(self, event):
        #print(event.key)
        if event.key == pygame.K_z:
            self.ship.recenter()
        elif event.key == pygame.K_LEFT:
            self.ship.move_dx = -3
        elif event.key == pygame.K_RIGHT:
            self.ship.move_dx = 3
        elif event.key == pygame.K_q:
            return False
        
        return True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            self.ship.move_dx = 0

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
