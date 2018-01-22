"""Test intell."""

from django.test import TestCase

from getby.views import HomeView

from . import views, bugs


class ProfileTestCase(TestCase):
    """."""

    def setUp(self):
        """."""
        self.std_mtx = bugs.Matrix()
        self.md_mtx = bugs.Matrix(5)
        self.std_start = bugs.start()

    def test_home_view_has_title(self):
        """."""
        response = HomeView()
        assert response.template_name == 'getby/homepage.html'

    def test_intell_view_has_title(self):
        """."""
        response = views.index(self)
        assert response.content == b"Hello, world. You're at the intell index."

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
        mtx = bugs.start(bugs=1)
        res = mtx._bugs
        assert len(res) == 1

    def test_std_start_bug(self):
        """."""
        for _ in range(200):
            std_start = bugs.start()
            assert std_start._bugs[0][0] == 1

    def test_start_lots_o_times(self):
        """."""
        for _ in range(200):
            strt = bugs.start(bugs=15, size=10)
            assert len(strt.mtx) == 10

    def test_start_size_2_bug_index(self):
        """."""
        for _ in range(200):
            strt = bugs.start(size=2)
            assert strt._bugs[1][0] == 2

    def test_matrix_standard_bug_list(self):
        """."""
        res = self.std_start._bugs
        assert len(res) == 2

    def test_matrix_more_bugs_list(self):
        """."""
        mtx = bugs.start(bugs=4)
        res = mtx._bugs
        assert len(res) == 4

    def test_matrix_lots_o_bugs_list(self):
        """."""
        mtx = bugs.start(bugs=10)
        res = mtx._bugs
        assert len(res) == 10

    def test_matrix_tons_o_bugs_martix(self):
        """."""
        mtx = bugs.start(bugs=100)
        res = mtx.mtx
        assert len(res) == 18

    def test_matrix_lots_o_bugs_no_resize_matrix(self):
        """."""
        mtx = bugs.start(bugs=5, size=4)
        assert len(mtx.mtx) == 4

    def test_matrix_lots_o_bugs_resizes_matrix(self):
        """."""
        mtx = bugs.start(bugs=9)
        assert len(mtx.mtx) == 6

    def test_bug_idx_2x2(self):
        """."""
        mtx = bugs.start(size=2)
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
        mtx = bugs.start()
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
        mtx = bugs.start(size=10)
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
