"""Intelligent bugs."""

import random
import math


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
        self.moving = False
        self.directions = []

    def _move(self, mtx):  # pragma no cover
        """
        Determine how bug is to perform.

        When called bug will be a part of the matrix passed in...
        Bug needs to know where it can move ie. N, NE, E, SE, S, SW, W, NW
        ...cannot move in negative index direction
        [
          [[], [], []],  > if bug1 is @ mtx[0][0] - directions = [E, SE, S]
          [[], [], []],    if bug2 @ mtx[0][1] bug1 directions = [SE, S] ect..
          [[], [], []],  > if bug1 is @ mtx[0][2] - directions = [W, SW, S]
        ]                  if bug2 @ mtx[0][1] bug1 directions = [SW, S] ect..
        """
        pass

    def _location(self, mtx):
        """
        Location of bug in matrix.

        Gives bug the reference of Matrix object in which it lives.
        Initiated by start(no. of bugs, size of matrix)...
        """
        self.mtx = mtx
        self.idx = {}
        for subarray in self.mtx.mtx:
            if [self] in subarray:
                self.idx['x'] = self.mtx.mtx.index(subarray)
                self.idx['y'] = subarray.index([self])

    def _directions(self):
        """
        Given the matrix find available directions to travel.

        Each time all bugs get new directions.
        First initiated by start...
        """
        mtx = self.mtx.mtx
        for bug in self.mtx._bugs:
            # clear any previous directions
            bug[1].directions = []
            x = bug[1].idx['x']
            y = bug[1].idx['y']
            try:  # seems everything needs a try...
                if len(mtx[x][y + 1]) == 0:
                    bug[1].directions.append([x, y + 1])
            except IndexError:
                pass
            try:
                if len(mtx[x + 1][y]) == 0:
                    bug[1].directions.append([x + 1, y])
            except IndexError:
                pass
            try:
                if len(mtx[x + 1][y + 1]) == 0:
                    bug[1].directions.append([x + 1, y + 1])
            except IndexError:
                pass
            if x > 0:
                try:
                    if len(mtx[x - 1][y + 1]) == 0:
                        bug[1].directions.append([x - 1, y + 1])
                except IndexError:
                    pass
                if len(mtx[x - 1][y]) == 0:
                    bug[1].directions.append([x - 1, y])
            if y > 0:
                try:
                    if len(mtx[x + 1][y - 1]) == 0:
                        bug[1].directions.append([x + 1, y - 1])
                except IndexError:
                    pass
                if len(mtx[x][y - 1]) == 0:
                    bug[1].directions.append([x, y - 1])
            if x > 0 and y > 0:
                if len(mtx[x - 1][y - 1]) == 0:
                    bug[1].directions.append([x - 1, y - 1])


def start(bugs=2, size='small'):
    """
    Init matrix and bugs.

    A default matrix will look like this...
    [
      [[<intell.bugs.Bug object at 0x7f420e2e1c88>], [], []],
      [[<intell.bugs.Bug object at 0x7f420e2e1160>], [], []],
                                                [[], [], []]
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
    new._directions()  # get available directions bug can go
    return grid


if __name__ == '__main__':  # pragma no cover
    res = start(size=15)
    for item in res.mtx:
        print(item, '\n')
