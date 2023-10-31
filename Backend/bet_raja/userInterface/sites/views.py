from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView
from cms.models import Sport , AppOverview , PromoCode
from .serializers import *
from rest_framework.response import Response
from rest_framework import status




# Navbar
class NavOptionsView(APIView):
    def get(self , request , format=None):
        # Sites
        allsiteOverview=SiteOverview.objects.all()
        siteList=[]
        for overview in allsiteOverview:
            siteList.append({
                "name":overview.site.name , 
                "slug":overview.site.slug , 
            })

        # Apps
        allAppOverview=AppOverview.objects.all()
        appList=[]
        for overview in allAppOverview:
            appList.append({
                "name":overview.app.site.name , 
                "slug":overview.app.site.slug
            })
        
        # Sports
        allSports=Sport.objects.all()
        sportList=[]
        for sport in allSports:
            sportList.append({
                "name":sport.name , 
                "slug":sport.slug
            })
        
        # Promo COdes
        allPromoCodes=PromoCode.objects.all()
        promoCodeList=[]
        for promoCode in allPromoCodes:
            promoCodeList.append({
                "name":promoCode.site.name , 
                "slug":promoCode.site.slug
            })

        data={
            "sites":siteList , 
            "apps":appList ,
            "sports":sportList , 
            "promoCode":promoCodeList , 
        }

        return Response(data ,  status=status.HTTP_200_OK)


# Create your views here.
class AllSiteListView(ListAPIView):
    queryset=Site.objects.all()
    serializer_class=SiteSerializer


# Ipl Site lIst
class IplSiteListView(ListAPIView):
    queryset=Site.objects.filter(ipl=True)
    serializer_class=SiteSerializer



# Site Overview
class SiteOverviewView(RetrieveAPIView):
    serializer_class=SiteOverviewSerializer

    def get_object(self):
        slug_data=self.kwargs.get("slug")
        site=Site.objects.filter(slug=slug_data).first()
        if site is not None:
            return site.siteOverview
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


