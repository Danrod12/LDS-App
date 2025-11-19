from rest_framework import serializers
from .models import *

class ObraMisionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObraMisional
        fields = '__all__'



