from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Class for the home view."""

    template_name = 'getby/homepage.html'
