import pygame
from config import *

class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.size = 10

        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

    def get_rect(self):
        return pygame.Rect(
            self.x - self.size,
            self.y - self.size,
            self.size * 2,
            self.size * 2
        )

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

        self.speed_x *= -1