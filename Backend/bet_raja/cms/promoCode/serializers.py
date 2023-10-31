from rest_framework import serializers
from cms.models import Site , PromoCode 

# PromoCode Serializer
class PromoCodeListSerializer(serializers.ModelSerializer):
    site=serializers.SlugRelatedField(queryset=Site.objects.all() , slug_field="name")
    class Meta:
        model=PromoCode
        fields=["id" , "site"]


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PromoCode
        fields="__all__"
    







