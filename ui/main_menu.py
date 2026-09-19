import pygame
from classs.playing_field import *

main_menu_one=pygame.image.load("assets/images/main_menu_one.png")
main_menu_one=pygame.transform.scale(main_menu_one,(960,620))

main_menu_two=pygame.image.load("assets/images/main_menu_one_animation.png")
main_menu_two=pygame.transform.scale(main_menu_two,(960,620))

def visual_menu(window,animacion_tick):
    if animacion_tick<200:
        window.blit(main_menu_one,(0,0))
    else:
        window.blit(main_menu_two,(0,0))
