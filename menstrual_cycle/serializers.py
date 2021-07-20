from rest_framework import serializers
from .models import CycleSetting

class CycleSettingSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = CycleSetting
        fields = '__all__'
