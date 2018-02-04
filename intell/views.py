"""."""

from django.shortcuts import render
from .bugs import start


MTX = start(9, 25)


def index(request):
    """."""
    MTX._bugs[0][1]._move_all_together()
    return render(request, 'getby/matrix.html', {'matrix': MTX.mtx})
