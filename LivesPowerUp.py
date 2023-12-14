import pygame
from Config import *

class LivesPowerUp():
    def __init__(self,x,y):
        """funcion encargada de crear los power up que otorgan vidas extras

        Args:
            x (_type_): ubicacion en x
            y (_type_): ubicacion en y
        """
        self.image = live
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.picked = False

    def update(self, screen, power_up_list):
        """funcion encargada de mostrar los powerup en pantalla en caso de no haber sido agarrados,
        si son agarrados los elimina

        Args:
            screen (_type_):patanlla donde se mostraran 
            power_up_list (_type_): lista de los powerup de vida
        """
        if self.picked:
            power_up_list.remove(self)
        else:
            screen.blit(self.image, self.rect)