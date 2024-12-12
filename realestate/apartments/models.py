from django.db import models
from django.contrib.auth.models import AbstractBaseUser

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


class Condition(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}"


class Content(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}"


class Apartment(models.Model):
    num_of_rooms = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    story = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default="OG")
    furnishing = models.CharField(max_length=2, choices=FURNISHING_CHOICES, default="FU")
    heating = models.CharField(max_length=2, choices=HEATING_CHOICES, default="DH")
    conditions = models.ManyToManyField(Condition)
    contents = models.ManyToManyField(Content)


    def __str__(self):
        return f"{self.location} {self.price} {self.story}"


class Profile(AbstractBaseUser):
    phone = models.CharField(max_length=16)


class Landlord(Profile):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agency(Profile):
    name = models.CharField(max_length=32)
    website = models.CharField(max_length=48)
    email = models.EmailField(max_length=64)
    registration_date = models.DateField()


    class Meta:
        verbose_name_plural = "Agencies"


    def __str__(self):
        return f"{self.name}"