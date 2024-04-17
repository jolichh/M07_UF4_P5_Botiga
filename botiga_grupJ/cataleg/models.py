from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Producte(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    valoration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    quantity = models.PositiveBigIntegerField()