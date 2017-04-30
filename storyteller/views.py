from django.shortcuts import render
from django.template import loader
from django.views import generic
from django.http import HttpResponseRedirect,Http404,HttpResponse
from .models import Nouns

def index(request):
    return render(request, 'storyteller/main.html')
    