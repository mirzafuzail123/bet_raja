from rest_framework import serializers
from cms.models import  Site , SiteOverview

# Site Serializer
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Site
        fields="__all__"



# Site OVervuiew
class SiteOverviewSerializer(serializers.ModelSerializer):
    site=SiteSerializer()
    class Meta:
        model=SiteOverview
        fields="__all__"


