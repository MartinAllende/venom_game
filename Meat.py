from Config import *

class Meat():
    def __init__(self,x,y):
        """funcion encargada de crear los power up de carnes

        Args:
            x (_type_): ubicacion en x
            y (_type_): ubicacion en y
        """
        self.image = meat
        self.image = pygame.transform.scale(meat,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.picked = False

    def update(self, screen, number):
        """funcion encargada de mostrar lass carnes en pantalla y se pasarlas arriba a al izquierad en caso
        de ser agarradas

        Args:
            screen (_type_): pantalla donde se va a mostrar
            number (_type_): numero de carne correspondiente
        """
        if self.picked:
            self.rect.x = 30 * number
            self.rect.y = 10
        screen.blit(self.image, self.rect)