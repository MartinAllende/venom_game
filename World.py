import pygame
from Enemy import *
from InvisibleBlock import *
from Meat import *
from Saw import *
from EndDoor import *
from ShootPowerUp import *
from Boss import *
from LivesPowerUp import *

class World():
    def __init__(self,data,tile_size,enemy_list,invisible_block_list, meat_list, trap_list, door_list, power_up_list, boss_list, lives_powerup_list):
        """funcion encargada de crear el mundo , creando cada una de las entidades segun lo dado en la data,
        dejando cada entidad en la posicion dada

        Args:
            data (_type_): data del nivel
            tile_size (_type_): tamanio de los cuadrado que dividen la pantalla
            enemy_list (_type_): lista de enemigos
            invisible_block_list (_type_): lista de los bloques invisibles
            meat_list (_type_): lista de los powerup de las carnes
            trap_list (_type_): lista de las trampas
            door_list (_type_): lista de la puerta final
            power_up_list (_type_): lista de los powerup de disparo
            boss_list (_type_): lista del boss
            lives_powerup_list (_type_): lista de los powerup de vidas extra
        """
        self.tile_list = []

        floor_img = pygame.image.load(r"imagenes\plataformas\piso.png")
        plat_img = pygame.image.load(r"imagenes\plataformas\plataforma.png")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(plat_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(floor_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    aux = Enemy(col_count*tile_size,row_count*tile_size,False,True,False)
                    enemy_list.append(aux)
                if tile == 4:
                    aux = Enemy(col_count*tile_size,row_count*tile_size,False,False,True)
                    enemy_list.append(aux)
                if tile == 5:
                    aux = InvisibleBlock(col_count*tile_size,row_count*tile_size, tile_size)
                    invisible_block_list.append(aux)
                if tile == 6:
                    aux = Meat(col_count*tile_size,row_count*tile_size)
                    meat_list.append(aux)
                if tile == 7:
                    aux = Saw(col_count*tile_size,row_count*tile_size,True,False)
                    trap_list.append(aux)
                if tile == 8:
                    aux = Saw(col_count*tile_size,row_count*tile_size,False,True)
                    trap_list.append(aux)
                if tile == 9:
                    aux = EndDoor(col_count*tile_size,row_count*tile_size)
                    door_list.append(aux)
                if tile == 10:
                    aux = ShootPowerUp(col_count*tile_size,row_count*tile_size)
                    power_up_list.append(aux)
                if tile == 11:
                    aux = Boss(col_count*tile_size,row_count*tile_size)
                    boss_list.append(aux)
                if tile == 12:
                    aux = LivesPowerUp(col_count*tile_size,row_count*tile_size)
                    lives_powerup_list.append(aux)
                col_count += 1
            row_count += 1

    def draw(self,screen):
        """funcion encargada de mostrar las plataformas en pantalla

        Args:
            screen (_type_): pantalla donde se van a mostrar 
        """
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
            # pygame.draw.rect(screen, (255,0,255), tile[1], 1)