import pygame
from player import Player
from ball import Ball
from config import *

class Game:
    """
    Controla a lógica principal do jogo.
    """

    def __init__(self, screen):

        self.screen = screen
        self.clock = pygame.time.Clock()

        self.player = Player(
            15,
            SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        )

        self.bot = Player(
            SCREEN_WIDTH - 25,
            SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        )

        self.ball = Ball(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2
        )

        self.score_player = 0
        self.score_bot = 0

        self.font = pygame.font.SysFont(None, 36)

    def reset_ball(self):

        self.ball.x = SCREEN_WIDTH // 2
        self.ball.y = SCREEN_HEIGHT // 2

        self.ball.speed_x *= -1

    def handle_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player.move_up()

        if keys[pygame.K_DOWN]:
            self.player.move_down()

    def update(self):

        self.ball.move()

        # colisão com jogador
        if self.ball.get_rect().colliderect(
                self.player.get_rect()):
            self.ball.speed_x *= -1

        # colisão com bot
        if self.ball.get_rect().colliderect(
                self.bot.get_rect()):
            self.ball.speed_x *= -1

        # ponto para bot
        if self.ball.x <= 0:
            self.score_bot += 1
            self.reset_ball()

        # ponto para player
        if self.ball.x >= SCREEN_WIDTH:
            self.score_player += 1
            self.reset_ball()

        # IA do bot
        if self.bot.y + self.bot.height // 2 < self.ball.y:
            self.bot.move_down()

        elif self.bot.y + self.bot.height // 2 > self.ball.y:
            self.bot.move_up()

    def draw(self):

        self.screen.fill(BLACK)

        self.player.draw(self.screen)
        self.bot.draw(self.screen)
        self.ball.draw(self.screen)

        # placar
        score_text = self.font.render(
            f"{self.score_player} - {self.score_bot}",
            True,
            WHITE
        )

        self.screen.blit(
            score_text,
            (SCREEN_WIDTH // 2 - 30, 20)
        )

        pygame.display.flip()

    def run(self):

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            self.handle_input()
            self.update()
            self.draw()

            self.clock.tick(FPS)