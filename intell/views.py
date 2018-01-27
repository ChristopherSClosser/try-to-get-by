"""."""

from django.shortcuts import render
from .bugs import start

MTX = start(bugs=2, size=10)


def index(request):
    """."""
    if request.method == 'GET':
        MTX._bugs[0][1]._move_all_random()
        return render(request, 'getby/matrix.html', {'matrix': MTX.mtx})
