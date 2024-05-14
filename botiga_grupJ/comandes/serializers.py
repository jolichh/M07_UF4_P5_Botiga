from rest_framework import serializers
from .models import Comanda

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ['id', 'carreto', 'compra_realizada', 'data', 'user']