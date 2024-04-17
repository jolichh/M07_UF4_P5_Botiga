from django.db import models
from carreto.models import Carrito
from pagaments.models import User

# Create your models here.
class Comanda(models.Model):
    id = models.AutoField(primary_key=True)
    carreto = models.ForeignKey(Carrito, on_delete=models.CASCADE)    
    data = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)