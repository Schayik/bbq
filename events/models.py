from django.conf import settings
from django.db import models


class Event(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Meat(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Visitor(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    number_of_extra_guests = models.IntegerField()

    def __str__(self):
        return self.name


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

    def __str__(self):
        return (
            'Visitor: ' + self.visitor.name +
            ', meat: ' + self.meat.type +
            ', quantity: ' + str(self.quantity)
        )
