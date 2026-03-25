import pygame
import random
from player import Player
from ball import Ball
from config import *

class Game:

    def __init__(self, screen):

        self.screen = screen

        self.player = Player(30, SCREEN_HEIGHT // 2)
        self.bot = Player(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2)

        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.clock = pygame.time.Clock()
        self.running = True

        self.score_player = 0
        self.score_bot = 0

        self.game_started = False

        pygame.mixer.init()

        self.paddle_sound = pygame.mixer.Sound("assets/sounds/bola.wav")
        self.score_sound = pygame.mixer.Sound("assets/sounds/win.wav")

        self.font = pygame.font.Font(None, 50)

    def handle_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player.move_up()

        if keys[pygame.K_DOWN]:
            self.player.move_down()

    def update(self):

        if not self.game_started:
            return

        self.ball.move()

        # IA do bot
        if self.bot.y < self.ball.y:
            self.bot.move_down()

        if self.bot.y > self.ball.y:
            self.bot.move_up()

        # colisão jogador
        if self.ball.get_rect().colliderect(self.player.get_rect()):

            self.ball.speed_x *= -1

            # variação aleatória no ângulo
            self.ball.speed_y += random.uniform(-2, 2)

            self.paddle_sound.play()

        # colisão bot
        if self.ball.get_rect().colliderect(self.bot.get_rect()):

            self.ball.speed_x *= -1

            # variação aleatória no ângulo
            self.ball.speed_y += random.uniform(-2, 2)

            self.paddle_sound.play()

        # colisão parede
        if self.ball.y <= 0 or self.ball.y >= SCREEN_HEIGHT:

            self.ball.speed_y *= -1

            # pequena variação
            self.ball.speed_x += random.uniform(-1, 1)

        # ponto bot
        if self.ball.x <= 0:

            self.score_bot += 1
            self.score_sound.play()
            self.ball.reset()

        # ponto player
        if self.ball.x >= SCREEN_WIDTH:

            self.score_player += 1
            self.score_sound.play()
            self.ball.reset()

    def draw(self):

        self.screen.fill(BLACK)

        pygame.draw.line(
            self.screen,
            WHITE,
            (SCREEN_WIDTH // 2, 0),
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT),
            2
        )

        self.player.draw(self.screen)
        self.bot.draw(self.screen)
        self.ball.draw(self.screen)

        score_text = self.font.render(
            f"{self.score_player}   {self.score_bot}",
            True,
            WHITE
        )

        self.screen.blit(
            score_text,
            (SCREEN_WIDTH // 2 - 40, 20)
        )

        if not self.game_started:

            start_text = self.font.render(
                "Press SPACE to start",
                True,
                WHITE
            )

            self.screen.blit(
                start_text,
                (
                    SCREEN_WIDTH // 2 - 150,
                    SCREEN_HEIGHT // 2
                )
            )

        pygame.display.flip()

    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_started = True

            self.handle_input()
            self.update()
            self.draw()

            self.clock.tick(FPS)