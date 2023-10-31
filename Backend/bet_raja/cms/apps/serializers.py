from rest_framework import serializers
from cms.models import  App , Site ,AppOverview

# Apps Serializer
class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model=App
        fields="__all__"


class AppListSerializer(serializers.ModelSerializer):
    site=serializers.SlugRelatedField(queryset=Site.objects.all() , slug_field="name")
    class Meta:
        model=App
        fields=["id" , "site" , "version" , "size"]




# Module OVerview
class AppOverviewListSerializer(serializers.ModelSerializer):
    app=serializers.PrimaryKeyRelatedField(queryset=App.objects.all())
    appData=serializers.SerializerMethodField()
    class Meta:
        model=AppOverview
        fields=["id" , "app" , "appData"]

    def get_appData(self , obj):
        if obj.app:
            return {
                "name":obj.app.site.name
            }



class AppOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppOverview
        fields="__all__"