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
        self.moving = False
        self.directions = []

    def Move(self, mtx):  # pragma no cover
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
        """Location of bug in matrix."""
        self.mtx = mtx
        self.idx = []
        for subarray in self.mtx.mtx:
            if [self] in subarray:
                self.idx.append([
                    self.mtx.mtx.index(subarray),
                    subarray.index([self])
                ])

    def _directions(self, mtx):
        """Given the matrix find available directions to travel."""
        for bug in self.mtx._bugs:
            x = bug[1].idx[0][0]
            y = bug[1].idx[0][1]
            try:
                if len(mtx[x][y + 1]) == 0:
                    bug[1].directions.append([x, y + 1])
                if len(mtx[x + 1][y]) == 0:
                    bug[1].directions.append([x + 1, y])
                if len(mtx[x + 1][y + 1]) == 0:
                    bug[1].directions.append([x + 1, y + 1])
            except:
                pass
        import pdb; pdb.set_trace()


def start(bugs=2, size='small'):
    """
    Init matrix and bugs.

    A default matrix will look like this...
    [
      [[<intell.bugs.Bug object at 0x7f420e2e1c88>], [], []],
      [[<intell.bugs.Bug object at 0x7f420e2e1160>], [], []],
                                                [[], [], []]
    ]
    Of course bugs will be randomly placed.
    """
    grid = Matrix(size)
    if bugs > len(grid.mtx) / 2:
        grid = Matrix(bugs * 2)
    for bug in range(bugs):
        rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
        rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
        while grid.mtx[rand_idx1][rand_idx2]:
            rand_idx1 = random.randint(0, (len(grid.mtx) - 1))
            rand_idx2 = random.randint(0, (len(grid.mtx) - 1))
        new = Bug(bug + 1)
        grid.mtx[rand_idx1][rand_idx2].append(new)
        grid._bugs.append((new.id, new))
        new._location(grid)
    new._directions(grid.mtx)
    return grid


if __name__ == '__main__':  # pragma no cover
    res = start(size=15)
    for item in res.mtx:
        print(item, '\n')
