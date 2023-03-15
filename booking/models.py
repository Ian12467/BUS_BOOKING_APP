from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Bus(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    # add more fields as needed


class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    # add more fields as needed


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # add more fields as needed

    # add more fields as needed
