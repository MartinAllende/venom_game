from Button import *

class ButtonLevel(Button):
    def __init__(self,x,y,image,number):
        """inicializacion del tipo de boton que representa los niveles

        Args:
            x (_type_): ubicacion del boton en x
            y (_type_): ubicacion del boton en y
            image (_type_): imagen del boton
            number (_type_): numero ligado al boton
        """
        super().__init__(x,y,image)
        self.number = number
        self.image = pygame.transform.scale(image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen,click):
        """funcion encargada de verificar si se dio click en el boton y de mostrarlo en pantalla

        Args:
            screen (_type_): pantalla donde se mostrar el boton
            click (_type_): ubicacion del click dado

        Returns:
            _type_: True en caso de que se haya dado click encima del boton, False en caso contrario
        """
        aux = super().update(screen, click)
        return aux