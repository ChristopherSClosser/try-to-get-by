"""."""

from django.shortcuts import render
from .models import start, feed
from django.views.generic.base import TemplateView
from urllib.parse import parse_qs, urlparse
from django.views.decorators.csrf import csrf_protect


MTX = start(9, 10)


@csrf_protect
def index(request):  # pragma no cover
    """."""
    MTX._bugs[0][1]._move_all_together()
    if request.method == 'POST':
        x = feed(MTX)
    return render(request, 'getby/matrix.html', {
        'matrix': MTX.mtx,
        'bug': MTX._bugs[0][1].count,
    })
