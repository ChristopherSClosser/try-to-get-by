"""Intelligent bugs."""

import random


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

    def __init__(self, id):
        """."""
        self.id = id
        self.position = None
        self.moving = False
        self.direction = ''
        self.space = None


def start(bugs=2, size='small'):
    """."""
    grid = Matrix(size)
    for bug in range(bugs):
        rand_idx = random.randint(0, len(grid.mtx))
        grid.mtx[rand_idx][rand_idx].append(Bug(bug))
    return grid


if __name__ == '__main__':
    res = start()
    for item in res.mtx:
        print(item, '\n')
