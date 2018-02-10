"""."""

from django.shortcuts import render
from .models import start
from django.views.generic.base import TemplateView
from urllib.parse import parse_qs, urlparse


MTX = start(9, 10)


def index(request):  # pragma no cover
    """."""
    MTX._bugs[0][1]._move_all_together()
    return render(request, 'getby/matrix.html', {
        'matrix': MTX.mtx,
        'bug': MTX._bugs[0][1].count,
    })
