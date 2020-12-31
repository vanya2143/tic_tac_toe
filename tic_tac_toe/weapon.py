class Colors:
    GREEN = '\033[92m'
    DEFAULT = '\033[0m'


class Weapon:
    name = None
    colors = Colors
    current_color = colors.DEFAULT

    def to_green(self):
        self.current_color = self.colors.GREEN

    def __str__(self):
        return f'{self.current_color}{self.name}{self.colors.DEFAULT}'

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
