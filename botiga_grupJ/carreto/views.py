from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carrito
from .serializers import CarritoSerializer,CarritoPostSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Cart(request, carrito_id=None):
    if request.method == 'GET':
        carritos = Carrito.objects.all()
        serializer = CarritoSerializer(carritos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarritoPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Datos insertados correctamente"})
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        carrito = Carrito.objects.get(pk=carrito_id)
        serializer = CarritoSerializer(carrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Datos actualizados correctamente"})
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        carrito = Carrito.objects.get(pk=carrito_id)
        carrito.delete()
        return Response({"mensaje": "Datos eliminados correctamente"})
