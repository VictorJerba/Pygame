import pygame
import sys
import random
import math

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Duas Bolas")

PRETO = (0,0,0)
VERMELHO = (255,0,0)
AZUL = (0,0,255)

clock = pygame.time.Clock()


x1 = 200
y1 = 200
raio = 30
vel_x1 = random.choice([-4,4])
vel_y1 = random.choice([-4,4])


x2 = 500
y2 = 300
vel_x2 = random.choice([-4,4])
vel_y2 = random.choice([-4,4])

rodando = True
while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

   
    x1 += vel_x1
    y1 += vel_y1

    if x1 + raio >= largura or x1 - raio <= 0:
        vel_x1 *= -1
    if y1 + raio >= altura or y1 - raio <= 0:
        vel_y1 *= -1

    
    x2 += vel_x2
    y2 += vel_y2

    if x2 + raio >= largura or x2 - raio <= 0:
        vel_x2 *= -1
    if y2 + raio >= altura or y2 - raio <= 0:
        vel_y2 *= -1

    
    distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if distancia <= raio * 2:
        vel_x1 *= -1
        vel_y1 *= -1
        vel_x2 *= -1
        vel_y2 *= -1

    pygame.draw.circle(tela, VERMELHO, (x1, y1), raio)
    pygame.draw.circle(tela, AZUL, (x2, y2), raio)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()