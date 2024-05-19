from django.db import models

# Create your models here.
class Drinks (models.Model):
    drink_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey('DrinksCategory', on_delete=models.PROTECT, default=None)

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=100)
    