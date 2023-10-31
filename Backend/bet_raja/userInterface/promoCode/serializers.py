from rest_framework import serializers
from cms.models import   PromoCode
from ..sites.serializers import SiteSerializer


# PromoCode Serializer
class PromoCodeSerializer(serializers.ModelSerializer):
    site=SiteSerializer()
    class Meta:
        model=PromoCode
        fields="__all__"






