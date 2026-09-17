from classs.game_state import GameState
from classs.state import State
import ui.visual_field as ui
import pygame
import sys
pygame.init()


game=GameState(False)

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

    state.tick_run()

    pygame.display.flip()
    clock.tick(60)
