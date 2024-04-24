from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pagament
from .serializers import PagamentSerializer, UserPagamentSerializer, UserSerializer

# Create your views here.
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def pagament(request):
    if request.method == 'GET':
        try: 
            get_pagaments = Pagament.objects.all()
            
            #Serializar pagos ordenando y mostrar datos del user
            serializer = PagamentSerializer(get_pagaments, many=True)

            return Response(serializer.data)
        except Pagament.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        return Response({"message": "Deeelete"})
    
    elif request.method == 'POST':
        # AÑADIR DATOS DE PAGO
        serializer = PagamentSerializer(data=request.data)
        if serializer.is_valid():
            # Verificar si ya existe un pago para este usuario
            user_id = serializer.validated_data['user']
            if not Pagament.objects.filter(user_id=user_id).exists():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Ya existe un pago para este usuario"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Los datos de pago no se han podido añadir"})
    
    elif request.method == 'PUT':
        return Response({"message": "Un put :)"})
    
    return Response({"nada a mostrar..."})

