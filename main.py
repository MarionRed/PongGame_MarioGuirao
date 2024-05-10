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

    keys = pygame.key.get_pressed()
    #Dejo los prints para comprobar que se reconocen las teclas.
    print(keys[pygame.K_w])
    print(keys[pygame.K_s])
    print(keys[pygame.K_UP])
    print(keys[pygame.K_DOWN])

    #No he sabido como hacer que funcione sin duplicar.
    if keys[pygame.K_w] and jugador1.posY - 20 >= 50:
        jugador1.posY -= 20

    if keys[pygame.K_s] and jugador1.posY + 20 <= 50 + 300 - 100:
        jugador1.posY += 20

    if keys[pygame.K_UP] and jugador2.posY - 20 >= 50:
        jugador2.posY -= 20

    if keys[pygame.K_DOWN] and jugador2.posY + 20 <= 50 + 300 - 100:
        jugador2.posY += 20

def Pintar():
    finestraJoc.fill((255,255,255))
    pygame.draw.rect(finestraJoc, (0, 255, 0), (0, 50, 600, 300))
    pygame.draw.rect(finestraJoc, COLOR_JUGADOR1, (MARGES_ESCENARI, jugador1.posY, 20, 100))
    pygame.draw.rect(finestraJoc, COLOR_JUGADOR2, (520, jugador2.posY, 20, 100))

while not gameOver:

    DetectarEvents()
    Pintar()

    rellotge.tick(30)
    pygame.display.update()