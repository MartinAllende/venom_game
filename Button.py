import pygame

class Button():
    def __init__(self,x,y,image,w = 80,h = 40):
        """funcion encargada de la inicializacion del objeto boton

        Args:
            x (_type_): ubicacion en x del boton
            y (_type_): ubicacion en y del boton
            image (_type_): imagen del boton
            w (int, optional): ancho del boton. Defaults to 80.
            h (int, optional): alto del boton. Defaults to 40.
        """
        self.image = image
        self.image = pygame.transform.scale(image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen, click):
        """funcion encargada de verificar si se dio click en el boton y de mostrarlo en pantalla

        Args:
            screen (_type_): pantalla donde se mostrar el boton
            click (_type_): ubicacion del click dado

         Returns:
            _type_: True en caso de que se haya dado click encima del boton, False en caso contrario

        """

        aux = False
        if self.rect.collidepoint(click):
            aux = True

        screen.blit(self.image, self.rect)
        return aux
    