from django.db import models

# Create your models here.


class Pizza(models.Model):
    size = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    ingredient_1 = models.CharField(max_length=30)
    ingredient_2 = models.CharField(max_length=30, default='')
    ingredient_3 = models.CharField(max_length=30, default='')
    price = models.FloatField()


