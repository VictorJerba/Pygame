import pygame
from game import Game
from config import *

def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    pygame.display.set_caption("Pong")

    game = Game(screen)

    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()