import pygame
import math
from Config import *

class SpiderManWeb():
    def __init__(self,x,y, angle):
        """funcion encargada de crear el tiro del boss

        Args:
            x (_type_): salida del tiro en el eje x
            y (_type_): salida del tiro en el eje y 
            angle (_type_): angulo del disparo
        """
        self.image = pygame.transform.scale(spiderweb,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)
        self.hit = False
        self.dx = math.cos(self.angle) * 10
        self.dy = -(math.sin(self.angle) * 10)
        self.hit = False

    def update(self, screen, w, h, spiderweb_list):
        """funcion ecargada de generar el movimiento de la bala y mostrarla en pantalla, y 
        la elimina si se va de pantalla o si choca con el jugador

        Args:
            screen (_type_): pantalla donde se ca a mostrar
            w (_type_): ancho de la pantalla
            h (_type_): largo de la pantalla
            spiderweb_list (_type_): lista de los tiros del boss
        """
        
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.hit:
           spiderweb_list.remove(self)
        elif self.rect.top > w or self.rect.bottom < 0 or self.rect.left > h or self.rect.right < 0:
            spiderweb_list.remove(self)
        screen.blit(self.image, self.rect)