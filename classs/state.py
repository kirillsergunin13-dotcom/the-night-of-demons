from classs.game_state import GameState
from ui.main_menu import *
from ui.visual_field import *
import pygame
import json

pygame.init()
font= pygame.font.Font(None,30)
big_font= pygame.font.Font(None,70)

damage_image=pygame.image.load("assets/images/table.png")
damage_image=pygame.transform.scale(damage_image,(960,620))

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
            visual_candel(self.game.candles,self.window)
            visual_player(self.game.play_field.player_x,self.game.play_field.player_y,self.window)
            if self.state_time>=0:
                self.state_time-=1
                self.window.blit(damage_image,(0,0))
            self.window.blit(font.render(f"Сентябрь {self.game.night}",True,(255,0,0)),(0,0))

            if self.game.health<=0:
                self.game=0
                self.game=GameState(False)
                self.state_name = "main_menu"
                data=self.game.class_to_json()
                with open("standart_game.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4)


            if self.game.candles>=3 and self.game.crucifix>=0:
                self.game.update()
                
                data=self.game.class_to_json()
                with open("standart_game.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4)
                
        elif self.state_name=="one_night":
            one_night_text_1=big_font.render(f"   Эта ваша первая ночь в этом доме, ",True,(255,0,0))
            one_night_text_2=font.render("          она дешёвая, но каждую ночь вас могут разбудить демоны,",True,(255,100,100))
            one_night_text_3=font.render("          найдите 3 свечи что-бы призвать физическое тело демона, ",True,(255,100,100))
            one_night_text_4=font.render("              после постарайтесь выжить пока демон не устанет, ",True,(255,100,100))
            one_night_text_5=font.render("ну и в конце используйте распятие что-бы его изгнать и можете спать спокойно.",True,(255,100,100))
            one_night_text_6=font.render("И не забудьте демон может создавать мебель и предметы, не касайтесь их!",True,(255,100,100))
            self.window.blit(one_night_text_1,(0,80))
            self.window.blit(one_night_text_2,(100,130))
            self.window.blit(one_night_text_3,(100,160))
            self.window.blit(one_night_text_4,(100,190))
            self.window.blit(one_night_text_5,(100,220))
            self.window.blit(one_night_text_6,(100,250))
            
    def keys_tick(self,keys):
        if keys[pygame.K_ESCAPE] and self.state_name=="game_find":
            self.state_name="main_menu"

        if self.state_name=="game_find":
            if keys[pygame.K_w] and self.game.play_field.player_y>0:
                self.game.play_field.player_y-=1
            if keys[pygame.K_s] and self.game.play_field.player_y<620:
                self.game.play_field.player_y+=1
            if keys[pygame.K_a] and self.game.play_field.player_x>0:
                self.game.play_field.player_x-=1
            if keys[pygame.K_d] and self.game.play_field.player_x<960:
                self.game.play_field.player_x+=1

    def event_update(self,event):
        if event.type==pygame.MOUSEBUTTONUP and self.state_name=="game_find":
            x=self.game.play_field.player_x//50
            y=self.game.play_field.player_y//50
            for item in self.game.play_field.items:
                if item.x==x and item.y==y and item.lies:
                    item.lies=False
                    if item.visual==0:
                        self.game.candles+=1
                    if item.visual==1:
                        self.game.crucifix=+1
                    if item.demon_item and random.choice([0,0,1])==1:
                        self.game.health-=1
                        self.state_time+=60
        elif event.type==pygame.MOUSEBUTTONUP and self.state_name=="main_menu":
            if self.game.night==0:
                self.state_name="one_night"
            else:
                self.state_name="game_find"
        elif event.type==pygame.MOUSEBUTTONUP and self.state_name=="one_night":
            self.state_name="game_find"
        