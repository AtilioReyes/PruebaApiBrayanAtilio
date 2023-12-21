from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import AlumnoForm
from .forms import CursoForm
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from .serializers import cursoSerializers, alumnoSerializers
from rest_framework import viewsets,permissions




@api_view(['GET','POST'])
def curso_lista(request):
    if request.method == 'GET':
        curso = curso.objetcs.all()
        serializer = cursoSerializers(curso,many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = curso = cursoSerializers(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUESt)
    

@api_view(['GET','PUT','DELETE'])
def curso_detalles(request, pk):
    try:
        curso = curso.objetcs.get(pk=pk)
    except curso.DoesNotExist:
        return Response (status =status.HTTP_404_NOT_FOUnd)
    
    if request.method == 'GET':
        serializer = cursoSerializers(curso)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = cursoSerializers(curso, data = request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        curso.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)    
