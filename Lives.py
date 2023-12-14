import pygame
from Config import *

class Lives():
    def __init__(self,x,y):
        """funcion encargada de crear las vidas del jugador

        Args:
            x (_type_): ubicacion en x  
            y (_type_): ubicaion en y
        """
        self.image = pygame.transform.scale(live,(40,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.used = False

    def update(self, screen):
        """funcion encargada de mostrar la vida arriba a la derecha en caso de que no haya sido usada

        Args:
            screen (_type_): pantalla donde se van a mostrar
        """
        if self.used == False:
            screen.blit(self.image,self.rect)