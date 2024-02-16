# pricing/models.py
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    TYPE_CHOICES = (
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    #description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.FloatField()
    km_price_perishable = models.FloatField()
    km_price_non_perishable = models.FloatField()
    base_price = models.FloatField()
