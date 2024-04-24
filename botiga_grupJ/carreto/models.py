from django.db import models
from cataleg.models import Producte

# Create your models here.
class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    # Relación uno a muchos con la tabla Producte
    productos = models.ManyToManyField(Producte)  