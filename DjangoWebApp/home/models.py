"""
Home App Models
These are the models I have created for use within the home app
L. McConnell - November 2020
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class timeUsage(models.Model):
    """
    This is the model used to store instances of time usage
    """
    id              = models.PositiveIntegerField(primary_key=True)
    activity        = models.CharField(max_length=60)
    startTime       = models.DateTimeField()
    endTime         = models.DateTimeField()
    duration        = models.DurationField()
    note            = models.CharField(max_length=240)
    tag             = models.CharField(max_length=60)
    author          = models.ForeignKey(User, on_delete=models.CASCADE, default=-1) #if a user is deleted, delete their time usage as well

    def __str__(self):
        return f'Time Entry {self.id}'
