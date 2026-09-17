import random


class Item:
    visual:int
    x:int
    y:int
    demon_item:bool
    def __init__(self,variant,x,y,demon_item):
        self.visual=variant
        self.x=x
        self.y=y
        self.demon_item=demon_item

class PlayingField:
    play_room:list
    items:list[Item]=[]
    def __init__(self,play_field:list):
        start_room=play_field
        for i in range(0,12):
            for j in range(0,19):
                if start_room[i][j]==0 and random.choice(range(0,17))==0:
                    start_room[i][j]=3
        self.play_room=list(start_room)
        for candles in range(3):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if start_room[y][x]==1:
                    self.items.append(Item(0,x,y,False))
                    flag=False

        for candles_demon in range(5):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if start_room[y][x]==3:
                    self.items.append(Item(0,x,y,True))
                    flag=False
        for crucifix in range(2):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if start_room[y][x]==1:
                    self.items.append(Item(1,x,y,False))
                    flag=False
        for crucifix_demon in range(3):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if start_room[y][x]==3:
                    self.items.append(Item(1,x,y,True))
                    flag=False
    