from Button import *
from Config import *

class MainMenu():
    def __init__(self):
        """funcion encargada de crear el menu principal
        """
        self.star_button = Button(360,300,play_button)
        self.setting_button = Button(360,400,setting_button)
        self.leaderboard_button = Button(380,500,leaderboard_button,40,40)
        self.extreme_mode_button = Button(550,610, off_button, 40,40)
        self.fount = pygame.font.SysFont("Arial", 40)
        extreme_mode_text = "Extreme mode:"
        self.extreme_mode_text = self.fount.render(extreme_mode_text, True, (255,255,255))
        self.extreme_mode_text_rect = self.extreme_mode_text.get_rect()
        self.extreme_mode_text_rect.x , self.extreme_mode_text_rect.y = 250,600
        self.extreme_mode = False

    def update(self, screen, click):
        """funcion encargada de checkear en que boton dio click, y mostrar
        los mismo en pantalla

        Args:
            screen (_type_): pantalla donde se va a mostrar
            click (_type_): ubicacion del click dado por el usuario

        Returns:
            _type_: 1 en caso de que se haya dado click en boton start, 2 en caso
            de que se haya dado click en boton settings, 3 en caso de que se haya
            dado click en el boton de leaderboard, 0 en caso de que no se haya
            dado click en ningun boton
        """

        screen.blit(pygame.transform.scale(background_image, (800, 800)), (0,0))
        screen.blit(self.extreme_mode_text, self.extreme_mode_text_rect)
        extreme_mode_button = self.extreme_mode_button.update(screen, click)
        aux_start = self.star_button.update(screen, click)
        aux_settings = self.setting_button.update(screen,click)
        aux_leaderboard =  self.leaderboard_button.update(screen,click)

        if extreme_mode_button == True and self.extreme_mode == True:
            self.extreme_mode_button.image = pygame.transform.scale(off_button,(40,40))
            self.extreme_mode = False
        elif extreme_mode_button == True and self.extreme_mode == False:
            self.extreme_mode_button.image = pygame.transform.scale(on_button,(40,40))
            self.extreme_mode = True

        
        if aux_start:
            aux = 1
        elif aux_settings:
            aux = 2
        elif aux_leaderboard:
            aux = 3
        else:
            aux = 0

        return aux
    
    def get_extreme_mode(self):
        """funcion encargada de tomar el valor del modo extremo

        Returns:
            _type_: true o false segun el estado del modo extremo
        """
        return self.extreme_mode