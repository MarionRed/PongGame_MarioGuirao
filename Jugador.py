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

    def pintar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.posX, self.posY, self.ancho, self.alto))