import pygame as pg

#Define as cores
coresRGB = {

    "preto": (0, 0, 0),
    "branco": (255, 255, 255),
    "azul": (0, 0, 255),
    "vermelho": (255, 0, 0)

}


#Cria o Labirinto
class Labirinto:
    def __init__(self, image, mascara, tela) -> None:
        self.piso = pg.sprite.Sprite()
        self.piso.image = pg.transform.scale(image, (800, 700))
        self.piso.rect = self.piso.image.get_rect()
        self.parede = pg.sprite.Sprite()
        self.parede.image = pg.transform.scale(mascara, (800, 700))
        self.parede.rect = self.parede.image.get_rect()
        self.tela = tela

    def desenhar_labirinto(self):
        self.tela.blit(self.piso.image, self.piso.rect)
        self.tela.blit(self.parede.image, self.parede.rect)
