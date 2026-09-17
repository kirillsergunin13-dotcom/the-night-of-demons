from classs.game_state import GameState
from ui.main_menu import *
from ui.visual_field import *
import pygame


class State:
    state_name:str = "main_menu"
    state_time:int = 0
    window:pygame.display
    game:GameState

    def __init__(self,game:GameState):
        self.window=pygame.display.set_mode((960,620))
        self.game=game
    def tick_run(self):
        self.window.fill((0,0,0))
        if self.state_name=="main_menu":
            visual_menu(self.window)
        elif self.state_name=="game_find":
            visual_blocks(self.game.play_field.play_room,self.window)
            visual_item(self.game.play_field.items,self.window)

    def keys_tick(self,keys):
        if keys[pygame.K_ESCAPE] and self.state_name=="game_find":
            self.state_name="main_menu"

    def event_update(self,event):
        if event.type==pygame.MOUSEBUTTONUP and self.state_name=="game_find":
            self.game.update()
        elif event.type==pygame.MOUSEBUTTONUP and self.state_name=="main_menu":
            self.state_name="game_find"
        