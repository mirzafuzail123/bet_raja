from rest_framework import serializers
from cms.models import Site , SiteOverview , Sport

# Site Serializer
class SiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Site
        fields="__all__"


class SingleSiteSerializer(serializers.ModelSerializer):
    sports=serializers.PrimaryKeyRelatedField(queryset=Sport.objects.all() , many=True)
    sportsData=serializers.SerializerMethodField()
    class Meta:
        model=Site
        fields="__all__"
    
    def get_sportsData(self , obj):
        sportsList=[]
        for data in obj.sports.all():
            sportsList.append({
                "name":data.name , 
                "id":data.id , 
            })
        return sportsList





# Module : Overview



# Site Overview List
class SiteOverviewListSerializer(serializers.ModelSerializer):
    site=serializers.SlugRelatedField(queryset=Site.objects.all() , slug_field="name")
    class Meta:
        model=SiteOverview
        fields=["id" , "site"]


class SiteOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=SiteOverview
        fields="__all__"
