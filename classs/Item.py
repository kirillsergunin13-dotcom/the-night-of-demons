import random
from ordinary_field import Field
from playing_field import PlayingField
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

class Items:
    items:list[list[Item]]
    def __init__(self,field:PlayingField):
        for candles in range(3):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if field[y][x]==1:
                    self.items.append(Item(0,x,y,False))
        for candles_demon in range(5):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if field[y][x]==4:
                    self.items.append(Item(0,x,y,True))
        for crucifix in range(2):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if field[y][x]==1:
                    self.items.append(Item(1,x,y,False))
        for crucifix_demon in range(3):
            flag=True
            while flag:
                x,y=random.choice(range(0,19)),random.choice(range(0,12))
                if field[y][x]==1:
                    self.items.append(Item(1,x,y,True))