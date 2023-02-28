class Player:
    def __init__(self, name, team, role_position, favourite_champ):
        self.name = name
        self.team = team
        self.role_position = role_position
        self.favourite_champ = favourite_champ


class Team:
    def __init__(self, name, players=None):
        self.name = name
        if players is None:
            self.players = []
        else:
            self.players = players

    def add_player(self, player):
        self.player.append(player)

    def remove_player(self, player):
        self.players.remove(player)
