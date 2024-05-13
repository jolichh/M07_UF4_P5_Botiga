from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comanda
from .serializers import ComandaSerializer

@api_view(['GET', 'POST'])
def Comanda(request):
    if request.method == 'GET':
        comandas = Comanda.objects.all()
        serializer = ComandaSerializer(comandas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response({'message': 'POST method not implemented'}, status=501)