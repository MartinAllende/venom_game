from ButtonLevel import *
from Config import*

class LevelSelector():
    def __init__(self, world_data, points_list):
        """funcion encargada de crear la interfaz de seleccion de nivel

        Args:
            world_data (_type_): informacion de los niveles
            points_list (_type_): lista de los puntos del jugador conseguidos en cada nivel
        """
        x = 20
        y = 40

        self.lvl_disponibility = 0
        for list in points_list:
            for point in list:
                if int(point) > 0:
                    self.lvl_disponibility += 1
                    break

        self.level_buttons = []
        self.bloqued_buttons = []

        for level in range(self.lvl_disponibility+1):
            aux = ButtonLevel(x,y,pygame.image.load(rf"imagenes\numbers\{level+1}.png"),level+1)
            if level + 1 <= len(world_data):
                self.level_buttons.append(aux)
                x += 100
                if x > 700:
                    x = 20
                    y += 100
        
        for level in range(len(world_data)):

            if level+1 <= self.lvl_disponibility+1:
                pass
            else:
                aux = ButtonLevel(x,y,pygame.image.load(rf"imagenes\locked.jpg"),level+1)
                self.bloqued_buttons.append(aux)
                x += 100
                if x > 700:
                    x = 20
                    y += 100


        self.return_button = Button(700,750, return_button)

            

            
            