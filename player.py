import bullets.basic_bullet as basic_bullet
import player_ships.basic_ship as basic_ship

class Player:

    X_MOVE = 10
    Y_MOVE = 10
    MAX_HEALTH = 100

    def __init__(self):
        self.health = MAX_HEALTH
        self.x_move = X_MOVE
        self.y_move = Y_MOVE
        self.level = 1
        self.ship = basic_ship.Battleship
        self.bullet = basic_bullet.BasicBullet

    def level_up(self):
        # do some things, increment
