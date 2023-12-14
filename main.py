import pygame
from pygame.locals import *
from Config import *
from MainMenu import *
from PauseMenu import *
from Level import *
from LevelSelector import *
from EndMenu import *
from SettingMenu import *
from LeaderBoard import *
from TextBox import *
from DbFunctions import *
import json
import sqlite3


def get_data(path):
    """funcion encargad de tomar la informacion de un archivos json

    Args:
        path (_type_): ubicacion del archivo a leer

    Returns:
        _type_: informacion del archivo 
    """
    
    with open(path) as file:
        data = json.load(file)
    return data

try:

    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    W,H = 800,800

    screen = pygame.display.set_mode((W,H))
    menu_background = background_image
    menu_background = pygame.transform.scale(menu_background, (W, H))

    world_data = get_data("data.json")

    pygame.mixer.init()
    music = pygame.mixer.Sound(background_sound)
    music.set_volume(0.1)
    music.play(-1)

    name_entry = TextBox()
    menu = MainMenu()
    setting_menu = SettingMenu()
    pause_menu = PauseMenu()
    end_menu = EndMenu()

    music_state = True
    flag_music = False
    sound_effects = True
    extreme_mode = False

    flag = True
    in_name_entry = True
    in_main_menu =  False
    in_settings = False
    in_leaderboard = False
    in_level_selector = False
    in_end_menu = False
    in_level = False
    in_pause = False
    click_pos = (0,0)

    while flag:

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                flag = False
            if event.type == KEYDOWN:
                key = pygame.key.get_pressed()
                if  key[pygame.K_ESCAPE]:
                    if in_level:
                        initial_pause_time = pygame.time.get_ticks()
                        in_level = False
                        in_pause = True

        if in_name_entry:

            screen.blit(menu_background,(0,0))
            in_main_menu = name_entry.update(screen, click_pos, event_list)
            if in_main_menu:
                in_name_entry = False
                player_name = name_entry.get_text()
                click_pos = (0,0)
            
    ####################################################### MAIN_MENU #########################################################

        if in_main_menu:
            
            extreme_mode = menu.get_extreme_mode()
            aux = menu.update(screen, click_pos)
            if aux == 1:
                in_level_selector = True
                player_points_list = get_score_by_name(player_name, world_data)
                level_selector = LevelSelector(world_data, player_points_list)
                in_main_menu = False
                click_pos = (0,0)
            if aux == 2:
                in_settings = True
                in_main_menu = False
                click_pos = (0,0)
            if aux == 3:
                in_leaderboard = True
                points_list = get_scores_ordered(world_data)
                index = 0
                leaderboard = LeaderBoard(points_list[index], index + 1)
                in_main_menu = False
                click_pos = (0,0)
            click_pos = (0,0)

    ####################################################### SETTINGS_MENU #########################################################

        if in_settings:

            screen.blit(menu_background,(0,0))
            
            in_main_menu = setting_menu.update(screen, click_pos)

            music_state = setting_menu.get_music_state()

            if music_state and flag_music:
                flag_music = False
                music.set_volume(0.1)
                music.play(-1)
            elif music_state == False:
                flag_music = True
                music.stop()

            sound_effects = setting_menu.get_sound_effects_state()

            if in_main_menu:
                in_settings = False

            click_pos = (0,0)

    ####################################################### LEADERBOARD #########################################################

        if in_leaderboard:
            
            screen.blit(menu_background,(0,0))

            aux = leaderboard.update(screen, click_pos)

            if aux == 1:
                in_main_menu = True
                in_leaderboard = False
                click_pos = (0,0)

            if aux == 2:
                index -= 1
                if index < 0:
                    index = len(points_list) -1
                leaderboard = LeaderBoard(points_list[index], index + 1)
                click_pos = (0,0)

            if aux == 3:
                index += 1
                if index > len(points_list) -1 :
                    index = 0
                leaderboard = LeaderBoard(points_list[index], index + 1)
                click_pos = (0,0)

    ####################################################### LEVEL_SELECTOR #########################################################

        if in_level_selector:
            
            screen.blit(menu_background,(0,0))

            for lvl in level_selector.bloqued_buttons:
                lvl.update(screen, click_pos)

            for lvl in level_selector.level_buttons:
                in_level = lvl.update(screen,click_pos)
            
                
                if in_level:
                    in_level_selector = False
                    lvl_number = lvl.number
                    level = Level(world_data[str(lvl.number)])
                    paused_times = []
                    if lvl.number == 3:
                        background = final_background
                        background = pygame.transform.scale(background, (W, H))
                    else:
                        background = background_image
                        background = pygame.transform.scale(background, (W, H))


                    click_pos = (0,0)
                    break

            in_main_menu = level_selector.return_button.update(screen,click_pos)
            if in_main_menu:
                in_level_selector = False
                click_pos = (0,0)


    ####################################################### PAUSE #########################################################

        if in_pause:
            
            actual_pause_time = pygame.time.get_ticks()
            pause_time = actual_pause_time - initial_pause_time
            pause_decition = pause_menu.update(screen, click_pos)
            if pause_decition == 1:
                paused_times.append(pause_time)
                in_level = True
                in_pause = False
            if pause_decition == 2:
                in_pause = False
                in_main_menu = True

    ####################################################### LEVEL #########################################################

        if in_level:

            click_pos = (0,0)
            aux = level.update(screen,background, W,H, sound_effects, paused_times, extreme_mode)
            if aux == 2:
                in_end_menu = True
                in_level = False
            if aux == 1:
                in_main_menu = True
                in_level = False
                
    ####################################################### ENDLEVEL_MENU #########################################################
        
        if in_end_menu:

            in_main_menu = end_menu.update(screen,click_pos,level.get_points(),level.get_lives(),level.get_time())
            if in_main_menu:
                
                insertRow(player_name, end_menu.get_final_points(), lvl_number)
                in_end_menu = False

        pygame.display.update()
        
    pygame.quit()

except Exception as ex:

    pygame.quit()
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    W,H = 800,300

    screen = pygame.display.set_mode((W,H))

    flag = True

    fount = pygame.font.SysFont("Arial", 15)

    text = f"Error, {ex}"
    text = fount.render(str(text), True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = (400,150)

    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

        screen.fill((0,0,0))
        screen.blit(text, text_rect)

        pygame.display.update()

        