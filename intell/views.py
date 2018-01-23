"""."""

from django.shortcuts import render
from django.http import HttpResponse
from .bugs import start


def index(request):
    """."""
    mtx = start(size=10)
    return render(request, 'getby/matrix.html', {'matrix': mtx.mtx})
