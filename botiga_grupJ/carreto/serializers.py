from rest_framework import serializers
from .models import Carrito, ProductoEnCarrito
from .models import Producte




#GET PRODUCTOS
class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['id', 'name', 'description', 'price', 'valoration', 'quantity']

class ProductoEnCarritoSerializer(serializers.ModelSerializer):
    producto = ProducteSerializer(read_only=True)
    producto_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ProductoEnCarrito
        fields = [ 'cantidad', 'producto', 'producto_id']

class CarritoSerializer(serializers.ModelSerializer):
    productos = ProductoEnCarritoSerializer(source='productoencarrito_set', many=True, read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'productos', 'compra_realizada']

    def get_productos(self, obj):
        # Obtiene las instancias de ProductoEnCarrito asociadas al carrito
        productos_en_carrito = ProductoEnCarrito.objects.filter(carrito=obj)
        # Serializa las instancias de ProductoEnCarrito
        serializer = ProductoEnCarritoSerializer(productos_en_carrito, many=True)
        return serializer.data



#POST PRODUCTOS

class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['id', 'name', 'description', 'price', 'valoration', 'quantity']

class ProductoEnCarritoSerializer(serializers.ModelSerializer):
    producto = ProducteSerializer(read_only=True)
    producto_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ProductoEnCarrito
        fields = ['id', 'cantidad', 'producto', 'producto_id']

class CarritoPOSTSerializer(serializers.ModelSerializer):
    productos = ProductoEnCarritoSerializer(many=True)

    class Meta:
        model = Carrito
        fields = ['productos']

    def create(self, validated_data):
        productos_data = validated_data.pop('productos')
        carrito = Carrito.objects.create()
        for producto_data in productos_data:
            ProductoEnCarrito.objects.create(carrito=carrito, **producto_data)
        return carrito
    


#PUT PRODUCTOS
class ProductoEnCarritoUpdateSerializer(serializers.ModelSerializer):
    producto_id = serializers.IntegerField()

    class Meta:
        model = ProductoEnCarrito
        fields = ['producto_id', 'cantidad']

class CarritoPUTSerializer(serializers.ModelSerializer):
    productos = ProductoEnCarritoUpdateSerializer(many=True)

    class Meta:
        model = Carrito
        fields = ['productos']

    def update(self, instance, validated_data):
        productos_data = validated_data.pop('productos', [])
        instance.productos.clear()  

        for producto_data in productos_data:
            producto_id = producto_data['producto_id']
            cantidad = producto_data['cantidad']
            producto_en_carrito, created = ProductoEnCarrito.objects.update_or_create(
                carrito=instance, producto_id=producto_id, defaults={'cantidad': cantidad})

        instance.save()
        return instance
    
