from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def hello(request):
    if request.method == 'GET':
        return Response({"mensaje": "Hola, mundo!"})
    elif request.method == 'POST':
        # Get the data from the request
        data = request.data
        
        # Process the data and save it to the database
        # Replace this with your actual code to save the data to the database
        
        # Return a response indicating the data was inserted successfully
        return Response({"mensaje": "Datos insertados correctamente"})
    elif request.method == 'PUT':
        return Response({"mensaje": "Datos actualizados correctamente"})
    elif request.method == 'DELETE':
        return Response({"mensaje": "Datos eliminados correctamente"})
