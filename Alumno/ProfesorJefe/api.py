from .models import ProfJefe
from rest_framework import viewsets,permissions
from .serializers import profeSerializers


class profeViewSet (viewsets.ModelViewSet):
    queryset = ProfJefe.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = profeSerializers