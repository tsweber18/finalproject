from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class Nouns(models.Model):
    name = models.CharField(max_length=20)
    homeworld = models.CharField(max_length=20)
    shipName = models.CharField(max_length=20)
    def __str__(self):
        return self.name
        
class NounsForm(ModelForm):
    model=Nouns
    fields = ['name','homeworld','shipName']