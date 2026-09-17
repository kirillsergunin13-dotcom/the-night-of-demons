import random
class Field:
    room:list[list[int]]

    def __init__(self):
        self.room=[[random.choice([0,0,0,1,2]) for _ in range(0,19)] for _ in range(0,12)]