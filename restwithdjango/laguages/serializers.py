from rest_framework import serializers
from .models import Language, LanguageInventor, Programmer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'pradigm', 'inventor')


class LanguageInventorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LanguageInventor
        fields = ('id', 'url', 'name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'language')

