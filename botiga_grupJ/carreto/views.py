from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carrito
from .serializers import CarritoSerializer, CarritoPOSTSerializer

@api_view(['GET', 'POST'])
def Cart(request, carrito_id=None):
    if request.method == 'GET':
        if carrito_id is not None:
            try:
                carrito = Carrito.objects.get(id=carrito_id)
                serializer = CarritoSerializer(carrito)
                return Response(serializer.data)
            except Carrito.DoesNotExist:
                return Response({'message': 'Carrito no encontrado'}, status=404)
        else:
            carritos = Carrito.objects.all()
            serializer = CarritoSerializer(carritos, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarritoPOSTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Datos insertados correctamente"}, status=201)
        return Response(serializer.errors, status=400)




@api_view(['GET', 'PUT', 'DELETE'])
def CartModify(request, carrito_id=None):
    if request.method == 'GET':
        try:
            carrito = Carrito.objects.get(pk=carrito_id)
            serializer = CarritoSerializer(carrito)
            return Response(serializer.data)
        except Carrito.DoesNotExist:
            return Response({'message': 'Carrito no encontrado'}, status=404)

    elif request.method == 'PUT':
        carrito = Carrito.objects.get(pk=carrito_id)
        serializer = CarritoSerializer(carrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Datos actualizados correctamente"})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            carrito = Carrito.objects.get(pk=carrito_id)
            carrito.delete()
            return Response({"mensaje": "Datos eliminados correctamente"})
        except Carrito.DoesNotExist:
            return Response({'message': 'Carrito no encontrado'}, status=404)