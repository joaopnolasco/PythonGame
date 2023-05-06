import pygame as pg
import random
from rival import Rival
from trofeu import Trofeu
from item import Item, Item2, Item3
from player import Player

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('TROPHY COLLECT : Sport Clube Edition')

background = pg.image.load('ilhaTela.jpg')


clock = pg.time.Clock()

def main():
    done = False
    time_remaining = 300

    player = Player(screen, 385, 530)

    rivais = [
        Rival(screen, 0, 30, 30, 30, 8),
        Rival(screen, 200, 0, 30, 30, 10),
        Rival(screen, 400, 60, 30, 30, 12),
        Rival(screen, 600, 20, 30, 30, 12)
    ]

    trofeus = [
        Trofeu(screen, 20, 15, 5, 15, 5),
        Trofeu(screen, 150, 5, 20, 15, 1),
        Trofeu(screen, 500, 80, 60, 15, 2)
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

        for rival in rivais:
            rival.move()
            rival.draw()

        for trofeu in trofeus :
            trofeu.move()
            trofeu.draw()

        player.get_item(items)
        player.get_trofeu(trofeus)

        for item in items:
            item.move()
            item.draw()

        player.draw()

        if player.collide(rivais):
            done = True

        fonte = pg.font.Font(None, 36)
        texto_amarelos = fonte.render(f'Velocidade: {player.yellow_items}', True, (255, 255, 0))
        texto_laranjas = fonte.render(f'Moeda: {player.orange_items}', True, (255, 0, 0))
        texto_rosas = fonte.render(f'Timer: {player.pink_items}', True, (0, 0, 0))
        texto_pontuacao = fonte.render(f'Pontuação: {player.trofeu_items}', True, (255, 255, 0))
        screen.blit(texto_amarelos, (10, 50))
        screen.blit(texto_laranjas, (10, 90))
        screen.blit(texto_rosas, (10, 130))
        screen.blit(texto_pontuacao, (10, 170))

        time_remaining -= 1 / 60  # diminui 1 segundo a cada loop
        if time_remaining <= 0:
            done = True  # tempo acabou, o jogo termina

        # exibir o tempo restante na tela
        fonte_timer = pg.font.Font(None, 40)
        texto_timer = fonte_timer.render(f'Tempo: {int(time_remaining)}s', True, (0, 0, 0))
        screen.blit(texto_timer, (600, 10))  # posiciona o timer na tela

        pg.display.update()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    main()
