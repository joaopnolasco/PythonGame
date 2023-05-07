import pygame as pg
import random
from rival import Rival
from trofeu import Trofeu
from item import Item, Item2, Item3
from player import Player

import pygame

# Initialize pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trophy Collect: Sport Club edition")

# Set the background image
background_image = pygame.image.load("sportbackground.jpeg").convert()

# Set up the fonts
title_font = pygame.font.SysFont("Times New Roman", 60)
button_font = pygame.font.SysFont("Times New Roman", 40)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Create the "Start Game" button
start_button = pygame.Rect(250, 300, 300, 80)

# Create the "Quit Game" button
quit_button = pygame.Rect(250, 400, 300, 80)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('Warriyo - Mortals (feat. Laura Brehm) [NCS Release].mp3')
pygame.mixer.music.play(-1)
# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos):
                pg.init()

                screen = pg.display.set_mode((800, 600))
                pg.display.set_caption('TROPHY COLLECT: Sport Club Edition')

                background = pg.image.load('ilhaTela.jpg')

                clock = pg.time.Clock()

                # Início da adição da música

                # Fim da adição da música

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

                        for trofeu in trofeus:
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
                        texto_amarelos = fonte.render(f'Foguetes: {player.yellow_items}', True, (255, 255, 0))
                        texto_laranjas = fonte.render(f'Moedas: {player.orange_items}', True, (255, 0, 0))
                        texto_rosas = fonte.render(f'Tartarugas: {player.pink_items}', True, (0, 0, 0))
                        texto_pontuacao = fonte.render(f'Pontuação: {player.trofeu_items}', True, (255, 255, 0))
                        screen.blit(texto_amarelos, (10, 10))
                        screen.blit(texto_laranjas, (10, 50))
                        screen.blit(texto_rosas, (10, 90))
                        screen.blit(texto_pontuacao, (10, 130))

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


                if main() == '_main_':
                    main()
            if quit_button.collidepoint(mouse_pos):
                running = False

    # Draw the background image
    screen.blit(background_image, [0, 0])

    # Draw the title
    title_text = title_font.render("TROPHY COLLECT", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (width // 2, 100)
    screen.blit(title_text, title_rect)

    # Draw the buttons
    pygame.draw.rect(screen, GRAY, start_button, border_radius=10)
    pygame.draw.rect(screen, GRAY, quit_button, border_radius=10)
    pygame.draw.rect(screen, DARK_GRAY, start_button.inflate(-10, -10), border_radius=10)
    pygame.draw.rect(screen, DARK_GRAY, quit_button.inflate(-10, -10), border_radius=10)
    start_gradient = pygame.Surface((300, 80))
    start_gradient.fill((180, 180, 180))
    pygame.draw.rect(start_gradient, (200, 200, 200), (0, 0, 300, 40))
    screen.blit(start_gradient, (250, 300))
    quit_gradient = pygame.Surface((300, 80))
    quit_gradient.fill((180, 180, 180))
    pygame.draw.rect(quit_gradient, (200, 200, 200), (0, 40, 300, 40))
    screen.blit(quit_gradient, (250, 400))
    pygame.draw.rect(screen, BLACK, start_button, 2, border_radius=10)
    pygame.draw.rect(screen, BLACK, quit_button, 2, border_radius=10)

    # Draw the button text
    start_text = button_font.render("Start Game", True, BLACK)
    quit_text = button_font.render("Quit Game", True, BLACK)
    start_text_rect = start_text.get_rect(center=start_button.center)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(start_text, start_text_rect)
    screen.blit(quit_text, quit_text_rect)

    # Update
    pygame.display.update()

# Quit pygame
pygame.quit()
