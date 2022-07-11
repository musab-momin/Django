from .models import Language, Framework
from rest_framework import serializers

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')
    
    def validate_name(self, value):
        if value.lower() == 'java':
            raise serializers.ValidationError('Java is not allowed')
        return value


class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = ('id', 'name', 'language')
    