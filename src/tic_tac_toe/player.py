class Player:
    def __init__(self, nickname):
        self._nickname = nickname
        self._weapon = None
        self._games = []

    @property
    def get_nickname(self):
        return self._nickname

    def __repr__(self):
        return f'<Player: {self._nickname}>'
