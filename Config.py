import pygame

def rotate_images(original_list,flip_x,flip_y):
    """funcion encargada de rotar una lista de imagenes

    Args:
        original_list (_type_): lista a rotar
        flip_x (_type_): bool que representa si se quiere rotar en eje x
        flip_y (_type_): bool que representa si se quiere rotar en eje y

    Returns:
        _type_: lista_rotada
    """
    rotated_list =[]
    for image in original_list:
       rotated_list.append(pygame.transform.flip(image, flip_x, flip_y))
    return rotated_list

def rescale_images(list_animations, width, heigth):
    """funcion encargada de reescalar una lista de imagenes

    Args:
        list_animations (_type_): lista de imagenes a reescalar
        width (_type_): ancho de las imagenes
        heigth (_type_): alto de la imagenes
    """
    for i in range(len(list_animations)):
        img = list_animations[i]
        list_animations[i] = pygame.transform.scale(img,(width,heigth))

venom_right = [pygame.image.load(r"imagenes\venom\caminando\camina1.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina2.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina3.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina4.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina5.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina6.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina7.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina8.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina9.png"),
                        pygame.image.load(r"imagenes\venom\caminando\camina10.png")]
venom_left = rotate_images(venom_right, True, False)
venom_jump_right = [pygame.image.load(r"imagenes\venom\salta\salta3.png")]   
venom_jump_left = rotate_images(venom_jump_right, True, False)
venom_still = [pygame.image.load(r"imagenes\venom\quieto\quieto1.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto2.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto3.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto4.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto5.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto6.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto7.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto8.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto9.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto10.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto11.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto12.png"),
                pygame.image.load(r"imagenes\venom\quieto\quieto13.png")]

venom_shoot = pygame.image.load(r"imagenes\venom\venom_magma.png")
background_image = pygame.image.load(r"imagenes\background.PNG")
final_background = pygame.image.load(r"imagenes\final_background.jpg")

enemy_left_walk = [pygame.image.load(r"imagenes\enemigos\spider1.png"),
               pygame.image.load(r"imagenes\enemigos\spider2.png"),
               pygame.image.load(r"imagenes\enemigos\spider3.png")]

enemy_right_walk = rotate_images(enemy_left_walk, True, False)

enemy_right_fly = [pygame.image.load(r"imagenes\enemigos\heli1.png"),
                   pygame.image.load(r"imagenes\enemigos\heli2.png"),
                   pygame.image.load(r"imagenes\enemigos\heli3.png"),
                   pygame.image.load(r"imagenes\enemigos\heli4.png")]

enemy_left_fly = rotate_images(enemy_right_fly, True, False)

fire_ball = pygame.image.load(r"imagenes/enemigos/FireBall.png")

spiderman_up = [pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman1.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman2.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman3.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman4.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman5.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman6.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman7.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_up\spiderman8.png")]

spiderman_down = rotate_images(spiderman_up, False, True)

spiderman_right = [pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman1.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman2.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman3.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman4.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman5.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman6.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman7.png"),
                pygame.image.load(r"imagenes\enemigos\spiderman_right\spiderman8.png")]

spiderman_left = rotate_images(spiderman_right, True, False)

spiderman_death = pygame.image.load(r"imagenes\enemigos\spiderman_death.png")

spiderweb = pygame.image.load(r"imagenes\enemigos\spiderweb.png")

meat = pygame.image.load(r"imagenes\meat.png")

saw_movement = [pygame.image.load(r"imagenes\saw\saw1.png"),
                pygame.image.load(r"imagenes\saw\saw2.png"),
                pygame.image.load(r"imagenes\saw\saw3.png"),
                pygame.image.load(r"imagenes\saw\saw4.png"),
                pygame.image.load(r"imagenes\saw\saw5.png")]

live = pygame.image.load(r"imagenes\venom\heart.png")

door_images = [pygame.image.load(r"imagenes\plataformas\door\door1.png"),
        pygame.image.load(r"imagenes\plataformas\door\door2.png"),
        pygame.image.load(r"imagenes\plataformas\door\door3.png"),
        pygame.image.load(r"imagenes\plataformas\door\door4.png")]

play_button = pygame.image.load(r"imagenes\buttons\Play Button.png")
resume_button = pygame.image.load(r"imagenes\buttons\Resume Button.png")
return_button = pygame.image.load(r"imagenes\buttons\Back Square Button.png")
quit_button = pygame.image.load(r"imagenes\buttons\Quit Button.png")
main_menu_button = pygame.image.load(r"imagenes\buttons\Menu Button.png")
setting_button = pygame.image.load(r"imagenes\buttons\Settings Button.png")
on_button = pygame.image.load(r"imagenes\buttons\on_button.png")
off_button = pygame.image.load(r"imagenes\buttons\off_button.png")
leaderboard_button = pygame.image.load(r"imagenes\buttons\leaderboard_button.png")
back_button = pygame.image.load(r"imagenes\buttons\back_button.png")
next_button = pygame.image.load(r"imagenes\buttons\next_button.png")
load_button = pygame.image.load(r"imagenes\buttons\load_button.png")

background_sound = r"sounds\background_sound.mp3"
damage_sound = r"sounds\damage_sound.mp3"
eat_sound = r"sounds\eat_sound.mp3"
hit_sound = r"sounds\hit_sound.mp3"
venom_shoot_sound = r"sounds\venom_shot.mp3"
venom_shoot_hit = r"sounds\venom_shoot_hit.mp3"
spiderman_shot_sound = r"sounds\spiderman_shoot.mp3"

