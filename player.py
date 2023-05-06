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
        self.trofeu_items = 0
        self.vel_normal = 5
        self.vel_foguete = 10
        self.current_vel = self.vel_normal


    def draw(self):
        self.win.blit(imgPersonagem, (self.x, self.y))

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > 0:
            self.x -= self.current_vel
        if keys[pg.K_RIGHT] and self.x < 760:
            self.x += self.current_vel

    def get_item(self, items):
        for item in items:
            if self.x + self.current_vel < item.x + item.largura and self.x + self.current_vel + 30 > item.x:
                if self.y < item.y + item.altura and self.y + 60 > item.y:
                    if item.cor == 'YELLOW':
                        self.yellow_items += 1
                        self.current_vel = self.vel_foguete

                    elif item.cor == 'ORANGE':
                        self.orange_items += 1
                        if self.orange_items % 2 == 0:
                            self.trofeu_items += 5
                    elif item.cor == 'PINK':
                        self.pink_items += 1
                    self.score += 1




                    item.x = random.randint(0, 800)
                    item.y = -item.altura

    def collide(self, rivais):
        for rival in rivais:
            if self.x + self.vel < rival.x + rival.largura and self.x + self.vel + 30 > rival.x:
                if self.y < rival.y + rival.altura and self.y + 60 > rival.y:
                    return True
        return False

    def get_trofeu(self, trofeus):
        for trofeu in trofeus:
            if self.x + self.vel < trofeu.x + trofeu.largura and self.x + self.vel + 30 > trofeu.x:
                if self.y < trofeu.y + trofeu.altura and self.y + 60 > trofeu.y:
                    self.trofeu_items += 1
                    self.score += trofeu.pontuacao
                    trofeu.x = random.randint(0, 800)
                    trofeu.y = -trofeu.altura
