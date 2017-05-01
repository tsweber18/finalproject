from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class Nouns(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    homeworld = models.CharField(max_length=20)
    shipName = models.CharField(max_length=20)
    
        
class NounsForm(ModelForm):
    class Meta:
        model = Nouns
        fields = ['name','homeworld','shipName']