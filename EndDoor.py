from Config import *
from Meat import *
from Boss import *

class EndDoor():
    def __init__(self,x,y):
        """Funcion encargada de inicializar la puerta de salida

        Args:
            x (_type_): ubicacion en x
            y (_type_): ubicacion en y
        """
        rescale_images(door_images,40,80)
        self.images = door_images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-40
        self.index = 0
        self.counter = 0
        self.open = False

    def update(self,screen,meat_list, boss_list):
        """funcion encargada del funcionamiento principal de la puerta de salida, y de mostrar en pantalla

        Args:
            screen (_type_): pantalla donde se va a mostrar
            meat_list (_type_): lista donde se ecuentran los powerup de carnes
            boss_list (_type_): lista donde se encuentra el boss
        """

        self.check_open(meat_list, boss_list)

        if self.open:
            self.counter += 1
            if self.counter >= 20:
                self.counter = 0
                if self.index < len(self.images)-1:
                    self.index += 1
                    self.image = self.images[self.index]
                elif self.index == len(self.images)-1:
                    self.image = self.images[self.index]

        screen.blit(self.image,self.rect)

    def check_open(self, meat_list, boss_list):
        """funcion encargada de verificar si el jugador cumplio los requisitos
        para que la puerta se pueda abrir

        Args:
            meat_list (_type_): lista donde se ecuentran los powerup de carnes
            boss_list (_type_): lista donde se encuentra el boss
        """
        counter_meats = 0
        counter_picked_meats = 0
        counter_boss = 0
        counter_dead_boss = 0
        for meat in meat_list:
            counter_meats = counter_meats + 1
            if meat.picked:
                counter_picked_meats = counter_picked_meats + 1
        for boss in boss_list:
            counter_boss += 1
            if boss.is_dead:
                counter_dead_boss += 1
        if counter_meats == counter_picked_meats and counter_boss == counter_dead_boss:
            self.open = True