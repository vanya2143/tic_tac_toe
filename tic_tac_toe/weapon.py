from .utils import Colors


class Weapon:
    name = None

    def __str__(self):
        return f'{Colors.WHITE}{self.name}{Colors.ENDC}'

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
