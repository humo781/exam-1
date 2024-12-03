from django.db import models

class Meal(models.Model):
    meal_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    price = models.PositiveIntegerField()
    sort = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)

    def __str__(self):
        return self.meal_name
