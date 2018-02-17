"""."""

from django.shortcuts import render
from .models import start, feed
from django.views.decorators.csrf import csrf_protect
# from django.views.generic.base import TemplateView
from urllib.parse import parse_qs, urlparse
from django.shortcuts import redirect, reverse

MTX = start(9, 20)


@csrf_protect
def front_input(request):
    """."""
    res = parse_qs(urlparse(request.get_full_path()).query)
    bugs = int(res['bugs'][0])
    size = int(res['size'][0])
    MTX = start(bugs, size)
    res = request
    res.session['MTX'] = MTX
    # request['MTX'] = MTX
    return res
    # return render(request, 'getby/matrix.html', {
    #     'matrix': MTX.mtx,
    #     'bug': MTX._bugs[0][1].count,
    # })


@csrf_protect
def index(request):  # pragma no cover
    """."""
    # MTX = request.session['MTX']
    # import pdb; pdb.set_trace()
    MTX._bugs[0][1]._move_all_together()
    if request.method == 'POST':
        feed(MTX)
    return render(request, 'getby/matrix.html', {
        'matrix': MTX.mtx,
        'bug': MTX._bugs[0][1].count,
    })
