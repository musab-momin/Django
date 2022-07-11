from rest_framework import serializers
from .models import ApiNote



class ApiNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiNote
        fields = ('__all__')

