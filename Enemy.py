import pygame
from Config import *
from FireBalls import *

class Enemy():
    def __init__(self,x,y,can_shoot,can_move,can_fly):
        """funcion encargada de inicializar a los enemigos, y de setear sus animaciones correspondientemente

        Args:
            x (_type_): ubicacion en x
            y (_type_): ubicacion en y
            can_shoot (_type_): puede disparar , True en caso positivo, False en caso contrario
            can_move (_type_): puede moverse en el terreno , True en caso positivo, False en caso contrario
            can_fly (_type_): puede volar , True en caso positivo, False en caso contrario
        """

        if can_move:
            rescale_images(enemy_right_walk,40,40)
            self.images_enemy_right = enemy_right_walk
            rescale_images(enemy_left_walk,40,40)
            self.images_enemy_left = enemy_left_walk
        if can_fly:
            rescale_images(enemy_right_fly,80,50)
            self.images_enemy_right = enemy_right_fly
            rescale_images(enemy_left_fly,80,50)
            self.images_enemy_left = enemy_left_fly
        self.image_enemy = self.images_enemy_left[0]
        self.can_shoot = can_shoot
        self.can_move = can_move
        self.can_fly = can_fly
        self.index = 0
        self.counter = 0
        self.vel_y = 0
        self.image_enemy = pygame.transform.scale(self.images_enemy_right[self.index],(40,40))
        self.width = self.image_enemy.get_width()
        self.height = self.image_enemy.get_height()
        self.rect = self.image_enemy.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0
        self.walk_cooldown = 0
        self.direction = -1
        self.is_dead = False
        
    def update(self,screen,world,w,h,invisible_block_list, enemy_list, time, fireball_list):
        """Funcion encargada del funcionamiento principal de los enemigos segun sus capacidades, ademas,
        regula las acciones de cada enemigo, y los muestra en pantalla

        Args:
            screen (_type_): pantalla donde se va a mostrar
            world (_type_): objeto con la infomacion del mundo
            w (_type_): ancho de la pantalla
            h (_type_): largo de la pantalla
            invisible_block_list (_type_): lista de los bloques invisibles
            enemy_list (_type_): lista donde se encuentran todos los enemigos
            time (_type_): tiempo con el cual se regularan los disparos
            fireball_list (_type_): lista donde se encuentran las bolas de fuego lanzadas
        """
        self.dx = 0
        self.dy = 0
        self.walk_cooldown = 3

        if self.is_dead == False:
            if self.direction == -1:
                self.dx -= 1
                self.counter += 1
            if self.direction == 1:
                self.dx += 1
                self.counter += 1
            
            if self.can_fly:
                self.fly(w)
                self.throw_fireball(time, enemy_list, fireball_list)
                self.animate()

            if self.can_move:
                self.gravity()
                self.check_platforms_collide(world,w,h)
                self.change_direction(invisible_block_list)
                self.animate()
        else:
            self.dy = 11
            if self.rect.top > w:
                enemy_list.remove(self)

        self.rect.x += self.dx
        self.rect.y += self.dy
        screen.blit(self.image_enemy, self.rect)

    def gravity(self):
        """funcion encargada de la gravedad de los enemigos
        """
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y

    def check_platforms_collide(self, world, w, h):
        """funcion encargada de verificar las colisiones de los enemigos con las plataformas, 
        si se choca los ubica encima de las mismas

        Args:
            world (_type_): objeto con infomacion del mundo
            w (_type_): ancho de la pantalla
            h (_type_): largo de la pantalla
        """
        for tile in  world.tile_list:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if self.vel_y < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                    
                elif self.vel_y >= 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.jumped = False

        # self.rect.x += self.dx
        # self.rect.y += self.dy

    def animate(self):
        """funcion encargada de regular las animaciones de los enemigos
        """
        if self.counter > self.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.direction == 1:
                if self.index >= len(self.images_enemy_right):
                    self.index = 0
                self.image_enemy = self.images_enemy_right[self.index]
            if self.direction == -1:
                if self.index >= len(self.images_enemy_left):
                    self.index = 0
                self.image_enemy = self.images_enemy_left[self.index]

    def change_direction(self, invisible_block_list):
        """funcion encargada de cambiar la direccion de los enemigos que caminan cuando se van a salir
        de la plataforma

        Args:
            invisible_block_list (_type_): lista de los bloques invisibles
        """
        for block in invisible_block_list:
            # if block.rect.colliderect(self.rect):
            #     self.dx += 1
            if block.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.direction *= -1
            

    def fly(self,w):
        """funcion encargada del movimiento de los enemigos voladores

        Args:
            w (_type_): ancho de la pantalla
        """
        if self.rect.right + self.dx >= w:
            self.direction = -1
        if self.rect.left + self.dx <= 0:
            self.direction = 1

    def throw_fireball(self, time, enemy_list, fireball_list):
        """funcion encargada de hacer disparar a los enemigos que vuelan

        Args:
            time (_type_): tiempo transcurrido desde el ultimo disparo
            enemy_list (_type_): lista de enemigos
            fireball_list (_type_): lista de las bolas de fuego
        """
        if time % 100 == 0:
                fireball = FireBalls(*self.rect.center)
                fireball_list.append(fireball)
            
    
