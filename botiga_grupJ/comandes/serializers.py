from rest_framework import serializers

from botiga_grupJ.carreto.models import Carrito, ProductoEnCarrito
from botiga_grupJ.carreto.serializers import ProducteSerializer
from .models import Comanda

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ['id', 'data', 'user_id']  # Asegúrate de cambiar estos campos a los que correspondan a tu modelo Comanda

class ProductoEnCarritoSerializer(serializers.ModelSerializer):
    producto = ProducteSerializer(read_only=True)
    producto_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ProductoEnCarrito
        fields = ['cantidad', 'producto', 'producto_id']

class CarritoSerializer(serializers.ModelSerializer):
    productos = ProductoEnCarritoSerializer(source='productoencarrito_set', many=True, read_only=True)
    comanda = ComandaSerializer(read_only=True)  # Agrega esto

    class Meta:
        model = Carrito
        fields = ['id', 'productos', 'compra_realizada', 'comanda']  # Agrega 'comanda' aquí