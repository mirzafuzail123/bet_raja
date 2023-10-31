from rest_framework import serializers
from cms.models import  App , AppOverview
from ..sites.serializers import SiteSerializer


# App Serializer
class AppSerializer(serializers.ModelSerializer):
    site=SiteSerializer()
    class Meta:
        model=App
        fields="__all__"



# App OVervuiew
class AppOverviewSerializer(serializers.ModelSerializer):
    app=AppSerializer()
    class Meta:
        model=AppOverview
        fields="__all__"


