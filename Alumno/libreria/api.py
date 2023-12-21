from .models import curso,alumno
from rest_framework import viewsets,permissions
from .serializers import cursoSerializers, alumnoSerializers


class alumnoViewSet (viewsets.ModelViewSet):
    queryset = alumno.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = alumnoSerializers


class cursoViewSet (viewsets.ModelViewSet):
    queryset = curso.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = cursoSerializers