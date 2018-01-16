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

    def test_std_start_bug(self):
        """."""
        for _ in range(20):
            std_start = bugs.start()
            assert std_start._bugs[0].id == 1

    def test_start_size_2_bug_index(self):
        """."""
        for _ in range(20):
            strt = bugs.start(size=2)
            assert strt._bugs[1].id == 2

    # def test_bugs_index_1(self):
    #     """."""
    #     res = []
    #     bug =
    #     for subarray in self.std_start.mtx:
    #         for item in subarray:
    #             if len(item) > 0:
    #                 res.append(subarray.index(item))
    #     import pdb; pdb.set_trace()
    #     assert self.std_start._bugs[0].idx == res
