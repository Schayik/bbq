from django.conf import settings
from django.db import models


class Event(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()


class Meat(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=100)


class Visitor(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    number_of_extra_guests = models.IntegerField()


class Quantity(models.Model):
    meat = models.ForeignKey(
        Meat,
        on_delete=models.CASCADE,
    )
    visitor = models.ForeignKey(
        Visitor,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()
