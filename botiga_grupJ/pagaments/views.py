from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pagament, User
from .serializers import AddPagamentSerializer, GetUserPagamentSerializer

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
    
    # realizar el pago: 
    # marcar en comanda pagado=TRUE
    # vaciar carrito
    elif request.method == 'POST':
        # # AÑADIR DATOS DE PAGO
        # serializer = AddPagamentSerializer(data=request.data)
        # # Asegurar formato de datos cumple la serialización
        # if serializer.is_valid():
        #     # Verificar si ya existe un pago para este usuario
        #     user_id = serializer.validated_data['user']
        #     if not Pagament.objects.filter(user_id=user_id).exists():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     else:
        #         return Response({"message": "Ya existe un pago para este usuario"}, status=status.HTTP_400_BAD_REQUEST)
        #     serializer.save()

        # Añadir carrito a COMANDA y actualizar boolean
        #return Response({"message": "ACTUALIZAR BOOLEAN A TRUE PAGADO CARRITO DE COMANDA"})

        return Response(serializer.data, status=status.HTTP_201_CREATED)
       
    return Response({"nada a mostrar..."})

# trabaja sobre un dato especifico de pago: 
# muestra los datos de pago de un usuario, junto a todos los datos relacionados a ese user
@api_view(['GET','PUT','DELETE'])
def update_delete_pagament(request, pk=None):
    if request.method == 'GET':
        try: 
            pagament = User.objects.get(pk=pk)            
            #Serializar pagos ordenando y mostrar datos del user
            serializer = GetUserPagamentSerializer(pagament)

            return Response(serializer.data)
        except Pagament.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            pagament = Pagament.objects.get(pk=pk)
        except Pagament.DoesNotExist:
            return Response({"message": "No se ha encontrado coincidencias en la data base para ese ID"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddPagamentSerializer(pagament, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            pagament = Pagament.objects.get(pk=pk)
        except Pagament.DoesNotExist:
            return Response({"message": "El pago no existe"}, status=status.HTTP_404_NOT_FOUND)
       
        pagament.delete()
        return Response({"message": "El metodo de pago se ha eliminado correctamente"})
    
    return Response({"nada a mostrar..."})