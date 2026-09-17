from classs.playing_field import *


class GameState:
    night:int = 1
    candles:int = 0
    crucifix:int = 0
    health:int
    field:list
    play_field:PlayingField
    hardcor:bool

    def __init__(self,hardcor:bool=False):
        self.hardcor=hardcor
        self.field=[[random.choice([0,0,0,0,0,0,0,0,1,2]) for _ in range(0,19)] for _ in range(0,12)]
        self.health=2
        if hardcor:
            self.health=1
            self.hardcor=True
        self.play_field=PlayingField(self.field)
    def update(self):
        for y in range(0,12):
            for x in range(0,19):
                if self.field[y][x]==3:
                    self.field[y][x]=0
        self.play_field.items.clear()

        self.health=2
        self.play_field=[]
        print(self.play_field)
        self.play_field=PlayingField(self.field)
        self.candles=0
        self.crucifix-=1
        self.night+=1
        if self.hardcor:
            self.health=1
            self.crucifix=0
