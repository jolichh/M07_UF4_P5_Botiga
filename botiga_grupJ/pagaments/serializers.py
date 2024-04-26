from django.contrib.auth.models import Group, User
from .models import Pagament, User
from rest_framework import serializers


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

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model= User
        fields = ['name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # No mostrar contraseña