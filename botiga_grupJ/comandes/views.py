from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comanda
from .serializers import ComandaSerializer

@api_view(['GET'])
def comanda_list(request):
    comandas = Comanda.objects.all()
    serializer = ComandaSerializer(comandas, many=True)
    return Response(serializer.data)