# Pilota.py

import random

import pygame

class Pilota:
    velocitat = 5
    mida = 10

    def __init__(self, posicio_inicial, color):
        self.posicio = list(posicio_inicial)
        self.color = color
        self.velocitat_x = 0
        self.velocitat_y = 0
        self.reset()

    def reset(self):
        self.posicio[0] = 300
        self.posicio[1] = 200
        self.velocitat_x = random.choice([-1, 1]) * self.velocitat
        self.velocitat_y = random.choice([-1, 1]) * self.velocitat

    def moure(self):
        self.posicio[0] += self.velocitat_x
        self.posicio[1] += self.velocitat_y

    def rebota_vertical(self):
        self.velocitat_y *= -1

    def rebota_horitzontal(self):
        self.velocitat_x *= -1

    def augmenta_velocitat(self):
        self.velocitat += 0#

    def pintar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (int(self.posicio[0]), int(self.posicio[1])), self.mida)