from django.db import models

class BodyWeight(models.Model):
    weight = models.IntegerField()
    date = models.DateField(auto_now_add=True,unique=True)
