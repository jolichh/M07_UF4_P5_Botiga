from django.contrib.auth.models import Group, User

from carreto.serializers import CarritoSerializer
from comandes.models import Comanda
from carreto.models import Carrito
from .models import Pagament, User
from rest_framework import serializers

# campos del user
class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model= User
        fields = ['id','name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # No mostrar contraseña


# comanda con datos del carrito
# cada comanda puede tener varios carritos con propiedad de pagado o no
class ComandaSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Incluir el serializador de User para mostrar los datos del usuario
    carrito = serializers.SerializerMethodField()

    class Meta:
        model = Comanda
        fields = ['id', 'carreto', 'data', 'user']  # Incluir los campos necesarios de Comanda

    def get_carrito(self, obj):
        comandes = Carrito.objects.filter(user=obj.id)
        #importamos serializador de la app carreto
        return CarritoSerializer(comandes, many=True).data

# serializador de campos de la tabla pagament
class PagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagament
        fields = ['id','tarjet_num', 'exp_date', 'cvc', 'user']


# class GetPagamentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Pagament
#         fields = ['id','tarjet_num', 'exp_date', 'cvc', 'user']


# serializador para el POST
class AddPagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagament
        fields = ['tarjet_num', 'exp_date', 'cvc', 'user']

# muestra datos del usuario junto a sus datos de comandas
class UserPagamentSerializer(serializers.ModelSerializer):
    # guardarà los datos de manera filtrada
    # no es un campo real, obtiene los datos a través de las 'def'
    # donde obtiene los datos relacionados a cada user
    pagaments = serializers.SerializerMethodField()
    comandes = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'pagaments', 'comandes']

    def get_pagaments(self,obj):
        pagaments = Pagament.objects.filter(user=obj.id)
        return PagamentSerializer(pagaments, many=True).data
    
    def get_comandes(self, obj):
        comandes = Comanda.objects.filter(user=obj.id)
        return ComandaSerializer(comandes, many=True).data
    
# serializador del modelo comanda
class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ['id', 'carreto', 'data', 'user']

# para mostrar TODOS los datos al pagar: comanda, user, datos de pago
# los datos obtenidos formato CASCADE
class GetPagamentSerializer(serializers.ModelSerializer):
    user = UserPagamentSerializer()

    class Meta:
        model=Pagament
        fields = ['id','tarjet_num', 'exp_date', 'cvc', 'user']

## MOSTRAR USUARIOS CON TODA SU INFO RELACIONADA: 
# formas de pago(pagament), comanda, carreto
class GetUserPagamentSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField()

    class Meta:
        model= User
        fields = ['id','name', 'email', 'password', 'payment']
        #extra_kwargs = {'password': {'write_only': True}}  # No mostrar contraseña
        
    def get_payment(self,obj):
        pagaments = Pagament.objects.filter(user=obj.id)
        return PagamentSerializer(pagaments, many=True).data
    