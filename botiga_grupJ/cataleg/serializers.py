from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Producte, Categoria

class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['id', 'name', 'description', 'price', 'valoration', 'quantity', 'categoria']

class CategoriaSerializer(serializers.ModelSerializer):
    productes = ProducteSerializer(many=True, read_only=True, source='producte_set')  # Usamos source='producte_set'

    class Meta:
        model = Categoria
        fields = ('id', 'name', 'productes')

    def get_productes(self, obj):
        productos = obj.productes.all()
        serializer = ProducteSerializer(productos, many=True)
        return serializer.data
    


# esto de abajo son ejemplos del tutorial
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']