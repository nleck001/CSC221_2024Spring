import sys
import pygame

class AlienInvasion:
    """The game!"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("00 Alien Invasion by Ned")

    def run_game(self):
        """Runs the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == "__main__":
    print("Create game object...")
    ai = AlienInvasion()

    print("Running game...")
    ai.run_game()
