import pygame as pg
import random

imgPersonagem = pg.image.load("cestateste.png")

class Player:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.vel = 0
        self.score = 0
        self.yellow_items = 0
        self.orange_items = 0
        self.pink_items = 0

    def draw(self):
        self.win.blit(imgPersonagem, (self.x, self.y))

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > 0:
            self.x -= 5
        if keys[pg.K_RIGHT] and self.x < 760:
            self.x += 5

    def get_item(self, items):
        for item in items:
            if self.x + self.vel < item.x + item.largura and self.x + self.vel + 30 > item.x:
                if self.y < item.y + item.altura and self.y + 60 > item.y:
                    if item.cor == 'YELLOW':
                        self.yellow_items += 1
                    elif item.cor == 'ORANGE':
                        self.orange_items += 1
                    elif item.cor == 'PINK':
                        self.pink_items += 1
                    self.score += 1
                    item.x = random.randint(0, 800)
                    item.y = -item.altura

    def collide(self, carros):
        for carro in carros:
            if self.x + self.vel < carro.x + carro.largura and self.x + self.vel + 30 > carro.x:
                if self.y < carro.y + carro.altura and self.y + 60 > carro.y:
                    return True
        return False
