from django.db import models
from cataleg.models import Producte

# Create your models here.

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    # Relación uno a muchos con la tabla Producte
    productos = models.ManyToManyField(Producte, through='ProductoEnCarrito')
    compra_realizada = models.BooleanField(default=False)  

class ProductoEnCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producte, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'carreto_productoencarrito'

