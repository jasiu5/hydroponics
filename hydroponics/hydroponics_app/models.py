from django.contrib.auth.models import User
from django.db import models


class HydroponicSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Measurement(models.Model):
    system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE, related_name="measurements")
    timestamp = models.DateTimeField(auto_now_add=True)
    ph = models.FloatField()
    temperature = models.FloatField()
    tds = models.FloatField()
