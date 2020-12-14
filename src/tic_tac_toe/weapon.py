class Weapon:
    name = None

    def __str__(self):
        return self.name

    def __repr__(self):
        cls = type(self)
        return f'<Weapon {cls.__name__}>'


class Tic(Weapon):
    name = 'tik'


class Toc(Weapon):
    name = 'tok'


class Empty(Weapon):
    name = 'empty'

