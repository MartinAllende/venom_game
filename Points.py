import pygame

class Points():
    def __init__(self, x, y):
        """funcion encargada de crear el contador de puntos de la pantalla

        Args:
            x (_type_): ubicacion en x
            y (_type_): ubicacion en y
        """
        self.fount = pygame.font.SysFont("Arial", 40)
        self.center = (x,y)
        self.number = 0

    def update(self, screen, points):
        """funcion encargada de mostra el contado de puntos en pantalla y actualizarlo

        Args:
            screen (_type_): pantalla donde se va a mostrar
            points (_type_): puntos a mostrar
        """
        self.number = points
        self.text = self.fount.render(str(self.number), True, (255,255,255))
        screen.blit(self.text,self.center)