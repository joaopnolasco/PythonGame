import pygame

#inicia o pygame
pygame.init()

#Cria a tela do jogo
tela = pygame.display.set_mode((800, 600))

#Título e ícone do jogo
pygame.display.set_caption("Nome jogo")
#icon = pygame.image.load("iconejogo.png")

jogo_rodando = True
while jogo_rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_rodando == False
