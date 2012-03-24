#Written by Ian Donovan
#Bullet class

import pygame
from pygame.locals import *
from helpers import *
from Constants import *

#Bullet class
class Bullet(pygame.sprite.Sprite):
    #The constructor takes in a parent rect.
    #This will be the ship -- the bullet will spawn on the ship
    def __init__(self, parent):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bulletSprite.png',-1)

        #Ensures the bullet is centered on the ship's center
        self.rect.center = parent.center
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.damage = 5*PLAYERLEVEL

        #Later, I'll add functionality to Level Up bullets.
        self.level = PLAYERLEVEL
        self.yMoveDist = BULLETYMOVE

    
