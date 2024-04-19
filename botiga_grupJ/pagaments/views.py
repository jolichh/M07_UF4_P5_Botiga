from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from comandes.models import Comanda

# Create your views here.
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def pagament(request):
    if request.method == 'GET':
        try: 
            # get_comanda = Comanda.objects.all()
            
            # comanda_data = [{'id': producto.id, 'carreto': producto.carreto, 'data': producto.data} for producto in get_comanda]
            # return JsonResponse(comanda_data, safe=False)
            return Response({"message": "WWWllo, world!"})
        except Comanda.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        return Response({"message": "Deeelete"})
    
    elif request.method == 'POST':
        return Response({"message": "Un post"})

