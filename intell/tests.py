"""Test intell."""

from django.test import TestCase

from getby.views import HomeView

from . import bugs, models

from django.test import Client

csrf_client = Client(enforce_csrf_checks=True)


class ProfileTestCase(TestCase):
    """."""

    def setUp(self):
        """."""
        self.std_mtx = models.Matrix()
        self.md_mtx = models.Matrix(5)
        self.std_start = models.start()
        self.sixbyten = models.start(6, 10)

    def test_home_view_has_title(self):
        """."""
        response = HomeView()
        assert response.template_name == 'getby/homepage.html'

    def test_intell_view_200(self):
        """."""
        c = Client()
        res = c.get('/intell/')
        assert res.status_code == 200

    def test_intell_view_has_title(self):
        """."""
        c = Client()
        res = c.get('/intell/')
        assert b'<title>The start</title>' in res.content

    def test_std_matrix_init_bugs(self):
        """test_std_matrix_init_bugs."""
        assert self.std_mtx._bugs == []

    def test_std_matrix_init_size(self):
        """."""
        assert self.std_mtx._size == 'small'

    def test_std_matrix_init_marix(self):
        """."""
        assert self.std_mtx.mtx == [
            [[], [], []],
            [[], [], []],
            [[], [], []],
        ]

    def test_md_matrix_init_size(self):
        """."""
        assert self.md_mtx._size == 5

    def test_feed_std_mtx(self):
        """."""
        models.feed(self.std_mtx)
        assert len(self.std_mtx._food) == 1

    def test_feed_6x10(self):
        """."""
        for _ in range(20):
            models.feed(self.sixbyten)
        assert len(self.sixbyten._food) == 20

    def test_mtx_move_all_random(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[0][0].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        new._move_all_random()
        idx = {'x': 0, 'y': 0}
        assert new.idx != idx

    def test_bug_directions_0_0(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[0][0].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert new.directions == [[0, 1], [1, 0], [1, 1]]

    def test_bug_directions_bug1_00_bug2_11(self):
        """."""
        bug1 = bugs.Bug(1)
        self.std_mtx.mtx[0][0].append(bug1)
        self.std_mtx._bugs.append((bug1.id, bug1))
        bug1._location(self.std_mtx)
        bug2 = bugs.Bug(2)
        self.std_mtx.mtx[1][1].append(bug2)
        self.std_mtx._bugs.append((bug2.id, bug2))
        bug2._location(self.std_mtx)
        bug2._directions()
        assert [0, 0] not in bug2.directions
        assert [1, 1] not in bug1.directions

    def test_bug_directions_0_1(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[0][1].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [
            [0, 0], [0, 2], [1, 0], [1, 1], [1, 2]
        ]

    def test_bug_directions_0_2(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[0][2].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [[0, 1], [1, 1], [1, 2]]

    def test_bug_directions_1_0(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[1][0].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [
            [0, 0], [0, 1], [1, 1], [2, 0], [2, 1]
        ]

    def test_bug_directions_1_1(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[1][1].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [
            [0, 0], [0, 1], [0, 2], [1, 0],
            [1, 2], [2, 0], [2, 1], [2, 2],
        ]
        assert [1, 1] not in new.directions

    def test_bug_directions_1_2(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[1][2].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [
            [0, 1], [0, 2], [1, 1], [2, 1], [2, 2]
        ]

    def test_bug_directions_2_0(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[2][0].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [[1, 0], [1, 1], [2, 1]]

    def test_bug_directions_2_1(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[2][1].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [
            [1, 0], [1, 1], [1, 2], [2, 0], [2, 2]
        ]

    def test_bug_directions_2_2(self):
        """."""
        new = bugs.Bug(1)
        self.std_mtx.mtx[2][2].append(new)
        self.std_mtx._bugs.append((new.id, new))
        new._location(self.std_mtx)
        new._directions()
        assert sorted(new.directions) == [[1, 1], [1, 2], [2, 1]]

    def test_md_matrix_init_marix(self):
        """."""
        assert self.md_mtx.mtx == [
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], []],
        ]

    def test_matrix_one_bug(self):
        """."""
        mtx = models.start(bugs=1)
        res = mtx._bugs
        assert len(res) == 1

    def test_std_start_bug(self):
        """."""
        for _ in range(200):
            std_start = models.start()
            assert std_start._bugs[0][0] == 1

    def test_start_lots_o_times(self):
        """."""
        for _ in range(200):
            strt = models.start(bugs=15, size=10)
            assert len(strt.mtx) == 10

    def test_start_size_2_bug_index(self):
        """."""
        for _ in range(200):
            strt = models.start(size=2)
            assert strt._bugs[1][0] == 2

    def test_matrix_standard_bug_list(self):
        """."""
        res = self.std_start._bugs
        assert len(res) == 2

    def test_matrix_more_bugs_list(self):
        """."""
        mtx = models.start(bugs=4)
        res = mtx._bugs
        assert len(res) == 4

    def test_matrix_lots_o_bugs_list(self):
        """."""
        mtx = models.start(bugs=10)
        res = mtx._bugs
        assert len(res) == 10

    def test_matrix_tons_o_bugs_martix(self):
        """."""
        mtx = models.start(bugs=100)
        res = mtx.mtx
        assert len(res) == 18

    def test_matrix_tons_o_bugs_move_together(self):
        """."""
        mtx = models.start(bugs=100)
        res = mtx.mtx
        for _ in range(40):
            mtx._bugs[0][1]._move_all_together()
        assert len(res) == 18

    def test_matrix_move_together_over_50(self):
        """."""
        mtx = models.start(bugs=5)
        for _ in range(100):
            mtx._bugs[0][1]._move_all_together()
        assert len(mtx._bugs) == 5

    def test_matrix_move_together_feed(self):
        """."""
        mtx = models.start(5, 10)
        models.feed(mtx)
        for _ in range(2000):
            if _ % 50 == 0:
                models.feed(mtx)
            mtx._bugs[0][1]._move_all_together()
        assert len(mtx._bugs) == 5

    def test_matrix_lots_o_bugs_no_resize_matrix(self):
        """."""
        mtx = models.start(bugs=5, size=4)
        assert len(mtx.mtx) == 4

    def test_matrix_lots_o_bugs_resizes_matrix(self):
        """."""
        mtx = models.start(bugs=9)
        assert len(mtx.mtx) == 6

    def test_bug_idx_2x2(self):
        """."""
        mtx = models.start(size=2)
        idx = []
        res = []
        for subarray in mtx.mtx:
            for i in range(len(subarray)):
                try:
                    if subarray[i][0]:
                        idx.append([
                            mtx.mtx.index(subarray),
                            i,
                        ])
                except IndexError:
                    continue
        for bug in mtx._bugs:
            res.append([
                bug[1].idx['x'],
                bug[1].idx['y'],
            ])
        res = sorted(res)
        assert idx == res

    def test_bug_idx_small(self):
        """."""
        mtx = models.start()
        idx = []
        res = []
        for subarray in mtx.mtx:
            for i in range(len(subarray)):
                try:
                    if subarray[i][0]:
                        idx.append([
                            mtx.mtx.index(subarray),
                            i,
                        ])
                except IndexError:
                    continue
        for bug in mtx._bugs:
            res.append([
                bug[1].idx['x'],
                bug[1].idx['y'],
            ])
        res = sorted(res)
        assert idx == res

    def test_bug_idx_larger(self):
        """."""
        mtx = models.start(size=10)
        idx = []
        res = []
        for subarray in mtx.mtx:
            for i in range(len(subarray)):
                try:
                    if subarray[i][0]:
                        idx.append([
                            mtx.mtx.index(subarray),
                            i,
                        ])
                except IndexError:
                    continue
        for bug in mtx._bugs:
            res.append([
                bug[1].idx['x'],
                bug[1].idx['y'],
            ])
        res = sorted(res)
        assert idx == res
