# Jugador.py
import pygame
from constant import MARGES_ESCENARI, COLOR_JUGADOR1, AMPLA_ESCENARI, COLOR_JUGADOR2

class Jugador:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.ancho = 20
        self.alto = 100
        self.velocitat = 5

    def pintar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.posX, self.posY, self.ancho, self.alto))
    def colisiona(self, pilota):
        # Verificar si la posición de la pelota está dentro de los límites del jugador
        if (self.posX < pilota.posicio[0] < self.posX + self.ancho and
                self.posY < pilota.posicio[1] < self.posY + self.alto):
            return True
        return False