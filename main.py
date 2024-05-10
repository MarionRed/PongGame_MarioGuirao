import sys

import pygame

from constant import COLOR_JUGADOR1, MARGES_ESCENARI, COLOR_JUGADOR2, AMPLA_ESCENARI
from Jugador import Jugador
from Pilota import Pilota

pygame.init()
finestraJoc = pygame.display.set_mode((600, 400))
rellotge = pygame.time.Clock()

gameOver = False

jugador1 = Jugador(MARGES_ESCENARI, 50, COLOR_JUGADOR1)
jugador2 = Jugador(AMPLA_ESCENARI - MARGES_ESCENARI - 20, 50, COLOR_JUGADOR2)

pilota = Pilota((300, 200), (0, 0, 0))

puntuacio_jugador1 = 0
puntuacio_jugador2 = 0
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

    pilota.pintar(finestraJoc)

    #Parte de la puntuación
    font = pygame.font.Font(None, 36)
    text = font.render(f'Jugador 1: {puntuacio_jugador1} - Jugador 2: {puntuacio_jugador2}', 1, (10, 10, 10))
    finestraJoc.blit(text, (20, 20))

while not gameOver:

    DetectarEvents()
    pilota.moure()

    #Aquí rebota con el techo
    if pilota.posicio[1] <= +50 or pilota.posicio[1] >= 350:
        pilota.rebota_vertical()

    # Aquí la pelota rebote con los jugadores
    if jugador1.colisiona(pilota) or jugador2.colisiona(pilota):
        pilota.rebota_horitzontal()
        pilota.augmenta_velocitat()

    # Aquí resetea cuando la pelota choca con la pared
    if pilota.posicio[0] <= 0 or pilota.posicio[0] >= 600:
        pilota.reset()

    #Condicionales para sumar los puntos (No funciona)
    if pilota.posicio[0] <= 0:
        puntuacio_jugador2 =+ 1

    if pilota.posicio[0] >= 600:
        puntuacio_jugador1 =+ 1
    Pintar()

    rellotge.tick(30)
    pygame.display.update()