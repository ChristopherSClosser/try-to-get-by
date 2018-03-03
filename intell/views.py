"""."""

from django.shortcuts import render
from .models import start, feed
from django.views.decorators.csrf import csrf_protect
from urllib.parse import parse_qs, urlparse
from django.shortcuts import redirect, reverse

MTX = start(9, 18)


# @csrf_protect
# def front_input(request):  # pragma no cover
#     """."""
#     res = parse_qs(urlparse(request.get_full_path()).query)
#     bugs = int(res['bugs'][0])
#     size = int(res['size'][0])
#     MTX = start(bugs, size)
#     res = request
#     res.session['MTX'] = MTX
#     return res


@csrf_protect
def index(request):  # pragma no cover
    """."""
    if len(MTX._bugs) > 0:
        if request.method == 'POST':
            feed(MTX)
        bug = MTX._bugs[-1][1].count
        countdown = MTX._bugs[-1][1].countdown
        old_bug = MTX._bugs[0][1].count
        old_cd = MTX._bugs[0][1].countdown
        old_id = MTX._bugs[0][1].id
        young_bug = MTX._bugs[-1][1].id
        try:
            MTX._bugs[0][1]._move_all_together()
            bugs = len(MTX._bugs)
        except IndexError:
            return render(request, 'getby/matrix.html', {
                'matrix': MTX.mtx,
            })
        return render(request, 'getby/matrix.html', {
            'matrix': MTX.mtx,
            'bugs': bugs,
            'bug': bug,
            'old': old_bug,
            'oldid': old_id,
            'oldcd': old_cd,
            'young': young_bug,
            'cd': countdown,
        })
    elif len(MTX._bugs) == 0:
        return redirect(reverse('homenobugs'))
