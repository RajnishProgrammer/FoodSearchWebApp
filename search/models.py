from django.db import models

# Create your models here.

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    items = models.CharField(max_length=200)
    # lat_long = models.DecimalField(max_digits=9, decimal_places=6)
    lat_long = models.CharField(max_length=200)
    full_details = models.TextField()
