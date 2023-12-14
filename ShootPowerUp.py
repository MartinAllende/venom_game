import pygame
from Config import *

class ShootPowerUp():
    def __init__(self,x,y):
        """funcion encargada de crear el power up de disparo

        Args:
            x (_type_): ubicacion en x 
            y (_type_): ubicacion en y
        """
        self.image = venom_shoot
        self.image = pygame.transform.scale(venom_shoot,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.picked = False

    def update(self, screen, power_up_list):
        """funcion encargada de verificar si se agarro el power up en caso positivos lo elimina, 
        sino lo muestra en la pantalla

        Args:
            screen (_type_): pantalla donde se va a mostrar
            power_up_list (_type_): lista de los power up de disparo
        """
        if self.picked:
            power_up_list.remove(self)
        else:
            screen.blit(self.image, self.rect)