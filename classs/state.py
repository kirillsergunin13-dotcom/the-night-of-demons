from classs.game_state import GameState
from ui.main_menu import *
from ui.visual_field import *
from ui.attack_visual import *
import pygame
import json
import assets.attack.main_attack as attack

pygame.init()
pygame.mixer.init()
font= pygame.font.Font(None,30)
big_font= pygame.font.Font(None,70)

walk = pygame.mixer.Sound("assets/music/walking.mp3")
walk_channel = pygame.mixer.Channel(0)

attack_music = pygame.mixer.Sound("assets/music/attack.mp3")
item_music = pygame.mixer.Sound("assets/music/item.mp3")
demon_music = pygame.mixer.Sound("assets/music/demon.mp3")
die_music = pygame.mixer.Sound("assets/music/die.mp3")

damage_image_one=pygame.image.load("assets/images/demon.png")
damage_image_one=pygame.transform.scale(damage_image_one,(960,620))

damage_image_two=pygame.image.load("assets/images/demon_anim.png")
damage_image_two=pygame.transform.scale(damage_image_two,(960,620))

class State:
    state_name:str = "main_menu"
    state_time:int = 0
    window:pygame.display
    game:GameState
    attack:str
    attack_time:int
    darkness:int 
    next_state:str
    animation_tick:int

    def __init__(self,game:GameState):
        self.animation_tick=0
        self.window=pygame.display.set_mode((960,620))
        self.game=game
        self.attack_time=0
        self.darkness=0
    def tick_run(self,codes:list,setting):
        self.animation_tick+=1
        if self.animation_tick>=350:
            self.animation_tick=0
        if 868989 not in codes:
            if self.game.health<=0:
                die_music.play()
                print()
                if 11 in codes:
                    setting["hardcor_record"]=max(self.game.night,setting["hardcor_record"])
                    with open("setting.json", 'w', encoding='utf-8') as file:
                        json.dump(setting, file, indent=4)
                else:
                    setting["standart_record"]=max(self.game.night,setting["standart_record"])
                    with open("setting.json", 'w', encoding='utf-8') as file:
                        json.dump(setting, file, indent=4)
                self.game=0
                self.game=GameState(11 in codes)
                self.state_name = "main_menu"
                if 998875 not in codes:
                    self.darkness=255
                data=self.game.class_to_json()
                if 11 in codes:
                    with open("hardcor_game.json", 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4)
                else:
                    with open("standart_game.json", 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4)

        self.window.fill((0,0,0))

        

        if self.state_name=="main_menu":
            self.animation_tick+=2
            visual_menu(self.window,self.animation_tick)
        elif self.state_name=="attack_time":
            if self.state_time<=0 or 123789 in codes:
                self.state_name="game_find"
                if 998875 not in codes:
                    self.darkness=270
                self.game.update()

                data=self.game.class_to_json()
                with open("standart_game.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4)

            visual_blocks(self.game.play_field.play_room,self.window)
            visual_item(self.game.play_field.items,self.window)
            visual_candel(self.game.candles,self.window)
            visual_player(self.game.play_field.player_x,self.game.play_field.player_y,self.window,self.animation_tick)
            if self.animation_tick<300:
                self.window.blit(damage_image_one,(0,0))
            else:
                self.window.blit(damage_image_two,(0,0))
            visual_choice_attack(self.attack,self.window,self.attack_time)
            self.window.blit(font.render(f"Здоровье {self.game.health}",True,(255,0,0)),(800,0))

            if self.attack_time<=0:
                player_x=self.game.play_field.player_x//50
                player_y=self.game.play_field.player_y//50

                print("x",player_x,"y",player_y)
                if self.attack=="linery_attack" and player_y<=5:
                    self.game.health-=1
                elif self.attack=="table_attack" and self.game.play_field.play_room[player_y][player_x] !=1:
                    self.game.health-=1
                elif self.attack=="attack" and player_x>=5 and player_x<=10 :
                    self.game.health-=1
                elif self.attack=="right_attack" and player_x>=10:
                    self.game.health-=1
                elif self.attack=="left_attack" and player_x<=5:
                    self.game.health-=1
                elif self.attack=="y_wall" and player_y>=10:
                    self.game.health-=1
                attack_music.play()
                self.attack=attack.attack_choice(self.state_time)
                
                self.attack_time=80
                self.state_time-=90

                if 8685848 in codes:
                    self.attack_time=120
                if 8784858689 in codes:
                    self.state_time+=85
            else:
                self.attack_time-=1
                        
        elif self.state_name=="game_find":
            visual_blocks(self.game.play_field.play_room,self.window)
            visual_item(self.game.play_field.items,self.window)
            visual_candel(self.game.candles,self.window)
            visual_player(self.game.play_field.player_x,self.game.play_field.player_y,self.window,self.animation_tick)
            if self.state_time>=0:
                self.state_time-=1
                if self.animation_tick<200:
                    self.window.blit(damage_image_one,(0,0))
                else:
                    self.window.blit(damage_image_two,(0,0))
            self.window.blit(font.render(f"Здоровье {self.game.health}",True,(255,0,0)),(800,0))
            self.window.blit(font.render(f"Сентябрь {self.game.night}",True,(255,0,0)),(0,0))

            


            if (self.game.candles>=3 and self.game.crucifix>=0) or 987321 in codes:
                demon_music.play()
                self.state_name="attack_time"
                if 998875 not in codes:
                    self.darkness=200
                self.state_time=(self.game.night)*100
                self.attack_time=80
                self.attack=attack.attack_choice(self.state_time)
                
                
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

        if self.darkness>0:
            self.darkness-=1
            dark = pygame.Surface((1000, 1000))
            dark.fill((0,0,0))
            dark.set_alpha(self.darkness) 
            self.window.blit(dark,(0,0))
        elif self.darkness<0:
            self.darkness+=1
            if 998875 in codes:
                self.darkness=0
            dark_anti = pygame.Surface((1000, 1000))
            dark_anti.fill((0,0,0))
            dark_anti.set_alpha(255+self.darkness) 
            self.window.blit(dark_anti,(0,0))
            if self.darkness==0:
                self.state_name=self.next_state
                self.darkness=255


            
    def keys_tick(self,keys):
        if keys[pygame.K_ESCAPE] and self.state_name=="game_find":
            self.darkness=-255
            self.next_state="main_menu"

        if self.state_name=="game_find" or self.state_name=="attack_time":
            if keys[pygame.K_w] and self.game.play_field.player_y>16:
                self.animation_tick+=10
                if not walk_channel.get_busy():
                    walk_channel.play(walk)
                self.game.play_field.player_y-=5
            if keys[pygame.K_s] and self.game.play_field.player_y<580:
                self.animation_tick+=10
                if not walk_channel.get_busy():
                    walk_channel.play(walk)
                self.game.play_field.player_y+=5
            if keys[pygame.K_a] and self.game.play_field.player_x>16:
                self.animation_tick+=10
                if not walk_channel.get_busy():
                    walk_channel.play(walk)
                self.game.play_field.player_x-=5
            if keys[pygame.K_d] and self.game.play_field.player_x<940:
                self.animation_tick+=10
                if not walk_channel.get_busy():
                    walk_channel.play(walk)
                self.game.play_field.player_x+=5

    def event_update(self,event):
        if event.type==pygame.MOUSEBUTTONUP and self.state_name=="game_find":
            x=self.game.play_field.player_x//50
            y=self.game.play_field.player_y//50
            for item in self.game.play_field.items:
                if item.x==x and item.y==y and item.lies:
                    item.lies=False
                    item_music.play()
                    if item.visual==0:
                        self.game.candles+=1
                    if item.visual==1:
                        self.game.crucifix=+1
                    if item.demon_item and random.choice([0,0,1])==1:
                        self.game.health-=1
                        self.state_time+=60
        elif event.type==pygame.MOUSEBUTTONUP and self.state_name=="main_menu":
            if self.game.night==0:
                self.next_state="one_night"
                self.darkness=-255
            else:
                self.next_state="game_find"
                self.darkness=-255
        elif event.type==pygame.MOUSEBUTTONUP and self.state_name=="one_night":
            self.next_state="game_find"
            self.darkness=-255
        