from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from carreto.models import Carrito
from pagaments.models import User

class Comanda(models.Model):
    id = models.AutoField(primary_key=True)
    carreto = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    compra_realizada = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

#Aqui indico que tengo que llamar a la funcion update_or_create_comanda
#Cada vez que se haga un post_save de un Carrito    
@receiver(post_save, sender=Carrito)
#Y esta funcion dependiendo si el carrito es nuevo crea una nueva Comand o si ya existia actualiza la comanda 
#Eso lo sabe gracias a la variable created que se pasa por parametro
def update_or_create_comanda(sender, instance, created, **kwargs):
    if created:
        # Si el Carrito acaba de ser creado, crea una nueva Comanda
        Comanda.objects.create(carreto=instance, compra_realizada=instance.compra_realizada)
    else:
        # Si el Carrito ya existía y solo se está actualizando, actualiza la Comanda existente
        Comanda.objects.filter(carreto=instance).update(compra_realizada=instance.compra_realizada)