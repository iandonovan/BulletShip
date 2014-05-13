import bullets.bullet as bullet
import player_ships.ship as ship

class Player:

    STARTING_LEVEL = 1
    MAX_HEALTH = 100

    def __init__(self):
        self.health = self.MAX_HEALTH
        self.level = self.STARTING_LEVEL
        self.ship = ship.Ship()
        self.bullet = bullet.Bullet(self.ship.rect)

    # def level_up(self):
        # do some things, increment
