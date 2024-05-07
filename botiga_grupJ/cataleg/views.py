from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categoria, Producte
from cataleg.serializers import CategoriaSerializer, ProducteSerializer, GroupSerializer, UserSerializer

# EL CATALOGO MUESTRA TODOS LOS PRODUCTOS
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

# MODIFICAR-ELIMINAR UN PRODUCTO
@api_view(['GET','PUT','DELETE'])
def update_delete_cataleg(request, pk=None):
    if request.method == 'GET':
        try: 
            prod_catalog = Producte.objects.get(pk=pk)            
            #Serializar producto
            serializer = ProducteSerializer(prod_catalog)

            return Response(serializer.data)
        except Producte.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # INDIFERENTE SI LE PASAS EL ID O NO (lo obtiene de la url)    
    if request.method == 'PUT':
        try:
            prod_catalog = Producte.objects.get(pk=pk)
        except Producte.DoesNotExist:
            return Response({"message": "No se ha encontrado coincidencias en la data base para ese ID"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProducteSerializer(prod_catalog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            prod_catalog = Producte.objects.get(pk=pk)
        except Producte.DoesNotExist:
            return Response({"message": "El producto no existe"}, status=status.HTTP_404_NOT_FOUND)
       
        prod_catalog.delete()
        return Response({"message": "El producto se ha eliminado correctamente"})
    
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