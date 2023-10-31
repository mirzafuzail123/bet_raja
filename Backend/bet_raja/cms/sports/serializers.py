from rest_framework import serializers
from cms.models import  Sport

# Sports Serializer
class SportsListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sport
        fields="__all__"


class SingleSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sport
        fields="__all__"

