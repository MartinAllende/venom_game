from Button import *
from Config import *

class LeaderBoard():
    def __init__(self, points_list, level):
        """funcion encargada de crear la lista de los mejores puntajes

        Args:
            points_list (_type_): lista donde se encuentran los puntos, jugadores y niveles
            level (_type_): nivel del cual creremos la lista de mejores puntajes
        """
        
        self.menu_button = Button(360, 750, main_menu_button)
        self.back_button = Button(50,750,back_button,40,40)
        self.next_button = Button(750,750, next_button,40,40)
        self.fount = pygame.font.SysFont("Arial", 40)
        counter = 1
        self.points_list = []
        self.points_rect_list = []

        self.caption = f"Best Points in level {level}"
        self.caption = self.fount.render(str(self.caption), True, (255,255,255))
        self.caption_rect = self.caption.get_rect()
        self.caption_rect.center = 400, 100

        for player in points_list:
            text = f"{counter}. {player[1]} - {player[0]}"
            text = self.fount.render(str(text), True, (255,255,255))
            self.points_list.append(text)
            counter += 1
        
        x,y=400,200
        for text in self.points_list:
            text_rect = text.get_rect()
            text_rect.center = x,y
            self.points_rect_list.append(text_rect)

            if y < 600:
                y += 100
            else:
                break
            
    def update(self, screen, click):
        """funcion encargada de mostrar los botones en pantalla, ademas de la lista

        Args:
            screen (_type_): pantalla donde se va a mostrar todo
            click (_type_): ubicaion del click

        Returns:
            _type_: 1 en caso de que se haya dado click en el boton del menu, 2 en caso de que se haya dado
            click en el boton de back, 3 en caso de que se haya dado click en el boton de next,
            0 en caso de que no se haya dado click sobre ningun boton
        """

        aux_menu = self.menu_button.update(screen, click)
        aux_back = self.back_button.update(screen, click)
        aux_next = self.next_button.update(screen, click)

        screen.blit(self.caption, self.caption_rect)

        for i in range(len(self.points_rect_list)):
            screen.blit(self.points_list[i], self.points_rect_list[i])

        if aux_menu:
            aux = 1
        elif aux_back:
            aux = 2
        elif aux_next:
            aux = 3
        else:
            aux = 0

        return aux