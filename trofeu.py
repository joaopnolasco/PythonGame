import pygame as pg
import random

imgTrofeu = pg.image.load("trophy.png")

class Trofeu:
    def __init__(self, win, x, y, largura, altura, vel):
        self.win = win
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel
        self.pontuacao = 0

    def draw(self):
        self.win.blit(imgTrofeu, (self.x, self.y))

    def move(self):
        self.y += self.vel
        if self.y > 600:
            self.x = random.randint(0, 800)
            self.y = -self.altura
