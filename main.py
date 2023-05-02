import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Collect Items')

background = pg.image.load('backgroundp1.jpg')
imgPersonagem = pg.image.load("cestateste.png")
imgInimigo = pg.image.load("bomba.png")
imgItem1 = pg.image.load("rocket.png")
#imgItem2 = pg.image.load("star.png")
#imgItem3 = pg.image.load("relogiobom.png")
#imgItem4 = pg.image.load("relógioruim.png")

clock = pg.time.Clock()


class Carro:
    def __init__(self, win, x, y, largura, altura, vel, cor):
        self.win = win
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel
        self.cor = cor

    def draw(self):
        self.win.blit(imgInimigo, (self.x, self.y))

    def move(self):
        self.y += self.vel
        if self.y > 600:
            self.x = random.randint(0, 800)
            self.y = -self.altura


class Item:
    def __init__(self, win, x, y, largura, altura, vel, cor):
        self.win = win
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel
        self.cor = cor
        self.collected = False

    def draw(self):
        self.win.blit(imgItem1, (self.x, self.y))

    def move(self):
        self.y += self.vel
        if self.y > 600:
            self.x = random.randint(0, 800)
            self.y = -self.altura
            self.collected = False


class Player:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.largura = 30
        self.altura = 20
        self.vel = 5
        self.cor = 'CYAN'
        self.score = 0
        self.yellow_items = 0
        self.orange_items = 0
        self.pink_items = 0

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.x -= self.vel
        if keys[pg.K_d]:
            self.x += self.vel

        # Verifica se o jogador está dentro dos limites da tela
        if self.x < 0:
            self.x = 0
        elif self.x > 800 - self.largura:
            self.x = 800 - self.largura
        if self.y < 0:
            self.y = 0
        elif self.y > 600 - self.altura:
            self.y = 600 - self.altura

    def draw(self):
        self.win.blit(imgPersonagem, (self.x, self.y))

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.largura, self.altura)

    def get_item(self, items):
        for item in items:
            if not item.collected and self.get_rect().colliderect(pg.Rect(item.x, item.y, item.largura, item.altura)):
                item.collected = True
                if item.cor == 'YELLOW':
                    self.yellow_items += 1
                elif item.cor == 'ORANGE':
                    self.orange_items += 1
                elif item.cor == 'PINK':
                    self.pink_items += 1
                self.score += 1




def main():
    done = False

    player = Player(screen, 385, 530)

    carros = [
        Carro(screen, 0, 30, 30, 30, 4, 'RED'),
        Carro(screen, 200, 0, 30, 30, 2, 'GREEN'),
        Carro(screen, 400, 60, 30, 30, 3, 'BLUE')
    ]

    items = [
        Item(screen, random.randint(0, 800), -40, 20, 20, 3, 'YELLOW'),
        Item(screen, random.randint(0, 800), -80, 20, 20, 4, 'ORANGE'),
        Item(screen, random.randint(0, 800), -120, 20, 20, 5, 'PINK'),

    ]

    while not done:
        screen.fill((40, 40, 40))
        screen.blit(background, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True



        player.control()

        for carro in carros:
            carro.move()
            carro.draw()

            if player.get_rect().colliderect(pg.Rect(carro.x, carro.y, carro.largura, carro.altura)):
                done = True

        player.get_item(items)

        for item in items:
            item.move()
            item.draw()

        player.draw()

        fonte = pg.font.Font(None, 36)
        texto_itens = fonte.render(f'Itens: {player.score}', True, (255, 255, 255))
        texto_amarelos = fonte.render(f'Amarelos: {player.yellow_items}', True, (255, 255, 0))
        texto_laranjas = fonte.render(f'Laranjas: {player.orange_items}', True, (255, 165, 0))
        texto_rosas = fonte.render(f'Rosas: {player.pink_items}', True, (255, 192, 203))
        screen.blit(texto_itens, (10, 10))
        screen.blit(texto_amarelos, (10, 50))
        screen.blit(texto_laranjas, (10, 90))
        screen.blit(texto_rosas, (10, 130))

        pg.display.update()
        clock.tick(60)

    pg.quit()


if __name__ == '__main__':
    main()
