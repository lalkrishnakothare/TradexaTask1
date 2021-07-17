from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
