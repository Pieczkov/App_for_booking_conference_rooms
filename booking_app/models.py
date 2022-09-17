from django.db import models


"""Model representing conference rooms"""


class ConferenceRoom(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    room_capacity = models.PositiveIntegerField()
    projector = models.BooleanField(default=False)


"""Model representing conference room reservations for a given day"""


class RoomReservation(models.Model):
    date = models.DateField(auto_now=False)
    comment = models.TextField(null="no comment added")
    room_id = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)



