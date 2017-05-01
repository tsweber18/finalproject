from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views import generic
from django.http import HttpResponseRedirect,Http404,HttpResponse
from storyteller.models import Nouns, NounsForm

def index(request):
    if request.POST:
        form = NounsForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'storyteller/main.html')
    
def ship(request):
    list=Nouns.objects.all()
    a=list[0]
    b=list[1]
    c=list[2]
    context={
        'a': a,
        'b': b,
        'c': c,
    }
    return render(request, 'storyteller/ship.html', context)