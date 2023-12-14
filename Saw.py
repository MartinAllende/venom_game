import pygame
from Config import *
from InvisibleBlock import *

class Saw():
    def __init__(self,x,y,up_down,left_right):
        """funcion encargda de crear las trampas

        Args:
            x (_type_): ubicacion en x
            y (_type_): ubicacion en y
            up_down (_type_): true en caso de que se mueva de abajo para arriba
            left_right (_type_): true en caso de que se mueva de derecha a izquierda
        """
        rescale_images(saw_movement,40,40)
        self.images = saw_movement
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.up_down = up_down
        self.left_right = left_right
        self.index = self.direction = 1
        self.dx = 0
        self.dy = 0

    def update(self, screen, invisible_block_list):
        """funcion encargada del funcionamiento principal de las trampas, su moviemiento y sus animaciones

        Args:
            screen (_type_): pantalla donde se va a mostrar
            invisible_block_list (_type_): lista de los bloques invisibles
        """
        self.dx = 0
        self.dy = 0
        if self.left_right:
            if self.direction == -1:
                self.dx -= 5
            if self.direction == 1:
                self.dx += 5
        if self.up_down:
            if self.direction == -1:
                self.dy -= 5
            if self.direction == 1:
                self.dy += 5

        self.change_direction(invisible_block_list)
        self.animate()

        self.rect.x += self.dx
        self.rect.y += self.dy
        screen.blit(self.image, self.rect)
            
    def animate(self):
        """funcion encargada de cambiar las animaciones correspondientemente
        """
        self.index += 1            
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
            


    def change_direction(self, invisible_block_list):
        """funcion encargada de cambiar la direccion de las trampas

        Args:
            invisible_block_list (_type_): lista de los bloques invisibles
        """
        for block in invisible_block_list:
            if self.left_right:
                if block.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                    self.direction *= -1
            if self.up_down:
                if block.rect.colliderect(self.rect.x , self.rect.y + self.dy , self.width, self.height):
                    self.direction *= -1
                