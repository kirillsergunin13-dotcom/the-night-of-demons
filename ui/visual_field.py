import pygame
from classs.playing_field import *

player_one=pygame.image.load("assets/images/player.png")
player_one=pygame.transform.scale(player_one,(60,60))

player_two=pygame.image.load("assets/images/player_animation.png")
player_two=pygame.transform.scale(player_two,(60,60))

table=pygame.image.load("assets/images/table.png")
table=pygame.transform.scale(table,(50,50))

candel=pygame.image.load("assets/images/candel.png")
candel=pygame.transform.scale(candel,(25,25))
big_candel=pygame.transform.scale(candel,(50,50))

crucifix=pygame.image.load("assets/images/crucifix.png")
crucifix=pygame.transform.scale(crucifix,(25,25))

back=pygame.image.load("assets/images/down_ground.png")
back=pygame.transform.scale(back,(960,620))

def visual_blocks(field:list,window):
    window.blit(back,(0,0))
    for y in range(0,12):
        for x in range(0,19):
            if field[y][x]==1:
                window.blit(table,((x*50)+10,(y*50)+10))
            if field[y][x]==3:
                window.blit(table,((x*50)+10,(y*50)+10))

def visual_item(items:list[Item],window):
    for item in items:
        if item.visual==0 and item.lies:
            window.blit(candel,((item.x*50)+20,(item.y*50)+13))
        elif item.visual==1 and item.lies:
            window.blit(crucifix,((item.x*50)+20,(item.y*50)+13))

def visual_player(coordinate0,coordinate1,window,animation_tick):
    if animation_tick<200:
        window.blit(player_one,(coordinate0,coordinate1))
    else:
        window.blit(player_two,(coordinate0,coordinate1))

def visual_candel(count,window):
    if count>=1:
        window.blit(big_candel,(300,200))
    if count>=2:
        window.blit(big_candel,(400,300))
    if count>=3:
        window.blit(big_candel,(500,200))
