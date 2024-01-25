from django.db import models

class Element(models.Model):
    name = models.TextField()
    symbol = models.CharField(max_length=3)
    atomic_number = models.IntegerField()
