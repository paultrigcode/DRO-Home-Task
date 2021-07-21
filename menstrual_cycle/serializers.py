from rest_framework import serializers
from .models import CycleSetting

class CycleSettingSerializer(serializers.ModelSerializer):
    '''
    Serializer class for CycleSetting model
    '''    
    
    class Meta:
        model = CycleSetting
        fields = '__all__'
