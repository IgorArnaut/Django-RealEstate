from django.db import models

# Create your models here.
STATE_CHOICES = {
    "OG": "ORIGINAL",
    "NE": "NEW",
    "RE": "RENOVATED",
    "LU": "LUX"
}


FURNISHING_CHOICES = {
    "FU": "FURNISHED",
    "SF": "SEMI_FURNISHED",
    "EM": "EMPTY"
}


HEATING_CHOICES = {
    "DH": "DISTRICT",
    "FH": "FLOOR",
    "SH": "STORAGE_HEATER",
    "GA": "GAS",
    "TS": "TILED_STOVE",
    "HP": "HEAT_PUMP"
}


class Apartment(models.Model):
    numOfRooms = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    story = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default="OG")
    furnishing = models.CharField(max_length=2, choices=FURNISHING_CHOICES, default="FU")
    heating = models.CharField(max_length=2, choices=HEATING_CHOICES, default="DH")

    def __str__(self):
        return f"{self.location} {self.price} {self.story}"


class Condition(models.Model):
    name = models.CharField(max_length=20)
    apartment = models.ManyToManyField(Apartment)

    def __str__(self):
        return f"{self.name}"


class Content(models.Model):
    name = models.CharField(max_length=20)
    apartment = models.ManyToManyField(Apartment)

    def __str__(self):
        return f"{self.name}"