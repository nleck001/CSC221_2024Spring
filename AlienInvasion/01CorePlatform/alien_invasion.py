import sys
import pygame
from settings import Settings


class AlienInvasion:
    """The game!"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("01 Alien Invasion")

    def run_game(self):
        """Runs the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    print("Create game object...")
    ai = AlienInvasion()

    print("Running game...")
    ai.run_game()

    print("Game complete")
