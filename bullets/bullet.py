import pygame
from pygame.locals import *
from helpers import *

#Bullet class
class Bullet(pygame.sprite.Sprite):
    Y_SPEED = -20
    # This refers more to the bullet level, which I have to flesh out
    BULLET_LEVEL = 1

    # Parent will be the ship -- the bullet will spawn on the ship
    def __init__(self, parent):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bullet.png',-1)

        # Ensures the bullet is centered on the ship's center
        self.rect.center = parent.center
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.damage = 5*self.BULLET_LEVEL

        # Later, I'll add functionality to Level Up bullets.
        self.level = self.BULLET_LEVEL
        self.yMoveDist = self.Y_SPEED

    
