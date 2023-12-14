import pygame

class InvisibleBlock():
    def __init__(self,x,y,tile_size):
        """funcion encargada de inicializar los bloque invisibles delimitadores del movimiento de los 
        enemigos

        Args:
            x (_type_): ubicaion en x
            y (_type_): ubicacion en y
            tile_size (_type_): ancho del cuadrado
        """
        self.rect = pygame.Rect(tile_size,tile_size,tile_size,tile_size)
        self.rect.x = x
        self.rect.y = y