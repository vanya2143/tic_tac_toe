class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Weapon:
    name = None

    def to_green(self):
        return f'{Colors.OKGREEN}{self.name}{Colors.ENDC}'

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
