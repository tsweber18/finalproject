from __future__ import unicode_literals

from django.db import models

class Nouns(models.Model):
    name = models.CharField(max_length=20)
    homeworld = models.CharField(max_length=20)
    shipName = models.CharField(max_length=20)
    def __str__(self):
        return self.name
        
