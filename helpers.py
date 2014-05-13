#Written by Ian Donovan
#Some functionality from Chimp tutorial
#see http://www.pygame.org/docs/tut/chimp/ChimpLineByLine.html

#Helper file; loads images and sounds.
import os, sys
import pygame
from pygame.locals import *

#This function loads an image and adjusts its background
def load_image(name, colorkey=None):
    #'data' is the folder in which the image is saved
    fullname = os.path.join('assets/sprites', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound:', wav)
        raise SystemExit
    return sound
