from django.shortcuts import render
from django.http import JsonResponse
from carreto.models import Carrito
from comandes.models import Comanda
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pagament, User
from .serializers import AddPagamentSerializer, GetUserPagamentSerializer, UpdatePaymentSerializer
from django.contrib.auth.hashers import check_password
import json

# Mostrar los datos relacionados al pago: 
# todos los productos de la comanda junto al user y sus datos de pago
@api_view(['GET', 'POST'])
def pagaments(request):
    # mostrar todo
    if request.method == 'GET':
        try: 
            get_user = User.objects.all()
            
            #Serializar pagos ordenando y mostrar datos del user
            serializer = GetUserPagamentSerializer(get_user, many=True)

            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # realizar el pago
    elif request.method == 'POST':
        
        # DEBE: coincidir password y contraseña con los del user logeado(id). 
        # El user ID viene con el login, se pedirá introducir datos de login para verificar que se trata del mismo user

        ## VERIFICAR USER
        # Obtener los datos USER de la solicitud
        data = request.data
        user_id = data.get('user_id')   #no editable
        user_name = data.get('name')
        user_password = data.get('password')
        carrito_pagar = data.get('carrito_id')

        
        try:
            # Obtener el usuario y sus datos
            user = User.objects.get(pk=user_id)
            
            # Verificar los datos de usuario que coincidan
            if user.name != user_name or user_password!=user.password:
                return Response({"message": "Los datos de usuario no coinciden"}, status=status.HTTP_401_UNAUTHORIZED)
                
            # realizar el pago       
            try:     
                # obtener su comanda
                comanda = Comanda.objects.get(user_id=user_id)
                # el id de carrito se lo pasamos en JSON

                # obtener el carrito no pagado (solo hay uno)
                carrito = Carrito.objects.get(id=carrito_pagar)

                # modificar el boolean del carrito a pagado (update carrito)
                carrito.compra_realizada = True
                carrito.save()

                # crear nuevo carrito para user (indicar id de comanda)
                carrito_vacio = Carrito.objects.create(compra_realizada=False)
                carrito_vacio.save()

                # asignarle la comanda
                comanda.carreto = carrito_vacio
                comanda.save()

                return Response({"message": "Se ha realizado el pago correctamente"})
            except:
                return Response({"message":"no se ha encontrado su carrito..."}, status=status.HTTP_404_NOT_FOUND)
        
        except User.DoesNotExist:
            return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
  
    return Response({"nada a mostrar..."})

# trabaja sobre un dato especifico de pago: 
# muestra los datos de pago de un usuario, junto a todos los datos relacionados a ese user
@api_view(['GET','PUT'])
def update_delete_pagament(request, pk=None):
    if request.method == 'GET':
        try: 
            pagament = User.objects.get(pk=pk)            
            #Serializar pagos ordenando y mostrar datos del user
            serializer = GetUserPagamentSerializer(pagament)

            return Response(serializer.data)
        except Pagament.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # modificar datos de la targeta  
    # requiere user name y password 
    if request.method == 'PUT':

        # Obtener los datos de la solicitud
        data = request.data
        user_name = data.get('name')
        password = data.get('password')

        # Obtener el usuario y su pagament asociado
        try:
            user = User.objects.get(pk=pk)
            user_id = user.id

            # buscar pagament
            pagament = Pagament.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Verificar los datos de usuario que coincidan
        if user.name != user_name or password!=user.password:
            return Response({"message": "Los datos de usuario no coinciden"}, status=status.HTTP_401_UNAUTHORIZED)

        # Serializar y actualizar el pagament
        serializer = UpdatePaymentSerializer(pagament, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"nada a mostrar..."})