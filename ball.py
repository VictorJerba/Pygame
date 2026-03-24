import pygame
from config import *

class Ball:
    """
    Representa a bola do jogo.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED
        self.size = BALL_SIZE

    def move(self):

        self.x += self.speed_x
        self.y += self.speed_y

        if self.y <= 0 or self.y >= SCREEN_HEIGHT - self.size:
            self.speed_y *= -1

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            WHITE,
            (int(self.x), int(self.y)),
            self.size
        )

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.size,
            self.size
        )