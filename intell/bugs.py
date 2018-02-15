"""Intelligent bugs."""

import random


class Bug(object):
    """Make a bug."""

    def __init__(self, id):
        """Set defaults."""
        self.id = id
        self.hungry = False
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
            # if bug is hungry and there is food
            if bug[1].hungry:
                bug[1]._get_food()
            # if bug[1].id == 1:  # For queen... #
            #     bug[1]._move_random()
            #     continue
            bug[1].rand_int = random.randrange(10)
            if len(bug[1].directions) > 1:
                bug[1]._get_together()
            elif len(bug[1].directions) == 1:
                move_to = bug[1].directions[0]
                self.mtx.mtx[bug[1].idx['x']][bug[1].idx['y']].remove(bug[1])
                self.mtx.mtx[move_to[0]][move_to[1]].append(bug[1])
                bug[1].idx['x'], bug[1].idx['y'] = move_to[0], move_to[1]
                self._directions()
                bug[1].count += 1
        # print(self.mtx._bugs[0][1].hungry)

    def _get_food(self):
        """Move towards food."""
        if self.mtx._food:
            food = self.mtx._food[0]
            move_to_x = food.idx['x']
            move_to_y = food.idx['y']
            move_to = []
            x = self.idx['x']
            y = self.idx['y']
            if x > move_to_x:
                move_to.append(x - 1)
            elif x < move_to_x:
                move_to.append(x + 1)
            elif x == move_to_x:
                move_to.append(x)
            if y > move_to_y:
                move_to.append(y - 1)
            elif y < move_to_y:
                move_to.append(y + 1)
            elif y == move_to_y:
                move_to.append(y)
            if move_to not in self.directions:
                self._move_random()
                return
            self.mtx.mtx[self.idx['x']][self.idx['y']].remove(self)
            self.mtx.mtx[move_to[0]][move_to[1]].append(self)
            self.idx['x'], self.idx['y'] = move_to[0], move_to[1]
            self._directions()
            self.count += 1

    def _get_together(self):
        """
        Have bugs move towards eachother and stay around eachother.

        Pick index to move to where the difference between
        sums is the least.
        """
        rand = random.randrange(len(self.mtx._bugs))
        rand_bug = self.mtx._bugs[rand]  # use rand if no queen 0 for queen #
        while rand_bug[1] == self:  # pragma no cover
            rand = random.randrange(len(self.mtx._bugs))
            rand_bug = self.mtx._bugs[rand]
        move_to_x = rand_bug[1].idx['x']
        move_to_y = rand_bug[1].idx['y']
        move_to = []
        x = self.idx['x']
        y = self.idx['y']
        if x > move_to_x:
            move_to.append(x - 1)
        elif x < move_to_x:
            move_to.append(x + 1)
        elif x == move_to_x:
            move_to.append(x)
        if y > move_to_y:
            move_to.append(y - 1)
        elif y < move_to_y:
            move_to.append(y + 1)
        elif y == move_to_y:
            move_to.append(y)
        if move_to not in self.directions:
            self._move_random()
            return

# >>>>>>v these methods will take the group into the four corners #
        # nums = []
        # if self.rand_int == 3 or self.rand_int == 9 or self.rand_int == 10:
        #     print('moving 0, 0', self.count)
        #     for idx in self.directions:  # move to 0, 0
        #         nums.append(idx[0] + idx[1] - move_towards)
        # elif self.rand_int == 1 or self.rand_int == 5 or self.rand_int == 7:
        #     print('moving 10, 10', self.count)
        #     for idx in self.directions:  # move to 10, 10
        #         nums.append(-(idx[0] + idx[1] - move_towards))
        # elif self.rand_int == 2:
        #     print('moving 0, 10', self.count)
        #     for idx in self.directions:  # move to 0, 10
        #         nums.append(move_towards - idx[0] + idx[1])
        # elif self.rand_int == 4 or self.rand_int == 6 or self.rand_int == 8:
        #     print('moving 10, 0', self.count)
        #     for idx in self.directions:  # move to 10, 0
        #         nums.append(abs(idx[0] + idx[1] - move_towards))
        # try:
        #     index_min = min(range(len(nums)), key=nums.__getitem__)
        # except:
        #     rand_idx = random.randrange(len(self.directions))
        #     index_min = rand_idx
        # now perform move #
        # move_to = self.directions[index_min]
