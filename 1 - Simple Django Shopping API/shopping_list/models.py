from django.db import models

# Create your models here.
from django.db import models

class ShoppingItem(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
