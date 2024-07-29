from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator



class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car = models.ForeignKey(CarMake, related_name='model', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.IntegerField(default=2023,
        validators=[
            MinValueValidator(2015, message="Year must be 2015 or later."),
            MaxValueValidator(2023, message="Year cannot exceed 2023."),
        ]
    )

    def __str__(self):
        return self.name
