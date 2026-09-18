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
        self.night=0
        self.hardcor=hardcor
        self.field=[[random.choice([0 for _ in range(100)]+[1]) for _ in range(0,19)] for _ in range(0,12)]
        self.health=10
        if hardcor:
            self.health=1
            self.hardcor=True
        self.play_field=PlayingField(self.field)
        self.crucifix=0
    def update(self):
        for y in range(0,12):
            for x in range(0,19):
                if self.field[y][x]==3:
                    self.field[y][x]=0
        self.play_field.items.clear()

        self.health=2
        self.play_field=[]
        self.play_field=PlayingField(self.field)
        self.candles=0
        self.crucifix=self.crucifix-1
        self.night+=1
        if self.hardcor:
            print("!!!!!!!!!")
            self.health=1
            self.crucifix=0

    def class_to_json(self):
        return {"night":self.night,"field":self.field,"crucifix":self.crucifix,"hardcor":self.hardcor}

    def json_to_class(self,game):
        self.hardcor=game["hardcor"]
        self.night=game["night"]
        self.field=game["field"]
        self.crucifix=game["crucifix"]
        self.health=2
        self.play_field=PlayingField(self.field)
        
