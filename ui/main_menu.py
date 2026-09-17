import pygame
from classs.playing_field import *

main_menu_one=pygame.image.load("assets/images/main_menu_one.png")
main_menu_one=pygame.transform.scale(main_menu_one,(960,620))

def visual_menu(window):
    window.blit(main_menu_one,(0,0))
