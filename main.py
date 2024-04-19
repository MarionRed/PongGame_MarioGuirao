import sys

import pygame

pygame.init()
finestraJoc = pygame.display.set_mode(600, 400)
rellotge = pygame.time.Clock()

gameOver = False

def DetectarEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def Pintar():
    pygame.draw.rect(finestraJoc, ())

while not gameOver:

    DetectarEvents()
    Pintar()

    rellotge.tick(30)
    pygame.display.update()
