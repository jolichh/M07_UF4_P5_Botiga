from django.db import models

# Create your models here.
class comanda(models.Model):
    id = models.AutoField(primary_key=True)
    carreto = models.ForeignKey('carreto', on_delete=models.CASCADE)
    
    data = models.DateField(auto_now_add=True)