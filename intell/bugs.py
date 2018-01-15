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
        """Set defaults."""
        self.id = id
        self.position = None
        self.moving = False
        self.directions = []
        self.space = None

    def Move(self, mtx):
        """
        Determine how bug is to perform.

        When called bug will be a part of the matrix passed in...
        Bug needs to know where it can move ie. N, NE, E, SE, S, SW, W, NW
        ...cannot move in negative index direction
        [
            [[], [], []],  >if bug1 is @ mtx[0][0] - directions = [E, SE, S]
            [[], [], []],   if bug2 @ mtx[0][1] bug1 directions = [SE, S] ect..
            [[], [], []],  >if bug1 is @ mtx[0][2] - directions = [W, SW, S]
        ]                   if bug2 @ mtx[0][1] bug1 directions = [SW, S] ect..
        """

    def location(self, mtx):
        """Location of bug in matrix."""
        self.mtx = mtx
        self.idx = []
        for subarray in self.mtx:
            if [self.id] in subarray:
                self.idx.append((self.mtx.index(subarray), subarray.index([self.id])))
        pass


def start(bugs=2, size='small'):
    """."""
    grid = Matrix(size)
    for bug in range(bugs):
        rand_idx = random.randint(0, len(grid.mtx))
        new = Bug(bug)
        grid.mtx[rand_idx][rand_idx].append(new.id)
        new.location(grid.mtx)
        import pdb; pdb.set_trace()
    return grid


if __name__ == '__main__':
    res = start()
    for item in res.mtx:
        print(item, '\n')
