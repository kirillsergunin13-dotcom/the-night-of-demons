import pygame
from classs.playing_field import *

player=pygame.image.load("assets/images/player.png")


table=pygame.image.load("assets/images/table.png")
table=pygame.transform.scale(table,(50,50))

candel=pygame.image.load("assets/images/candel.png")
candel=pygame.transform.scale(candel,(25,25))
big_candel=pygame.transform.scale(candel,(50,50))

crucifix=pygame.image.load("assets/images/crucifix.png")
crucifix=pygame.transform.scale(crucifix,(25,25))

def visual_blocks(field:list,window):
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

def visual_player(coordinate0,coordinate1,window):
    window.blit(player,(coordinate0,coordinate1))

def visual_candel(count,window):
    if count>=1:
        window.blit(big_candel,(300,200))
    if count>=2:
        window.blit(big_candel,(400,300))
    if count>=3:
        window.blit(big_candel,(500,200))
