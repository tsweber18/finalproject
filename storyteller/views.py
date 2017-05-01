from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views import generic
from django.http import HttpResponseRedirect,Http404,HttpResponse
from .models import Nouns, NounsForm

def index(request):
    if request.POST:
        Nouns = NounsForm(request.POST)
        if Nouns.is_valid():
            Nouns.save()
    return render(request, 'storyteller/main.html', {'Nouns': Nouns})
    
def ship(request):
    a=Nouns.objects.get(pk=1)
    b=Nouns.objects.get(pk=2)
    c=Nouns.objects.get(pk=3)
    return render(request, 'storyteller/ship.html', {'a': a}, {'b': b}, {'c': c})