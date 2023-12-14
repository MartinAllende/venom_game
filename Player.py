import pygame
import math
from Config import *
from Enemy import *
from FireBalls import *
from Meat import *
from VenomShoot import *
from ShootPowerUp import *


class Player():
    def __init__(self, x, y):
        """funcion encargada de crear en jugador principal

        Args:
            x (_type_): ubicacion en x
            y (_type_): ubicacion en y
        """

        rescale_images(venom_right,40,80)
        self.images_right = venom_right
        rescale_images(venom_left,40,80)
        self.images_left = venom_left
        rescale_images(venom_jump_right,40,80)
        self.images_jumping_right = venom_jump_right
        rescale_images(venom_jump_left,40,80)
        self.images_jumping_left = venom_jump_left

        self.index = 0
        self.counter = 0
        self.image = pygame.transform.scale(self.images_right[self.index],(40,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        y = y-50
        self.spawn = (x,y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.dx = 0
        self.dy = 0
        self.walk_cooldown = 0
        self.meats_picked = 0
        self.shoot_cooldown = 20
        self.points = 0
        self.can_shoot = False
        self.angle = 0

    def update(self, world, screen, w, h, enemy_list, fireball_list, meat_list, trap_list, lives_list, venom_bullet_list, power_up_list, spiderweb_list, sound_effects, lives_powerup_list):
        """Funcion encargada de manejar el funcionamiento pricipal del jugador, tanto como mostarlo en pantalla,
        como verificar sus colisiones y que hacer al respecto, como su movimiento

        Args:
            world (_type_): objeto con la infomacion del mundo
            screen (_type_): pantalla donde se va a mostrar
            w (_type_): ancho de la pantalla
            h (_type_): alto de la pantalla
            enemy_list (_type_): lista donde se encuentran todoss los enemigos
            fireball_list (_type_): lista donde se encuentran las bolas de fuego lanzadas por los enemigos
            meat_list (_type_): lista donde se encuentran los power up de carnes
            trap_list (_type_): lista donde se encuentran todas las trampas
            lives_list (_type_): lista de las vidas del jugador
            venom_bullet_list (_type_): lista de los disparos generador por el jugador
            power_up_list (_type_): lista donde se ecuentran los power up de disparo
            spiderweb_list (_type_): lista de los disparos generador por el boss
            sound_effects (_type_): estado de los efectos de sonidp
            lives_powerup_list (_type_): lista donde se ecuentran los powerups que otorgan vidas extras
        """
        self.dx = 0
        self.dy = 0
        self.walk_cooldown = 3
        self.shoot_cooldown += 1

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_a]:
            self.dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d]:
            self.dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_d] == False and key[pygame.K_a] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1 and self.jumped == True:
                self.image = self.images_jumping_right[self.index]
            elif self.direction == 1 and self.jumped == False:
                self.image = self.images_right[self.index]
            if self.direction == -1 and self.jumped == True:
                self.image = self.images_jumping_left[self.index]
            elif self.direction == -1 and self.jumped == False:
                self.image = self.images_left[self.index]
        
        
            
        self.animate()
        self.gravity()

        self.enemy_collides(enemy_list, lives_list, sound_effects)
        self.fireball_collides(fireball_list, lives_list, sound_effects)
        self.meat_collides(meat_list, sound_effects)
        self.saw_collides(trap_list, lives_list, sound_effects)
        self.power_up_shoot_collide(power_up_list)
        self.spiderweb_collide(spiderweb_list, lives_list, sound_effects)
        self.lives_powerup_collide(lives_powerup_list, lives_list)
        if self.can_shoot == True and self.shoot_cooldown > 80 and pygame.mouse.get_pressed()[0]:
            self.shoot_cooldown = 0
            self.shoot(venom_bullet_list, sound_effects)
        self.check_platforms_collide(world, w, h)
        

        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen,(255,255,255),self.rect, 5)

    def gravity(self):
        """funcion encargada de generar la gravedad al jugador
        """
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y

    def check_platforms_collide(self, world, w, h):
        """funcion encargad de verificar si el jugador se choco con alguna plataforma, y de mover el
        rectangulo del jugador

        Args:
            world (_type_): infomacion del mundo
            w (_type_): ancho de la pantalla
            h (_type_): alto de la pantalla
        """
        for tile in  world.tile_list:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if self.vel_y < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                    
                elif self.vel_y > 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.jumped = False

        if self.rect.left + self.dx > 0 and self.rect.right + self.dx < w:
            self.rect.x += self.dx
        self.rect.y += self.dy


    def animate(self):
        """funcion encargada de cambiar las animaciones del jugadro segun las acciones que
        este realizando
        """
        if self.counter > self.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.direction == 1 and self.jumped == False:
                if self.index >= len(self.images_right):
                    self.index = 0
                self.image = self.images_right[self.index]
            elif self.direction == 1 and self.jumped == True:
                if self.index >= len(self.images_jumping_right):
                    self.index = 0
                self.image = self.images_jumping_right[self.index]
            if self.direction == -1 and self.jumped == False:
                if self.index >= len(self.images_left):
                    self.index = 0
                self.image = self.images_left[self.index]
            elif self.direction == -1 and self.jumped == True:
                if self.index >= len(self.images_jumping_left):
                    self.index = 0
                self.image = self.images_jumping_left[self.index]
            
    def enemy_collides(self, enemy_list, lives_list, sound_effects):
        """funcion encargada de verificar las colisiones con los enemigos, segun como
        hayan sido mata al enemigo o le quita una vida al jugador

        Args:
            enemy_list (_type_): lista de los enemigos
            lives_list (_type_): lista de vidas del jugador
            sound_effects (_type_): estado de los efectos de sonido
        """

        for enemy in enemy_list:
            if enemy.can_move:
                
                if enemy.rect.colliderect(self.rect.left + 1, self.rect.top + 1, 2, self.height - 2) or enemy.rect.colliderect(self.rect.right -1 , self.rect.top + 1 , 2, self.height - 2):
                    for live in lives_list:
                        if live.used == False:
                            live.used = True
                            if sound_effects:
                                sound = pygame.mixer.Sound(hit_sound)
                                sound.set_volume(0.2)
                                sound.play()
                            break
                    self.dx = 0
                    self.dy = 0
                    self.rect.x,self.rect.y = self.spawn
                    
                
                elif enemy.rect.colliderect(self.rect.left + 1, self.rect.bottom - 1, self.width - 2, 2):
                    enemy.is_dead = True
                    self.points += 10
                    if sound_effects:
                        sound = pygame.mixer.Sound(damage_sound)
                        sound.set_volume(0.2)
                        sound.play()

        
    def fireball_collides(self, fireball_list, lives_list, sound_effects):
        """funcion encargada de verificar las colisiones con las bolas de fuego, 
        si le pegan, le quita una vida al jugador

        Args:
            fireball_list (_type_): lista de las bolas de fuego
            lives_list (_type_): lista de las vidas del jugador
            sound_effects (_type_): estado de los efectos de sonido
        """

        for fireball in fireball_list:
            if fireball.rect.colliderect(self.rect.left + 1, self.rect.top + 1, self.width - 1, 2):
                fireball.hit = True
                for live in lives_list:
                    if live.used == False:
                        live.used = True
                        if sound_effects:
                            sound = pygame.mixer.Sound(hit_sound)
                            sound.set_volume(0.2)
                            sound.play()

                        break
                self.rect.x,self.rect.y = self.spawn
                self.dx = 0
                self.dy = 0
                
    def meat_collides(self, meat_list, sound_effects):
        """funcion que se encarga de verficar las colision con los power ups de carnes

        Args:
            meat_list (_type_): lista de carnes
            sound_effects (_type_): efectos de sonido
        """

        for meat in meat_list:
            if meat.rect.colliderect(self.rect):
                meat.picked = True
                self.meats_picked += 1
                self.points += 10
                if sound_effects:
                    sound = pygame.mixer.Sound(eat_sound)
                    sound.set_volume(0.5)
                    sound.play()

    def saw_collides(self, trap_list, lives_list, sound_effects):
        """funcion que se encarga de verificar las colisiones del jugador con las trampas

        Args:
            trap_list (_type_): lista de trampas
            lives_list (_type_): lista de vidas del jugador
            sound_effects (_type_): estado de los efectos de sonido
        """
        
        for saw in trap_list:
            if saw.rect.colliderect(self.rect):
                for live in lives_list:
                    if live.used == False:
                        live.used = True
                        if sound_effects:
                            sound = pygame.mixer.Sound(hit_sound)
                            sound.set_volume(0.2)
                            sound.play()
                        break
                self.rect.x,self.rect.y = self.spawn
                self.dx = 0
                self.dy = 0

    def get_points(self):
        """funcion encargada de tomar los puntos actuales del jugador

        Returns:
            _type_: puntos actuales del jugador
        """
        return self.points

    def shoot(self, venom_bullet_list, sound_effects):
        """funcion encargada de hacer que el personaje principal dispare

        Args:
            venom_bullet_list (_type_): lista de los disparos de jugador
            sound_effects (_type_): estado de los efectos de sonido
        """
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.center[0]
        y_dist = -(pos[1] - self.rect.center[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        aux = VenomShoot(*self.rect.center,self.angle)
        venom_bullet_list.append(aux)
        if sound_effects:
            sound = pygame.mixer.Sound(venom_shoot_sound)
            sound.set_volume(0.2)
            sound.play()

    def power_up_shoot_collide(self, power_up_list):
        """verificar las colisiones con los power up de disparo

        Args:
            power_up_list (_type_): lista de los power up de disparo
        """
        for power_up in power_up_list:
            if power_up.rect.colliderect(self.rect):
                self.can_shoot = True
                power_up.picked = True

    def spiderweb_collide(self, spiderweb_list, lives_list, sound_effects):
        """verifica las colisiones del personaje principal con los tiros del boss

        Args:
            spiderweb_list (_type_): lista con los disparos del boss
            lives_list (_type_): lista de las vidas del jugador
            sound_effects (_type_): estado de los efectos de sonido
        """
        for web in spiderweb_list:
            if web.rect.colliderect(self.rect):
                spiderweb_list.remove(web)
                for live in lives_list:
                    if live.used == False:
                        live.used = True
                        if sound_effects:
                            sound = pygame.mixer.Sound(hit_sound)
                            sound.set_volume(0.2)
                            sound.play()
                        break

    def lives_powerup_collide(self, lives_powerup_list, lives_list):
        """verefica las colisiones con los power up de vida

        Args:
            lives_powerup_list (_type_): lista de los powerup de vida
            lives_list (_type_):lista de las vidas del jugador
        """
        for live_powerup in lives_powerup_list:
            if live_powerup.rect.colliderect(self.rect):
                for live in lives_list:
                    if live.used:
                        live.used = False
                        lives_powerup_list.remove(live_powerup)
                        break