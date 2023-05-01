import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((610, 480))
pg.display.set_caption('Collect Items')



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
        pg.draw.rect(self.win, self.cor, (self.x, self.y, self.largura, self.altura))

    def move(self):
        self.y += self.vel
        if self.y > 480:
            self.x = random.randint(0, 610)
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

    def draw(self):
        pg.draw.rect(self.win, self.cor, (self.x, self.y, self.largura, self.altura))

    def move(self):
        self.y += self.vel
        if self.y > 480:
            self.x = random.randint(0, 610)
            self.y = -self.altura


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

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.x -= self.vel
        if keys[pg.K_d]:
            self.x += self.vel

        # Verifica se o jogador está dentro dos limites da tela
        if self.x < 0:
            self.x = 0
        elif self.x > 610 - self.largura:
            self.x = 610 - self.largura
        if self.y < 0:
            self.y = 0
        elif self.y > 480 - self.altura:
            self.y = 480 - self.altura

    def draw(self):
        pg.draw.rect(self.win, self.cor, (self.x, self.y, self.largura, self.altura))

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.largura, self.altura)

    def get_item(self, items):
        for item in items:
            if self.get_rect().colliderect(pg.Rect(item.x, item.y, item.largura, item.altura)):
                self.score += 1
                items.remove(item)



def main():
    done = False

    player = Player(screen, 305, 450)

    carros = [
        Carro(screen, 0, 30, 30, 30, 4, 'RED'),
        Carro(screen, 200, 0, 30, 30, 2, 'GREEN'),
        Carro(screen, 400, 60, 30, 30, 3, 'BLUE')
    ]

    items = [
        Item(screen, random.randint(0, 610), -40, 20, 20, 3, 'YELLOW'),
        Item(screen, random.randint(0, 610), -80, 20, 20, 4, 'ORANGE'),
        Item(screen, random.randint(0, 610), -120, 20, 20, 5, 'PINK')
    ]

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        player.control()

        screen.fill((40, 40, 40))

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
        texto = fonte.render(f'Itens: {player.score}', True, (255, 255, 255))
        screen.blit(texto, (10, 10))

        pg.display.update()
        clock.tick(60)

    pg.quit()


if __name__ == '__main__':
    main()
