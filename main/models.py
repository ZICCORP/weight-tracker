from django.db import models
from users.models import CustomUser

class BodyWeight(models.Model):
    weight = models.PositiveIntegerField()
    date = models.DateField()
    owner = models.ForeignKey(CustomUser,models.CASCADE)
