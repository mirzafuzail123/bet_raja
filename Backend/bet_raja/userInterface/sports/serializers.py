from rest_framework import serializers
from cms.models import  Sport


# Site Serializer
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sport
        fields="__all__"





