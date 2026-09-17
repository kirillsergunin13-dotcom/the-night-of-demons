from ordinary_field import Field
import random
from Item import Items
class PlayingField(Field):
    items:Items=[]
    def __init__(self):
        super().__init__()
        for i in len(self.room):
            for j in len(i):
                if self.room[i][j]==0 and random.choice(range(0,20))==20:
                    self.room[i][j]=4
        self.items=Items(self.room)
        