import pygame
import unicodedata
from Button import *
from Config import *
from pygame.locals import *

class TextBox():
    def __init__(self):
        """funcion encargada de crear un cuadro de texto para ingresar el nombre del jugador
        """
        self.fount = pygame.font.SysFont("Arial", 40)
        self.text = ""
        self.text_box_rect = pygame.Rect(150,350,500,100)
        self.text_box_rect.x = 150
        self.text_box_rect.y = 350
        self.load_button = Button(360,600,load_button)

    def update(self, screen, click, event_list):
        """funcion encargada de actualizar el cuadro de texto cuando se ingresa una letra
        y mostrarlo en pantalla

        Args:
            screen (_type_): pantalla donde se va a mostrar
            click (_type_): posicion del click del jugador
            event_list (_type_): lista de los eventos

        Returns:
            _type_: true en caso de que se clickee en el boton load o false en caso contrario
        """
        self.take_letter(event_list)
        text_image = self.fount.render(self.text, True,(255,255,255))
        text_image_rect = text_image.get_rect()
        text_image_rect.center = self.text_box_rect.center
        aux = self.load_button.update(screen,click)
        pygame.draw.rect(screen, (0,0,0), self.text_box_rect)
        screen.blit(text_image, text_image_rect)

        return aux

    def take_letter(self, event_list):
        """funcio encargada de tomar las letras ingresadas por el usuario y ponerla en el texto

        Args:
            event_list (_type_): lista de los eventos
        """
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                caracter = event.unicode
                if event.key == pygame.K_BACKSPACE:
                   self.text = self.text[:-1]
                elif len(caracter) == 1 and unicodedata.category(caracter)[0] != 'C' and len(self.text) <= 15:
                    self.text += caracter
    
    def get_text(self):
        """funcio encargada de tomar el texto final escrito en el cuadro

        Returns:
            _type_: nombre escrito en el cuadro
        """
        return self.text