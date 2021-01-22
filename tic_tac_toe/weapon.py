from .utils import Colors


class Weapon:
    name = None

    def __str__(self):
        return self.name

    def __repr__(self):
        cls = type(self)
        return f'<Weapon {cls.__name__}>'


class Tic(Weapon):
    name = 'x'


class Tac(Weapon):
    name = 'o'


class Empty(Weapon):
    name = '.'

    def __bool__(self):
        return False


class Staff(Weapon):
    def __init__(self, name):
        self.name = Colors.bold(name)
