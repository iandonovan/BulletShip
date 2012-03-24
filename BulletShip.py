#Written by Ian Donovan
#Space Invaders-style arcade shooter

import pygame
from pygame.locals import *
from Battleship import *
from Constants import *

if not pygame.font: print "Warning! Fonts disabled!"
if not pygame.mixer: print "Warning! Sounds disabled!"

#This is the actual game itself
class ShipAttack:
    def __init__(self):
        #Initialize pygame
        pygame.init()
        #Initialize window size -- these are in Constants.py
        self.width = WIDTH
        self.height = HEIGHT
        #Initialize screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Bullet Ship')
        pygame.mouse.set_visible(0)

    #Load up the sprites for the game
    #We load bullets when they're fired
    def loadSprites(self):
        #Build the object
        self.player = Battleship()
        #Group of sprites; can be a lone sprite -- may change.
        self.player_sprites = pygame.sprite.RenderPlain((self.player))

    #The game loop
    def gameLoop(self):
        self.loadSprites()

        #Send repeat keystrokes if the button is held down
        pygame.key.set_repeat(500, 250)

        #These variables are used for drawing sprites on the screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        #Only play as long as you're alive
        while (self.player.health > 0):
            #Get events
            for event in pygame.event.get():
                #If the user's quitting, quit
                if (event.type == pygame.QUIT):
                    sys.exit()
                #Check for keystrokes now
                #Pushing a key down (left, right, etc.)
                elif (event.type == KEYDOWN):
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)
                    or (event.key == K_TAB)
                    or (event.key == K_LSHIFT)):
                    #The function to handle the press
                        self.player.keyDown(event.key)
                #Letting a key up
                elif (event.type == KEYUP):
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                    #The function to handle the let-up
                        self.player.keyUp(event.key)
                        
            #Big update function -- mainly, move things around
            self.player.update()

            #Draw the sprites
            self.screen.blit(self.background, (0,0))
            self.player_sprites.draw(self.screen)
            
            #If there are bullets, draw them, too.
            if self.player.bullet_sprites.sprites():
                self.player.bullet_sprites.draw(self.screen)
            pygame.display.flip()

if __name__ == "__main__":
#Begin
    MainWindow = ShipAttack()
    MainWindow.gameLoop()
