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

    def _move_all_random(self):
        """For each bug call to move random."""
        for bug in self.mtx._bugs:
            bug[1]._move_random()

    def _move_all_together(self):
        """For each bug call move together."""
        for bug in self.mtx._bugs:
            bug[1]._get_together()

    def _get_together(self):
        """
        Have bugs move towards eachother and stay around eachother.

        Pick index to move to where the difference between
        sums is the least.
        """
        rand_bug = random.randrange(len(self.mtx._bugs))
        move_towards = rand_bug[1].idx['x'] + rand_bug[1].idx['y']
        nums = []
        for idx in sorted(self.directions):
            nums.append(idx[0] + idx[1] - move_towards)
        index_min = min(xrange(len(nums)), key=nums.__getitem__)

    def _move_random(self):
        """
        Determine how bug is to perform.

        When called the matrix will be a part of the bug passed in...
        Choose random index to move to
        """
        rand_idx = random.randint(0, (len(self.directions) - 1))
        move_to = self.directions[rand_idx]
        self.mtx.mtx[self.idx['x']][self.idx['y']].remove(self)
        self.mtx.mtx[move_to[0]][move_to[1]].append(self)
        self.idx['x'], self.idx['y'] = move_to[0], move_to[1]
        self._directions()

    def _location(self, mtx):
        """
        Location of bug in matrix[i][i].

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
        Bug needs to know where it can move ie. N, NE, E, SE, S, SW, W, NW
        ...cannot move in negative index direction
        [
          [[], [], []],  > if bug1 is @ mtx[0][0] - directions = [E, SE, S]
          [[], [], []],    if bug2 @ mtx[0][1] bug1 directions = [SE, S] ect..
          [[], [], []],  > if bug1 is @ mtx[0][2] - directions = [W, SW, S]
        ]                  if bug2 @ mtx[0][1] bug1 directions = [SW, S] ect..
        """
        mtx = self.mtx.mtx
        for bug in self.mtx._bugs:
            # clear any previous directions
            bug[1].directions = []
            x = bug[1].idx['x']
            y = bug[1].idx['y']
            self._pos_dir(bug, mtx, x, y)
            self._neg_dir(bug, mtx, x, y)

    def _pos_dir(self, bug, mtx, x, y):
        """Get positive directions."""
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

    def _neg_dir(self, bug, mtx, x, y):
        """Get negative directions."""
        if x > 0:
            self._neg_x(bug, mtx, x, y)
        if y > 0:
            self._neg_y(bug, mtx, x, y)
        if x > 0 and y > 0:
            if len(mtx[x - 1][y - 1]) == 0:
                bug[1].directions.append([x - 1, y - 1])

    def _neg_x(self, bug, mtx, x, y):
        """Get if trying to move x - 1."""
        try:
            if len(mtx[x - 1][y + 1]) == 0:
                bug[1].directions.append([x - 1, y + 1])
        except IndexError:
            pass
        if len(mtx[x - 1][y]) == 0:
            bug[1].directions.append([x - 1, y])

    def _neg_y(self, bug, mtx, x, y):
        """Get if trying to move y - 1."""
        try:
            if len(mtx[x + 1][y - 1]) == 0:
                bug[1].directions.append([x + 1, y - 1])
        except IndexError:
            pass
        if len(mtx[x][y - 1]) == 0:
            bug[1].directions.append([x, y - 1])


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


if __name__ == '__main__':  # pragma no cover
    res = start(size=15)
    for item in res.mtx:
        print(item, '\n')
