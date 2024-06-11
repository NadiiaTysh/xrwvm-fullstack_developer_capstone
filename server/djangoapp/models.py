from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    TYPE_CHOICES = [
        ('sedan','Sedan'),
        ('suv','SUV'),
        ('wagon','Wagon'),
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='suv')
    year = models.IntegerField(default=2023, validators=[MinValueValidator(2015), MaxValueValidator(2023)])

    def __str__(self):
        return self.name
