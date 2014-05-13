import pygame
import pygame.locals
import player
pygame.init()

if not pygame.font: print("Warning! Fonts disabled!")
if not pygame.mixer: print("Warning! Sounds disabled!")

class BulletShip:

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.width = self.WIDTH
        self.height = self.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.key.set_repeat(500, 250)

    def set_background(self):
        pygame.display.set_caption('Bullet Ship')
        pygame.mouse.set_visible(0)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

    def set_player(self):
        self.player = player.Player()
        self.player_sprites = pygame.sprite.RenderPlain(self.player.ship)

    # The game loop
    def gameLoop(self):
        # Only play as long as you're alive
        while (self.player.health > 0):
            # Get events
            for event in pygame.event.get():
                # If the user's quitting, quit
                if (event.type == pygame.QUIT):
                    sys.exit()
                # Check for keystrokes now
                # Pushing a key down (left, right, etc.)
                elif (event.type == pygame.KEYDOWN):
                    if ((event.key == pygame.K_RIGHT)
                    or (event.key == pygame.K_LEFT)
                    or (event.key == pygame.K_UP)
                    or (event.key == pygame.K_DOWN)
                    or (event.key == pygame.K_TAB)
                    or (event.key == pygame.K_LSHIFT)):
                    # The function to handle the press
                        self.player.keyDown(event.key)
                # Letting a key up
                elif (event.type == pygame.KEYUP):
                    if ((event.key == pygame.K_RIGHT)
                    or (event.key == pygame.K_LEFT)
                    or (event.key == pygame.K_UP)
                    or (event.key == pygame.K_DOWN)):
                    # The function to handle the let-up
                        self.player.keyUp(event.key)
                        
            # Big update function -- mainly, move things around
            self.player.ship.update()

            # Draw the sprites
            self.screen.blit(self.background, (0,0))
            self.player_sprites.draw(self.screen)
            
            # If there are bullets, draw them, too.
            if self.player.ship.bullet_sprites.sprites():
                self.player.ship.bullet_sprites.draw(self.screen)
            pygame.display.flip()

if __name__ == "__main__":
#Begin
    main_window = BulletShip()
    main_window.set_background()
    main_window.set_player()
    main_window.gameLoop()
