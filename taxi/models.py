from django.db import models


class Taxi(models.Model):
    taxi_name = models.CharField(max_length=255)
    licence_plate = models.CharField(max_length=11)
    driver_name = models.CharField(max_length=50)
    passenger_capacity = models.PositiveIntegerField()
    car_model = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.taxi_name
