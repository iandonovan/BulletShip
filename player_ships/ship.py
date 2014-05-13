import pygame
import helpers
import bullets.bullet as bullet

#Battleship, controlled by the player.
class Ship(pygame.sprite.Sprite):

    X_MOVE_DIST = 10
    Y_MOVE_DIST = 10
    X_MOVE = 0
    Y_MOVE = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = helpers.load_image('base_ship.png', -1)

        #These are used in moving the sprite, keeping it on the screen
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        
        #Create the group of sprites; add to the group when L_SHIFT is pressed
        self.bullet_sprites = pygame.sprite.Group()

        #MoveDist is the number of pixels added to the move
        #Move is the total move distance, used on each update()
        self.xMoveDist = self.X_MOVE_DIST
        self.yMoveDist = self.Y_MOVE_DIST
        self.xMove = self.X_MOVE
        self.yMove = self.Y_MOVE

    #A key is pressed down; get the move ready
    def keyDown(self, key):
        if (key == K_RIGHT):
            #Increment the xMove
            self.xMove += self.xMoveDist
        elif (key == K_LEFT):
            #Decrement to move left
            self.xMove -= self.xMoveDist
        elif (key == K_DOWN):
            #Increase yMove to move down
            self.yMove += self.yMoveDist
        elif (key == K_UP):
            #Decrement to move up
            self.yMove -= self.yMoveDist
        elif (key == K_LSHIFT):
            #Fire a bullet
            self.makeBullet()

    #Upon letting up on a button, stop moving
    def keyUp(self, key):
        if (key == K_RIGHT or key == K_LEFT):
            self.xMove = 0
        elif (key == K_DOWN or key == K_UP):
            self.yMove = 0

    #Make a bullet, assign it to the ship's ammo, add it to the sprite group
    def makeBullet(self):
        self.bullet = Bullet(self.rect)
        self.bullet_sprites.add(self.bullet)

    def update(self):
        #This routine sees if the move is valid, ie, still on-screen
        new_position = self.rect.move(self.xMove, self.yMove)
        if not self.area.contains(new_position):
            if new_position.left < self.area.left or new_position.right > self.area.right:
                self.xMove = 0
            if new_position.top > self.area.top or new_position.bottom < self.area.bottom:
                self.yMove = 0
        #Actually moves the sprite
        self.rect.move_ip(self.xMove, self.yMove)

        #If there are bullets in the group
        if self.bullet_sprites.sprites():
            #For each one
            for shots in self.bullet_sprites:
                #If it moves out of bounds, remove it from the group
                bulletMove = self.bullet.rect.move(0, self.bullet.yMoveDist)
                if not self.area.contains(bulletMove):
                    self.bullet_sprites.remove(self.bullet)
                #Move it
                shots.rect.move_ip(0, self.bullet.yMoveDist)

    #Damage the player
    def damage(self, hurt):
        if self.health > 0:
            self.health -= hurt

    #Heal the player
    def heal(self, heal):
        if (self.health + heal <= self.maxHealth):
            self.health += heal
        else:
            self.health = self.maxHealth
