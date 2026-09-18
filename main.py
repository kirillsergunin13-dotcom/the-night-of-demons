from classs.game_state import *
from classs.state import State
import ui.visual_field as ui
import pygame
import sys
import json

setting={"hardcor_record":0,"standart_record":0,"codes":[]}

try:
    with open("setting.json", 'r', encoding='utf-8') as file:
        setting = json.load(file)
except:
    print("Load Error")


game=GameState(11 in setting["codes"])

if 11 in setting["codes"]:
    try:
        with open("hardcor_game.json", 'r', encoding='utf-8') as file:
            set_game = json.load(file)
        if set_game!={}:
            game.json_to_class(set_game)
    except:
        print("Load Error")
else:
    try:
        with open("standart_game.json", 'r', encoding='utf-8') as file:
            set_game = json.load(file)
        if set_game!={}:
            game.json_to_class(set_game)
    except:
        print("Load Error")

state=State(game)


clock = pygame.time.Clock()
flag=True

while flag :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            flag=False
            pygame.quit()
            sys.exit()
        state.event_update(event)
    
    state.keys_tick(keys=pygame.key.get_pressed())
    state.tick_run(setting["codes"],setting)

    pygame.display.flip()
    clock.tick(60)


