from rest_framework import serializers
from .models import WaterParameters

class WaterParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterParameters
        fields = '__all__'