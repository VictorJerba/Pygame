import pygame
from config import *

class Player:


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = 5

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE,
                         (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)