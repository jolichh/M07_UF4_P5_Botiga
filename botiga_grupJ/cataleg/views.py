from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categoria, Producte
from cataleg.serializers import CategoriaSerializer, ProducteSerializer, GroupSerializer, UserSerializer

@api_view(['GET', 'POST'])
def cataleg(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # AÑADIR NUEVO PRODUCTO
        serializer = ProducteSerializer(data=request.data)
        # Asegurar formato de datos cumple la serialización
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
               
    return Response({"nada a mostrar..."})


# esto de abajo son ejemplo del tutorial
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]