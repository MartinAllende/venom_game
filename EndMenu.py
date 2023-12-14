from Button import *
from Config import *

class EndMenu():
    def __init__(self):
        """funcion encargada de inicializar en menu de final de nivel
        """
        self.main_menu_button = Button(360,700,main_menu_button)
        self.fount = pygame.font.SysFont("Arial", 40)
        self.final_points = 0
    
    def update(self, screen, click, points, lives, time):
        """funcion encargada del funcionamiento principal del menu de final, ademas, 
        muestra todo el texto y los botones en pantalla

        Args:
            screen (_type_): pantalla donde se va a mostrar
            click (_type_): ubicacion del click
            points (_type_): puntos logrados por el jugador en el nivel
            lives (_type_): cantidad de vidas del jugador al finalizar el nivel 
            time (_type_): tiempo en el cual termino el nivel

        Returns:
            _type_: True en caso de que se haya dado click en el boton de menu principal, False
            en caso contrario
        """
        self.final_points = points * lives - time
        points_text = f"Your score is: {self.final_points}"
        lives_text = f"Remaining Lives: {lives}"
        time_text = f"You complete the level in {time} segs"

        points_text = self.fount.render(str(points_text), True, (255,255,255))
        points_text_rect = points_text.get_rect()
        points_text_rect.center = (400,200)
        lives_text = self.fount.render(str(lives_text), True, (255,255,255))
        lives_text_rect = lives_text.get_rect()
        lives_text_rect.center = (400,350)
        time_text = self.fount.render(str(time_text), True, (255,255,255))
        time_text_rect = time_text.get_rect()
        time_text_rect.center = (400,500)

        screen.blit(points_text, (points_text_rect))
        screen.blit(lives_text, (lives_text_rect))
        screen.blit(time_text, (time_text_rect))

        go_main_menu = self.main_menu_button.update(screen, click)

        return go_main_menu

    def get_final_points(self):
        """funcion encargada de conseguir los puntos final conseguidor por el jugador

        Returns:
            _type_: puntos conseguidos por el jugador
        """
        return self.final_points