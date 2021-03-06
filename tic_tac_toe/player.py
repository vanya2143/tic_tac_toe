class Player:
    """ Class  for create a player object """

    def __init__(self, nickname):
        self._nickname = nickname
        self._games = []

    @property
    def nickname(self):
        return self._nickname

    def __repr__(self):
        return f'<Player: {self._nickname}>'
