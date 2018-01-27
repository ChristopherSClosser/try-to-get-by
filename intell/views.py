"""."""

from django.shortcuts import render
from django.http import HttpResponse
from .bugs import start
from django.views.generic import TemplateView

MTX = start(size=10)


def index(request):
    """."""
    if request.method == 'GET':
        MTX._bugs[0][1]._move_all_random()
        return render(request, 'getby/matrix.html', {'matrix': MTX.mtx})
