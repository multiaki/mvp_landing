from django.shortcuts import render_to_response, RequestContext

from .models import Join
from .forms import JoinForm


def home(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
    return render_to_response('join/home.html', locals(), context_instance=RequestContext(request))