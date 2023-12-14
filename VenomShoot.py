import pygame
import math
from Config import *

class VenomShoot():
    def __init__(self, x, y, angle):
        """funcion encargada de crear un tiro de personaje principal

        Args:
            x (_type_): ubicacion de salida en x
            y (_type_): ubicacion de salida en y
            angle (_type_): angulo del disparo
        """
        self.image = pygame.transform.scale(venom_shoot,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)
        self.hit = False
        self.dx = math.cos(self.angle) * 10
        self.dy = -(math.sin(self.angle) * 10)
        self.hit = False

    def update(self, screen, w, h, venon_bullet_list):
        """funcion encargada de actualizar y crear el movimiento de la bala de venom, si se
        va de pantalla o choca con algun enemigo la elimina

        Args:
            screen (_type_): pantalla donde se va a mostrar
            w (_type_): ancho de la pantalla
            h (_type_): largo de la pantalla
            venon_bullet_list (_type_): lista de los disparos de venom
        """
        
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.hit:
           venon_bullet_list.remove(self)
        elif self.rect.top > w or self.rect.bottom < 0 or self.rect.left > h or self.rect.right < 0:
            venon_bullet_list.remove(self)
        screen.blit(self.image, self.rect)