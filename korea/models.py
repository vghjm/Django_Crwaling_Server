from django.db import models

class Bob(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    image = models.CharField(max_length=2000)