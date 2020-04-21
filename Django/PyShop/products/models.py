from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=20830)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=2000)
    dicount = models.FloatField()
