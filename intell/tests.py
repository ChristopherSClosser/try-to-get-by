"""Test intell."""

from django.test import TestCase

from getby.views import HomeView

from . import views


class ProfileTestCase(TestCase):
    """."""

    def setUp(self):
        """."""

    def test_home_view_has_title(self):
        """."""
        response = HomeView()
        assert response.template_name == 'getby/homepage.html'

    def test_intell_view_has_title(self):
        """."""
        response = views.index(self)
        assert response.content == b"Hello, world. You're at the intell index."
