class GameStats():

    def __init__(self):
        self.ship_limit = 3
        self.game_active = True
        self.reset_stats()


    def reset_stats(self):
        self.ships_left = self.ship_limit
