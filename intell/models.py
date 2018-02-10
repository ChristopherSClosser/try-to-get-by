from django.db import models
import random
import math
from intell.bugs import Bug


class Matrix(models.Model):
    """Make the grid."""

    def __init__(self, _size='small'):
        """."""
        self._bugs = []
        self._size = _size
        self._food = []
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


class Food(object):
    """Food instances."""

    def __init__(self, mtx, _size):
        """."""
        self._size = _size
        self.mtx = mtx


def feed(grid, size=5):
    """Operation for feeding. Standard is 5 feedings."""
    rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
    rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
    while grid.mtx[rand_idx1][rand_idx2]:
        rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
        rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
    new = Food(grid.mtx, size)
    grid.mtx[rand_idx1][rand_idx2].append(new)
    grid._food.append(new)


def start(bugs=2, size='small'):
    """
    Init matrix and bugs.

    A default matrix will look like this...
    [
      [[<intell.bugs.Bug object at 0x7f420e2e1c88>], [], []],
      [[<intell.bugs.Bug object at 0x7f420e2e1160>], [], []],
                                                [[], [], []],
    ]
    Bugs will be randomly placed.
    """
    grid = Matrix(size)
    mtx_size = len(grid.mtx) * len(grid.mtx)
    if bugs > int(math.ceil(mtx_size)) / 3:
        x = int(math.ceil((bugs * 3) ** (0.5)))
        grid = Matrix(x)
    for bug in range(bugs):
        rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
        rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
        while grid.mtx[rand_idx1][rand_idx2]:
            rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
            rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
        new = Bug(bug + 1)
        grid.mtx[rand_idx1][rand_idx2].append(new)
        grid._bugs.append((new.id, new))
        new._location(grid)  # get index of bug
    new._directions()  # get available directions all bugs can go
    return grid
