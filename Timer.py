import pygame

class Timer():
    def __init__(self, x, y):
        """funcion encargada de crear la imagen el timer

        Args:
            x (_type_): ubicacion en x 
            y (_type_): ubicacione en y
        """
        self.fount = pygame.font.SysFont("Arial", 40)
        self.center = (x,y)
        self.number = 0

    def update(self, screen, time):
        """funcion encargada de actualizar y mostrar el pantalla el tiempo

        Args:
            screen (_type_): pantalla donde se va a mostrar
            time (_type_): tiempo a mostrar
        """
        self.number = time
        self.number = self.number * 0.001
        number_text = f"{(self.number):.0f}"
        self.text = self.fount.render(number_text, True, (255,255,255))
        screen.blit(self.text,self.center)