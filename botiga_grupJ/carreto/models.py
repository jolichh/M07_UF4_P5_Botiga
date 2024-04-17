from django.db import models
from cataleg.models import Producte

# Create your models here.
class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    productos = models.ForeignKey(Producte, on_delete=models.CASCADE)
