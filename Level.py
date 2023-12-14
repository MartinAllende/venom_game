from World import *
from Player import *
from Enemy import *
from InvisibleBlock import *
from FireBalls import *
from Meat import *
from Lives import *
from EndDoor import *
from Points import *
from Timer import *
from ShootPowerUp import *
from VenomShoot import *
from LivesPowerUp import *
import random

class Level():
    def __init__(self, world_data):
        """funcion encargada de crear el nivel

        Args:
            world_data (_type_): informacion del nivel
        """

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.initial_time = pygame.time.get_ticks()
        self.tile_size = 40
        self.power_up_list = []
        self.enemy_list = []
        self.invisible_block_list = []
        self.meat_list = []
        self.trap_list = []
        self.fireball_list = []
        self.lives_list = []
        self.door_list = []
        self.venom_bullet_list = []
        self.boss_list = []
        self.spiderweb_list = []
        self.lives_power_up_list = []

        x = 800 - 40
        y = 10
        for i in range(3):
            aux = Lives(x,y)
            x-=40
            self.lives_list.append(aux)

        self.timer = Timer(300,0)
        self.points = Points(500,0)
        self.player = Player(100, 700)
        self.world = World(world_data, self.tile_size, self.enemy_list, self.invisible_block_list, self.meat_list, self.trap_list, self.door_list, self.power_up_list, self.boss_list, self.lives_power_up_list)
        self.time = 0

    def update(self, screen, background, w,h, sound_effects, paused_times, extreme_mode):
        """funcion encarga de llamar a la funcion de funcionamiento general de cada objeto del juego, tanto balas, 
        peronaje principal, enemigos, etc

        Args:
            screen (_type_): pantalla donde se mostrara el nivel
            background (_type_): fondo de la pantalla del nivel
            w (_type_): ancho de la pantalla
            h (_type_): largo de la pantalla
            sound_effects (_type_): estado de los efectos de sonido
            paused_times (_type_): lista con los tiempo en los que se pauso

        Returns:
            _type_: 1 en caso de que las vidas del jugador sean 0, o de que el tiempo haya pasado los 90 seg,
            sino retorna 2 en caso de que el usuario haya entrado por la puerta final, sino 
            se cumplio ninguna de las 2 retorna 0
        """

        self.actual_time = pygame.time.get_ticks()
        self.elapsed_time = self.actual_time - self.initial_time
        for times in paused_times:
            self.elapsed_time -= times
        meat_counter = 0
        lives_counter = 0
        self.time += 1
        self.clock.tick(self.fps)
        screen.blit(background, (0,0))
        self.world.draw(screen)
        for enemy in self.enemy_list:
            enemy.update(screen,self.world,w,h, self.invisible_block_list, self.enemy_list, self.time, self.fireball_list)
        for fireball in self.fireball_list:
            fireball.update(screen, w,h, self.fireball_list)
        for meat in self.meat_list:
            meat_counter += 1
            meat.update(screen,meat_counter)
        for trap in self.trap_list:
            trap.update(screen, self.invisible_block_list)
        for door in self.door_list:
            door.update(screen, self.meat_list, self.boss_list)
            if self.player.rect.colliderect(door.rect) and door.open:
                aux_door = True
            else:
                aux_door = False
        for power_up in self.power_up_list:
            power_up.update(screen, self.power_up_list)
        for bullet in self.venom_bullet_list:
            bullet.update(screen, w, h, self.venom_bullet_list)
        for boss in self.boss_list:
            boss.update(screen,self.world,w,h, self.venom_bullet_list, self.spiderweb_list, self.player, sound_effects)
        for web in self.spiderweb_list:
            web.update(screen, w, h, self.spiderweb_list)
        
        self.player.update(self.world, screen, w, h, self.enemy_list, self.fireball_list, self.meat_list, self.trap_list, self.lives_list, self.venom_bullet_list, self.power_up_list, self.spiderweb_list, sound_effects, self.lives_power_up_list)
        
        self.timer.update(screen,self.elapsed_time)
        self.points.update(screen, self.player.get_points())

        if extreme_mode:
            self.aleatory_enemy_spawn()

        for live in self.lives_list:
            live.update(screen)
            if live.used == False:
                lives_counter += 1

        for live_powerup in self.lives_power_up_list:
            live_powerup.update(screen,self.lives_power_up_list)
            
        if lives_counter == 0 or self.elapsed_time * 0.001 > 60:
            aux = 1
        elif aux_door == True:
            aux = 2
        else:
            aux = 0

        return aux
    
    def get_points(self):
        """funcion encargada de conseguir los puntos conseguidos por el jugador

        Returns:
            _type_: puntos conseguidos por el jugador
        """
        return self.player.get_points()
    
    def get_lives(self):
        """funcion encargada de contar la cantidad de vidas con las que termino del jugador

        Returns:
            _type_: cantidad de vidas del jugador
        """
        counter = 0
        for live in self.lives_list:
            if live.used == False:
                counter += 1
        return counter
    
    def get_time(self):
        """encargada de obtener el tiempo en el cual termino el nivel

        Returns:
            _type_: tiempo en el cual termino de nivel
        """
        return int(self.elapsed_time * 0.001)

    def aleatory_enemy_spawn(self):
        number = random.randint(1,200)
        if number == 25 and len(self.enemy_list) <= 8 and self.player.rect.top > 500:
           x = random.randint(50,750)
           y = random.randint(50, self.player.rect.bottom - 50)
           aux = Enemy(x,y,False,True,False)
           self.enemy_list.append(aux)
        elif number == 25 and len(self.enemy_list) <= 8  and self.player.rect.top <= 500:
           x = random.randint(50,750)
           y = random.randint(self.player.rect.top + 200,750)
           aux = Enemy(x,y,False,True,False)
           self.enemy_list.append(aux)