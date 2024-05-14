from django.contrib.auth.models import Group, User

from carreto.serializers import CarritoSerializer
from comandes.models import Comanda
from carreto.models import Carrito
from .models import Pagament, User
from rest_framework import serializers
from django.contrib.auth.hashers import check_password


# serializador de campos de la tabla pagament
class PagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagament
        fields = ['id','tarjet_num', 'exp_date', 'cvc', 'user']


class ComandaSerializer(serializers.ModelSerializer):
    #Aqui indico que el campo carreto de Comanda tiene qie serializar-lo
    #Usando el serializador de Carrito para mostrar todo el contenido del carrito
    carreto = CarritoSerializer(read_only=True)

    class Meta:
        model = Comanda
        fields = ['id', 'carreto', 'compra_realizada', 'data', 'user']

## MOSTRAR USUARIOS CON TODA SU INFO RELACIONADA: 
# formas de pago(pagament), comanda, carreto
# datos en CASCADE
class GetUserPagamentSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField()
    comanda = serializers.SerializerMethodField()

    class Meta:
        model= User
        fields = ['id','name', 'email', 'password', 'payment', 'comanda']
        #extra_kwargs = {'password': {'write_only': True}}  # No mostrar contraseña
        
    def get_payment(self,obj):
        pagaments = Pagament.objects.filter(user=obj.id)
        return PagamentSerializer(pagaments, many=True).data
    
    def get_comanda(self, obj):
        comandes = Comanda.objects.filter(user=obj.id)
        return ComandaSerializer(comandes, many=True).data
    
    
# UPDATE datos de pago
class UpdatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagament
        fields = ['tarjet_num', 'exp_date', 'cvc']

    def update(self, instance, validated_data):
        # Actualizar los campos del objeto Pagament con los datos validados
        instance.tarjet_num = validated_data.get('tarjet_num', instance.tarjet_num)
        instance.exp_date = validated_data.get('exp_date', instance.exp_date)
        instance.cvc = validated_data.get('cvc', instance.cvc)
        instance.save()  # Guardar los cambios en la base de datos
        return instance
    