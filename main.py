import sys

import pygame

from constant import COLOR_JUGADOR1, MARGES_ESCENARI, COLOR_JUGADOR2, AMPLA_ESCENARI
from Jugador import Jugador

pygame.init()
finestraJoc = pygame.display.set_mode((600, 400))
rellotge = pygame.time.Clock()

gameOver = False

jugador1 = Jugador(MARGES_ESCENARI, 50, COLOR_JUGADOR1)
jugador2 = Jugador(AMPLA_ESCENARI - MARGES_ESCENARI - 20, 50, COLOR_JUGADOR2)
def DetectarEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.key.get_pressed()
    print(pygame.key.get_pressed()[pygame.K_w])

    pygame.key.get_pressed()
    print(pygame.key.get_pressed()[pygame.K_s])

    pygame.key.get_pressed()
    print(pygame.key.get_pressed()[pygame.K_UP])

    pygame.key.get_pressed()
    print(pygame.key.get_pressed()[pygame.K_DOWN])

    if pygame.key.get_pressed()[pygame.K_w]:
        jugador1.posY = jugador1.posY + 20

    if pygame.key.get_pressed()[pygame.K_s]:
        jugador1.posY = jugador1.posY - 20

    if pygame.key.get_pressed()[pygame.K_UP]:
        jugador2.posY = jugador2.posY + 20

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        jugador2.posY = jugador2.posY - 20

def Pintar():
    finestraJoc.fill((255,255,255))
    pygame.draw.rect(finestraJoc, (0, 255, 0), (0, 50, 600, 300))
    pygame.draw.rect(finestraJoc, COLOR_JUGADOR1, (MARGES_ESCENARI, 150, 20, 100))  # Jugador 1
    pygame.draw.rect(finestraJoc, COLOR_JUGADOR2, (520, 150, 20, 100))  # Jugador 2

while not gameOver:

    DetectarEvents()
    Pintar()

    rellotge.tick(30)
    pygame.display.update()
