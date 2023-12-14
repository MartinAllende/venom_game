from Config import *

class FireBalls():
    def __init__(self,x,y):
        """funcion encargada de inicializar las bolas de fuego lanzadas por lo enemigos

        Args:
            x (_type_): ubicacion en x 
            y (_type_): ubicacion en y
        """
        self.image = pygame.transform.scale(fire_ball,(20,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit = False
    
    def update(self, screen, w,h, fireball_list):
        """funcion encargada de la funcionalidad principal de las bolas de fuego, y de eliminarlas
        de memoria segun sea correspondiente, ademas de mostrarlas en pantalla

        Args:
            screen (_type_): pantalla
            w (_type_): ancho de la pantalla
            h (_type_): alto de la pantalla
            fireball_list (_type_): lista de las bolas de fuego
        """
        dy = 5
        self.rect.y += dy
        if self.hit:
            fireball_list.remove(self)
        elif self.rect.top > w:
            fireball_list.remove(self)
        screen.blit(self.image, self.rect)