# >>>>>>^ ######################################################

        self.mtx.mtx[self.idx['x']][self.idx['y']].remove(self)
        self.mtx.mtx[move_to[0]][move_to[1]].append(self)
        self.idx['x'], self.idx['y'] = move_to[0], move_to[1]
        self._directions()
        self.count += 1

    def _move_random(self):
        """
        Determine how bug is to perform.

        When called the matrix will be a part of the bug passed in...
        Choose random index to move to
        """
        try:
            rand_idx = random.randrange(len(self.directions))
        except:  # pragma no cover
            return
        move_to = self.directions[rand_idx]
        self.mtx.mtx[self.idx['x']][self.idx['y']].remove(self)
        self.mtx.mtx[move_to[0]][move_to[1]].append(self)
        self.idx['x'], self.idx['y'] = move_to[0], move_to[1]
        self._directions()
        self.count += 1

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

    def _hungry(self):
        """Make hungry true @ chosen interval."""
        if self.count % 50 == 0 and self.count > 0 and self.hungry is False:
            self.hungry = True
            return

    def _eat(self, food):
        """Food count decrement."""
        # x = self.idx['x']
        # y = self.idx['y']
        # fx = self.mtx._food[0].idx['x']
        # fy = self.mtx._food[0].idx['y']
        if self.hungry:
            self.hungry = False
            food._size -= 1
            food.size()

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
            # clear any previous directions #
            bug[1].directions = []
            x = bug[1].idx['x']
            y = bug[1].idx['y']
            self._pos_dir(bug, mtx, x, y)
            self._neg_dir(bug, mtx, x, y)
            bug[1]._hungry()

    def _pos_dir(self, bug, mtx, x, y):
        """Get positive directions."""
        try:
            if len(mtx[x][y + 1]) == 0:
                bug[1].directions.append([x, y + 1])
            elif len(mtx[x][y + 1]) == 1:
                if type(mtx[x][y + 1][0]).__name__ == 'Food':
                    bug[1]._eat(mtx[x][y + 1][0])
        except IndexError:
            pass
        try:
            if len(mtx[x + 1][y]) == 0:
                bug[1].directions.append([x + 1, y])
            elif len(mtx[x + 1][y]) == 1:
                if type(mtx[x + 1][y][0]).__name__ == 'Food':
                    bug[1]._eat(mtx[x + 1][y][0])
        except IndexError:
            pass
        try:
            if len(mtx[x + 1][y + 1]) == 0:
                bug[1].directions.append([x + 1, y + 1])
            elif len(mtx[x + 1][y + 1]) == 1:
                if type(mtx[x + 1][y + 1][0]).__name__ == 'Food':
                    bug[1]._eat(mtx[x + 1][y + 1][0])
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
            elif len(mtx[x - 1][y - 1]) == 1:
                if type(mtx[x - 1][y - 1][0]).__name__ == 'Food':
                    bug[1]._eat(mtx[x - 1][y - 1][0])

    def _neg_x(self, bug, mtx, x, y):
        """Get if trying to move x - 1."""
        try:
            if len(mtx[x - 1][y + 1]) == 0:
                bug[1].directions.append([x - 1, y + 1])
            elif len(mtx[x - 1][y + 1]) == 1:
                if type(mtx[x - 1][y + 1][0]).__name__ == 'Food':
                    bug[1]._eat(mtx[x - 1][y + 1][0])
        except IndexError:
            pass
        if len(mtx[x - 1][y]) == 0:
            bug[1].directions.append([x - 1, y])
        elif len(mtx[x - 1][y]) == 1:
            if type(mtx[x - 1][y][0]).__name__ == 'Food':
                bug[1]._eat(mtx[x - 1][y][0])

    def _neg_y(self, bug, mtx, x, y):
        """Get if trying to move y - 1."""
        try:
            if len(mtx[x + 1][y - 1]) == 0:
                bug[1].directions.append([x + 1, y - 1])
            elif len(mtx[x + 1][y - 1]) == 1:
                if type(mtx[x + 1][y - 1][0]).__name__ == 'Food':
                    bug[1]._eat(mtx[x + 1][y - 1][0])
        except IndexError:
            pass
        if len(mtx[x][y - 1]) == 0:
            bug[1].directions.append([x, y - 1])
        elif len(mtx[x][y - 1]) == 1:
            if type(mtx[x][y - 1][0]).__name__ == 'Food':
                bug[1]._eat(mtx[x][y - 1][0])
