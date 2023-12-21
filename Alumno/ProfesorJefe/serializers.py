from rest_framework import serializers
from .models import ProfJefe

class profeSerializers(serializers.ModelSerializer):
    class Meta: 
        model = ProfJefe 
        fields = ('__all__')