import pygame

eye=pygame.image.load("assets/images/eye.png")



def visual_choice_attack(attack:str,window,time:int):
    eye=pygame.image.load("assets/images/eye.png")
    red=(255,0,0, 128)
    attack_surface = pygame.Surface((1000, 1000), pygame.SRCALPHA)

    if attack=="linery_attack":
        pygame.draw.rect(attack_surface, red, pygame.Rect(0, 0, 1000, 250))
        window.blit(attack_surface, (0, 0))
        count=1
    elif attack=="table_attack":
        pygame.draw.rect(attack_surface, red, pygame.Rect(0, 0,1000, 1000))
        window.blit(attack_surface, (0, 0))
        count=2
    elif attack=="attack":
        pygame.draw.rect(attack_surface, red, pygame.Rect(250, 0, 250, 1000))
        window.blit(attack_surface, (0, 0))
        count=3
    elif attack=="right_attack":
        pygame.draw.rect(attack_surface, red, pygame.Rect(500, 0, 1000, 1000))
        window.blit(attack_surface, (0, 0))
        count=4
    elif attack=="left_attack":
        pygame.draw.rect(attack_surface, red, pygame.Rect(0, 0, 250, 1000))
        window.blit(attack_surface, (0, 0))
        count=5
    elif attack=="y_wall":
        pygame.draw.rect(attack_surface, red, pygame.Rect(0, 500, 1000, 1000))
        window.blit(attack_surface, (0, 0))
        count=6
    elif attack=="x_wall":
        count=7
    for attack in range(count):
        eye=pygame.transform.scale(eye,(50,((80-time)//3)))
        window.blit(eye,(270+(attack*60),10))