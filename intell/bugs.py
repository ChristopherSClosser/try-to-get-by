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
        self.count = 0
        self.rand_int = 0

    def _move_all_random(self):
        """For each bug call to move random."""
        for bug in self.mtx._bugs:
            bug[1]._move_random()

    def _move_all_together(self):
        """For each bug call move together."""
        for bug in self.mtx._bugs:
            bug[1].rand_int = random.randrange(8)
            if len(bug[1].directions) > 1:
                # if prime(self.count):  # adding some randomness #
                #     bug[1]._move_random()
                #     self.count += 1
                #     continue
                bug[1]._get_together()
            elif len(bug[1].directions) == 1:
                move_to = bug[1].directions[0]
                self.mtx.mtx[bug[1].idx['x']][bug[1].idx['y']].remove(bug[1])
                self.mtx.mtx[move_to[0]][move_to[1]].append(bug[1])
                bug[1].idx['x'], bug[1].idx['y'] = move_to[0], move_to[1]
                self._directions()
                bug[1].count += 1

    def _get_together(self):
        """
        Have bugs move towards eachother and stay around eachother.

        Pick index to move to where the difference between
        sums is the least.
        """
        rand = random.randrange(len(self.mtx._bugs))
        rand_bug = self.mtx._bugs[rand]
        while rand_bug[1] == self:
            rand = random.randrange(len(self.mtx._bugs))
            rand_bug = self.mtx._bugs[rand]
        move_towards = rand_bug[1].idx['x'] + rand_bug[1].idx['y']
        nums = []
        if self.count < 50:
            for idx in self.directions:  # they only move to 0,0 or 10,10
                # if (idx[0] + idx[1]) < move_towards:
                nums.append((idx[0] + idx[1]) - move_towards)
                # else:
                #     nums.append(move_towards - (idx[0] + idx[1]))
        else:
            if self.rand_int == 3 or self.rand_int == 8 or self.rand_int == 6:
                print('moving 0, 0', self.count)
                for idx in self.directions:  # move to 0, 0
                    nums.append(idx[0] + idx[1] - move_towards)
            elif self.rand_int == 1 or self.rand_int == 7:
                print('moving 10, 10', self.count)
                for idx in self.directions:  # move to 10, 10
                    nums.append(-(idx[0] + idx[1] - move_towards))
            elif self.rand_int == 2:
                print('moving 0, 10', self.count)
                for idx in self.directions:  # move to 0, 10
                    nums.append(move_towards - idx[0] + idx[1])
            elif self.rand_int == 4 or self.rand_int == 5:
                print('moving 10, 0', self.count)
                for idx in self.directions:  # move to 10, 0
                    nums.append(abs(idx[0] + idx[1] - move_towards))
        try:
            index_min = min(range(len(nums)), key=nums.__getitem__)
        except:
            rand_idx = random.randrange(len(self.directions))
            index_min = rand_idx
        # now perform move
        move_to = self.directions[index_min]
        self.mtx.mtx[self.idx['x']][self.idx['y']].remove(self)
        self.mtx.mtx[move_to[0]][move_to[1]].append(self)
        self.idx['x'], self.idx['y'] = move_to[0], move_to[1]
        self._directions()
        # print(self.count)
        self.count += 1

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


def prime(x):
    """Prime number function."""
    # check that number is greater than 0
    if x > 0:
        for i in range(2, x + 1):
            # check that only x and 1 can evenly divide x
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':  # pragma no cover
    res = start(size=15)
    for item in res.mtx:
        print(item, '\n')
