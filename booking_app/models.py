from django.db import models


# Create your models here.
class ConferenceRoom(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    room_capacity = models.PositiveIntegerField()
    projector = models.BooleanField(default=False)


