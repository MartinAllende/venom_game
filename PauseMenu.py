from Button import *
from Config import *

class PauseMenu():
    def __init__(self):
        """funcion encargada de crear el menu de pausa
        """
        self.resume_button = Button(360,380,resume_button)
        self.quit_button = Button(360,450,quit_button)

    def update(self, screen, click):
        """funcion encargada de mostrar la pausa y de verificar si se dio click en algun boton

        Args:
            screen (_type_): pantalla donde se mostrara la pausa
            click (_type_): ubicacion del click dado por usuario

        Returns:
            _type_: 1 en caso de que se haya dado click en el boton continuar, 2 en caso de 
            que se haya dado click en el boton de salir, 0 en caso de que no se haya dado
            click en ningun boton
        """
        resume_lvl = self.resume_button.update(screen, click)
        quit_button = self.quit_button.update(screen,click)

        if resume_lvl:
            aux = 1
        elif quit_button:
            aux = 2
        else:
            aux = 0

        return aux
