from django.contrib.auth.models import Group, User
from rest_framework import serializers


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nombre', 'precio', 'groups']

