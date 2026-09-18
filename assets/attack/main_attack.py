import pygame
import random



def attack_choice(count:int):
    if count>=100:
        attack=random.choice(range(2))
        if attack==2:
            return "x_wall"
        elif attack ==0:
            return "y_wall"
    if count>=50:
        attack=random.choice(range(4))
        if attack==0:
            return "left_attack"
        elif attack==1:
            return "right_attack"
        elif attack==2:
            return "attack"
    if count>=10 and random.choice([True,False]):
        return "table_attack"
    else:
        return "linery_attack"