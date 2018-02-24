"""Matrix and food classes."""

from django.db import models
import random
import math
from intell.bugs import Bug


class Matrix(models.Model):
    """Make the grid."""

    def __init__(self, _size='small', *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)
        self._bugs = []
        self.count = 0
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

    def _location(self):
        """
        Location of food in matrix[i][i].

        Gives food the reference of Matrix object in which it lives.
        Initiated by feed(mtx, size of food)...
        """
        self.idx = {}
        for subarray in self.mtx.mtx:
            if [self] in subarray:
                self.idx['x'] = self.mtx.mtx.index(subarray)
                self.idx['y'] = subarray.index([self])

    def size(self):
        """."""
        if self._size <= 0:
            self.mtx.mtx[self.idx['x']][self.idx['y']].remove(self)
            self.mtx._food.remove(self)


def feed(grid, size=10):
    """
    Operation for feeding. Standard is 5 feedings.

    A default matrix will look like this...
    [
      [[<intell.models.Food object at 0x7f420e2e1c88>], [], []],
                                                   [[], [], []],
                                                   [[], [], []],
    ]
    Food will be randomly placed.
    """
    for _ in range(2):
        rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
        rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
        while grid.mtx[rand_idx1][rand_idx2]:
            rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
            rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
        new = Food(grid, size)
        grid.mtx[rand_idx1][rand_idx2].append(new)
        new.fid = len(grid._food)
        grid._food.append(new)
        new._location()


def start(bugs=3, size='small'):
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
