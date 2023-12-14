from Config import *
from Button import *

class SettingMenu():
    def __init__(self):
        """Funcion encargada de crear el menu de configuraciones
        """
        self.music_button = Button(500,300, on_button, 40,40)
        self.sound_effects_button = Button(500, 450, on_button, 40,40)
        self.back_button = Button(360,600,return_button)
        self.fount = pygame.font.SysFont("Arial", 40)
        music_text = "Music:"
        sound_effects_text = "Sound effects:"
        self.music_text = self.fount.render(music_text, True, (255,255,255))
        self.music_text_rect = self.music_text.get_rect()
        self.music_text_rect.x , self.music_text_rect.y = 300,300
        self.music_on = True
        self.sound_effects_text = self.fount.render(sound_effects_text, True, (255,255,255))
        self.sound_effects_text_rect = self.sound_effects_text.get_rect()
        self.sound_effects_text_rect.x, self.sound_effects_text_rect.y = 200,450
        self.sound_effects_on = True

    def update(self, screen, click):
        """funcion encargada de mostrar los botones y el texto en el menu de configuraciones, ademas
        de chequear si se dio click en los botones

        Args:
            screen (_type_): pantalla donde se va a mostrar el menu
            click (_type_): posicion del click que dio el jugador


        Returns:
            _type_: true o false en caso de que se haya dado click en el boton de volver o no
        """

        screen.blit(self.music_text, self.music_text_rect)
        screen.blit(self.sound_effects_text,self.sound_effects_text_rect)
        music_button = self.music_button.update(screen,click)
        sound_effects_button = self.sound_effects_button.update(screen,click)
        back_button = self.back_button.update(screen, click)
        
        if music_button == True and self.music_on == True:
            self.music_button.image = pygame.transform.scale(off_button,(40,40))
            self.music_on = False
        elif music_button == True and self.music_on == False:
            self.music_button.image = pygame.transform.scale(on_button,(40,40))
            self.music_on = True

        if sound_effects_button == True and self.sound_effects_on == True:
            self.sound_effects_button.image = pygame.transform.scale(off_button,(40,40))
            self.sound_effects_on = False
        elif sound_effects_button == True and self.sound_effects_on == False:
            self.sound_effects_button.image = pygame.transform.scale(on_button,(40,40))
            self.sound_effects_on = True

        return back_button
    
    def get_music_state(self):
        """funcion encargada de tomar el valor del estado de la musica

        Returns:
            _type_: true o false segun el estado de la musica
        """
        return self.music_on
    
    def get_sound_effects_state(self):
        """funcion encargada de tomar el valor del estado de los efectos de sonido

        Returns:
            _type_: true o false segun el estado de los efectos de sonido
        """
        return self.sound_effects_on

