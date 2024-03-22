from django.db import models


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    price_confort = models.FloatField()
    price_econ = models.FloatField()
    city = models.ForeignKey("api.City", on_delete=models.CASCADE, null=True, blank=True) 
    duration = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)
    bed = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    
    def __str__(self):
        return f"{self.name}"