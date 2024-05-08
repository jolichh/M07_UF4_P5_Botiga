from rest_framework import serializers
from .models import Carrito
from .models import Producte


class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['id', 'name', 'description', 'price', 'valoration', 'quantity']

class CarritoSerializer(serializers.ModelSerializer):
    productos = serializers.SerializerMethodField()  

    class Meta:
        model = Carrito
        fields = ['id', 'productos']



    def get_productos(self, obj):
        # Obtiene los IDs de los productos asociados al carrito
        productos_ids = obj.productos.all()
        # Obtiene los detalles de los productos por sus IDs
        productos = Producte.objects.filter(id__in=productos_ids)
        # Serializa los productos
        serializer = ProducteSerializer(productos, many=True)
        return serializer.data

class CarritoPOSTSerializer(serializers.ModelSerializer):
    productos = serializers.ListField(child=serializers.IntegerField())  # Lista de IDs de productos

    class Meta:
        model = Carrito
        fields = ['productos']

    def create(self, validated_data):
        productos_ids = validated_data.pop('productos', [])  # Recibe los IDs de los productos
        carrito = Carrito.objects.create(**validated_data)  # Crear el carrito
        carrito.productos.add(*productos_ids)  # Asociar los productos al carrito
        return carrito
    

class CarritoPUTSerializer(serializers.ModelSerializer):
    productos = serializers.ListField(child=serializers.IntegerField())  # Lista de IDs de productos

    class Meta:
        model = Carrito
        fields = ['productos']

    def update(self, instance, validated_data):
        productos_ids = validated_data.pop('productos', [])  # Recibe los IDs de los productos
        instance.productos.clear()  # Borra todos los Productos
        instance.productos.add(*productos_ids)  # Asociar los productos al carrito
        instance.save()
        return instance