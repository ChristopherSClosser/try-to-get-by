"""Intelligent bugs."""


class Matrix(object):
    """Make the grid."""

    def __init__(self, _size='small'):
        """."""
        self._bugs = []
        self._size = _size
        self.mtx = [
            [[], [], []],
            [[], [], []],
            [[], [], []],
        ]
        if _size != 'small':
            self.mtx = []
            for i in range(_size):
                self.mtx.append([])
                for _ in range(_size):
                    self.mtx[i].append([])


class Bug(object):
    """Make a bug."""

    def __init__(self):
        """."""
        self.position = None
        self.moving = False
        self.direction = ''
        self.space = None


def start(bugs=2, size='small'):
    """."""
    pass


if __name__ == '__main__':
    res = Matrix(10)
    for item in res.mtx:
        print(item, '\n')
