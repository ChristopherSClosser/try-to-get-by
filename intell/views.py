"""."""

from django.shortcuts import render
from .bugs import start

MTX = start(bugs=9, size=20)


def index(request):
    """."""
    MTX._bugs[0][1]._move_all_together()
    return render(request, 'getby/matrix.html', {'matrix': MTX.mtx})
