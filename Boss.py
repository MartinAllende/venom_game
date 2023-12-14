import random
import math
from Config import *
from SpiderManWeb import *

class Boss():
    def __init__(self, x, y):
        """Inicializacion del boss en la cual se establecen las imagenes de las animaciones, se crea el rectangulo
        perteneciente al mismo y se lo ubica en una direccion x,y

        Args:
            x (_type_): recibe la ubicacioen en x del boss
            y (_type_): recibe la ubicacioen en y del boss
        """
        rescale_images(spiderman_left, 80,40)
        rescale_images(spiderman_right, 80,40)
        rescale_images(spiderman_up, 40,80)
        rescale_images(spiderman_down, 40,80)

        self.images_left = spiderman_left
        self.images_right = spiderman_right
        self.images_down = spiderman_down
        self.images_up = spiderman_up
        self.image_death = spiderman_death
        self.image_death = pygame.transform.scale(self.image_death,(80,20))

        self.image = self.images_down[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.index = 0
        self.counter = 0
        self.vel_y = 0

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.dx = 0
        self.dy = 0
        self.walk_cooldown = 0
        self.directon_cooldown = 0
        self.direction_counter = 0
        self.direction = 1
        self.shot_cooldown = 50
        self.shot_cooldown_counter = 0
        self.hp = 50
        self.is_dead = False

    def update(self,screen,world,w,h, venom_bullets_list, spider_web_list, player, sound_effects):
        """Encargada del funcionamiento general del boss, se encarga de llamar a todas las funciones
        que hacen al boss ,se encarga del movimiento y de mostrarlo en pantalla

        Args:
            screen (_type_): pantalla donde se va a mostrar
            world (_type_): objero de tipo World donde se encuentra la infomacion del mundo
            w (_type_): ancho de la pantalla
            h (_type_): largo de la pantalla
            venom_bullets_list (_type_): lista donde se encuentran los disparos de venom
            spider_web_list (_type_): lista donde se encuentran los disparos del boss
            player (_type_): objeto donde se encuentra la infomacion del jugador
            sound_effects (_type_): el estado de los efectos de sonido
        """
        self.dx = 0
        self.dy = 0
        self.walk_cooldown = 3
        self.direction_counter += 1
        self.directon_cooldown = 100
        self.shot_cooldown_counter += 1

        if self.is_dead == False:

            if self.direction == 1:
                self.dy += 2
                self.counter += 1
            if self.direction == 2:
                self.dy -= 2
                self.counter += 1
            if self.direction == 3:
                self.dx -= 2
                self.counter += 1
            if self.direction == 4:
                self.dx += 2
                self.counter += 1

            self.verify_death(player)
            self.collision_venom_bullets(venom_bullets_list, sound_effects)
            if self.shot_cooldown_counter > self.shot_cooldown:
                self.shot_cooldown_counter = 0
                self.shot_spiderweb(spider_web_list, player, sound_effects)
            self.change_direction(w,h)

        else:

            x = self.rect.x
            y = self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y 
            self.gravity()
            self.check_platforms_collide(world)

        self.animate()

        self.rect.x += self.dx
        self.rect.y += self.dy
        screen.blit(self.image, self.rect)

    def gravity(self):
        """funcion encargada de generar la gravedad
        """
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y

    def check_platforms_collide(self, world):
        """funcion encargada de verificar si se choca con alguna plataforma, en caso de hacerlo estaba la posicion
        arriba de la misma

        Args:
            world (_type_): objeto donde se encuntra la informacion del mundo
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

    def animate(self):
        """funcion encargada de gestionar que animacion y en que momentos va a mostrar el boss
        """

        if self.is_dead == False:
            if self.counter > self.walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.direction == 1:
                    if self.index >= len(self.images_down):
                        self.index = 0
                    self.image = self.images_down[self.index]
                if self.direction == 2:
                    if self.index >= len(self.images_up):
                        self.index = 0
                    self.image = self.images_up[self.index]
                if self.direction == 3:
                    if self.index >= len(self.images_left):
                        self.index = 0
                    self.image = self.images_left[self.index]
                if self.direction == 4:
                    if self.index >= len(self.images_right):
                        self.index = 0
                    self.image = self.images_right[self.index]

        else:
            self.image = self.image_death

    def collision_venom_bullets(self, venom_bullets_list, sound_effects):
        """funcion encargada de verificar si el boss recibe el impacto de alguna bala de venom

        Args:
            venom_bullets_list (_type_): lista donde estan las balas disparadas por venom
            sound_effects (_type_): estado de los efectos de sonido
        """

        for bullet in venom_bullets_list:

            if bullet.rect.colliderect(self.rect):
                self.hp -= 10
                venom_bullets_list.remove(bullet)
                if sound_effects:
                    sound = pygame.mixer.Sound(venom_shoot_hit)
                    sound.set_volume(0.2)
                    sound.play()

    def verify_death(self, player):
        """Funcion encargada de verificar si el boss perdio toda su vida, en caso de estar muerto,
        le suma puntos al jugador

        Args:
            player (_type_): informacion del jugador
        """

        if self.hp <= 0:
            player.points += 100
            self.is_dead = True
                
    def change_direction(self, w, h):
        """funcion encargada de cambiar la direccion del boss aleatoriamente

        Args:
            w (_type_): ancho de la pantalla
            h (_type_): largo de la pantalla
        """

        if self.direction_counter > self.directon_cooldown:
            self.direction_counter = 0
            self.direction = random.randint(1,4)

        if self.rect.top + self.dy*2 < 0:
            self.direction = 1
            self.dy = 0
            
        if self.rect.bottom + self.dy*2 >= h - 200:
            self.direction = 2
            self.dy = 0

        if self.rect.right + self.dx*2 > w:
            self.direction = 3 
            self.dx = 0

        if self.rect.left + self.dx*2 < 0:
            self.direction = 4 
            self.dx = 0

    def shot_spiderweb(self, spiderweb_list, player, sound_effects):
        """funcion encargada de hacer que el boss dispare

        Args:
            spiderweb_list (_type_): lista donde se encuentran los disparos del boss
            player (_type_): objeto con infomacion del jugador
            sound_effects (_type_): estado de los efectos de sonido
        """
        pos = player.rect.center
        x_dist = pos[0] - self.rect.center[0]
        y_dist = -(pos[1] - self.rect.center[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        aux = SpiderManWeb(*self.rect.center,self.angle)
        spiderweb_list.append(aux)
        if sound_effects:
            sound = pygame.mixer.Sound(spiderman_shot_sound)
            sound.set_volume(0.2)
            sound.play()
        