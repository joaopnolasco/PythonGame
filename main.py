import pygame as pg
import random
from carro import Carro
from trofeu import Trofeu
from item import Item, Item2, Item3
from player import Player

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Jogo de coletar ')

background = pg.image.load('fundoTela.jpg')


clock = pg.time.Clock()

def main():
    done = False
    time_remaining = 300

    player = Player(screen, 385, 530)

    carros = [
        Carro(screen, 0, 30, 30, 30, 8, 'RED'),
        Carro(screen, 200, 0, 30, 30, 10, 'GREEN'),
        Carro(screen, 400, 60, 30, 30, 12, 'BLUE'),
        Carro(screen, 600, 20, 30, 30, 12, 'BLACK')
    ]

    trofeus = [
        Trofeu(screen, 20, 15, 5, 15, 5, 'BROWN'),
        Trofeu(screen, 150, 5, 20, 15, 1, 'BLACK'),
        Trofeu(screen, 500, 80, 60, 15, 2, 'PURPLE')
    ]

    items = [
        Item(screen, random.randint(0, 800), -40, 20, 20, 3, 'YELLOW'),
        Item2(screen, random.randint(0, 800), -80, 20, 20, 4, 'ORANGE'),
        Item3(screen, random.randint(0, 800), -120, 20, 20, 5, 'PINK'),

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

        for trofeu in trofeus :
            trofeu.move()
            trofeu.draw()

        player.get_item(items)
        player.get_trofeu(trofeus)

        for item in items:
            item.move()
            item.draw()

        player.draw()

        if player.collide(carros):
            done = True

        fonte = pg.font.Font(None, 36)
        texto_itens = fonte.render(f'Itens: {player.score}', True, (255, 255, 255))
        texto_amarelos = fonte.render(f'Foquete: {player.yellow_items}', True, (255, 255, 0))
        texto_laranjas = fonte.render(f'Moeda: {player.orange_items}', True, (255, 165, 0))
        texto_rosas = fonte.render(f'Velocidade: {player.pink_items}', True, (255, 192, 203))
        texto_pontuacao = fonte.render(f'Pontuação: {player.trofeu_items}', True, (255, 0, 0))
        screen.blit(texto_itens, (10, 10))
        screen.blit(texto_amarelos, (10, 50))
        screen.blit(texto_laranjas, (10, 90))
        screen.blit(texto_rosas, (10, 130))
        screen.blit(texto_pontuacao, (10, 170))

        time_remaining -= 1 / 60  # diminui 1 segundo a cada loop
        if time_remaining <= 0:
            done = True  # tempo acabou, o jogo termina

        # exibir o tempo restante na tela
        fonte_timer = pg.font.Font(None, 40)
        texto_timer = fonte_timer.render(f'Tempo: {int(time_remaining)}s', True, (255, 255, 255))
        screen.blit(texto_timer, (600, 10))  # posiciona o timer na tela

        pg.display.update()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    main()
