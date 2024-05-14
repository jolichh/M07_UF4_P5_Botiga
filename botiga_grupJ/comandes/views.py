from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comanda
from .serializers import ComandaSerializer

#Me muestra todas las comandas
@api_view(['GET'])
def comanda_list(request):
    comandas = Comanda.objects.all()
    serializer = ComandaSerializer(comandas, many=True)
    return Response(serializer.data)

#Solo muestra los carritos que han sido comprados
@api_view(['GET'])
def comanda_list_completed(request):
    #Filtra las comandas que han sido compradas por la variable compra_realizada
    comandas = Comanda.objects.filter(compra_realizada=True)
    serializer = ComandaSerializer(comandas, many=True)
    return Response(serializer.data)


#Solo muestra los carritos que no han sido comprados
@api_view(['GET'])
def comanda_list_not_completed(request):
    #Filtra las comandas que han sido compradas por la variable compra_realizada
    comandas = Comanda.objects.filter(compra_realizada=False)
    serializer = ComandaSerializer(comandas, many=True)
    return Response(serializer.data)