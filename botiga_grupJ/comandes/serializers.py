from rest_framework import serializers

from carreto.serializers import CarritoSerializer
from .models import Comanda

class ComandaSerializer(serializers.ModelSerializer):
    #Aqui indico que el campo carreto de Comanda tiene qie serializar-lo
    #Usando el serializador de Carrito para mostrar todo el contenido del carrito
    carreto = CarritoSerializer(read_only=True)

    class Meta:
        model = Comanda
        fields = ['id', 'carreto', 'data', 'user']


