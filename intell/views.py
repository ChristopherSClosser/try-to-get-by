"""."""

from django.shortcuts import render
from .bugs import start
from django.views.generic.base import TemplateView
from urllib.parse import parse_qs, urlparse


# INC = 0
# if INC == 0:
MTX = start(9, 25)


def index(request):
    """."""
    # if INC == 0:
    #     res = parse_qs(urlparse(request.get_full_path()).query)
    #     bugs = int(res['bugs'][0])
    #     size = int(res['size'][0])
    #     MTX = start(bugs, size)
    #     INC += 1
    #     print(INC, 'should only see once')
    #     MTX._bugs[0][1]._move_all_together()
    #     return render(request, 'getby/matrix.html', {'matrix': MTX.mtx})
    # else:
    # try:
    #     res = parse_qs(urlparse(res).query)
    # except KeyError:
    #     return []
    # try:
    # res = request.get_full_path().split('/intell/?')
    # x = res[1].split('&')

    # import pdb; pdb.set_trace()

    # except:
    MTX._bugs[0][1]._move_all_together()
    return render(request, 'getby/matrix.html', {
        'matrix': MTX.mtx,
        'bug': MTX._bugs[0][1].count,
    })
