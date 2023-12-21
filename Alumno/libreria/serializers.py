from rest_framework import serializers
from .models import curso, alumno

class cursoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = curso 
        fields = ('__all__')

class alumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = alumno
        fields = ('__all__')