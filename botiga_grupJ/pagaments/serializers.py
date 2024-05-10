from django.contrib.auth.models import Group, User

from comandes.models import Comanda
from .models import Pagament, User
from rest_framework import serializers

# campos del user
class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model= User
        fields = ['id','name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # No mostrar contraseña


# comanda con datos del user
# cada comanda puede tener varios carritos con propiedad de pagado o no
class ComandaSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Incluir el serializador de User para mostrar los datos del usuario

    class Meta:
        model = Comanda
        fields = ['id', 'carreto', 'data', 'user']  # Incluir los campos necesarios de Comanda


# serializador de campos de la tabla pagament
class PagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagament
        fields = ['id','tarjet_num', 'exp_date', 'cvc', 'user']


# para mostrar TODOS los datos al pagar: comanda, user, datos de pago
class GetPagamentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Pagament
        fields = ['id','tarjet_num', 'exp_date', 'cvc', 'user']


class UserPagamentSerializer(serializers.ModelSerializer):
    #guardarà los datos de manera filtrada
    pagaments = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'pagaments']

    # def get_pagaments(self,obj):
    #     pagaments = Pagament.objects.filter(user=obj.id)
    #     return PagamentSerializer(pagaments, many=True).data

class GetPagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pagament
        fields = ['id','tarjet_num', 'exp_date', 'cvc', 'user']

class AddPagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagament
        fields = ['tarjet_num', 'exp_date', 'cvc', 'user']

