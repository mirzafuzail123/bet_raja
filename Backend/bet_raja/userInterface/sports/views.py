from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView
from cms.models import Sport 
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from ..sites.serializers import SiteSerializer
from django.forms.models import model_to_dict


# Create your views here.
class SportView(APIView):
    def get(self  ,request , format=None , slug=None):
        sport=Sport.objects.filter(slug=slug).first()
        if sport is not None:
            siteData=[]
            for site in sport.sites.all():
                sd=model_to_dict(site)
                del sd["sports"]
                siteData.append(sd)
            sportData=model_to_dict(sport)
            sportData["sites"]=siteData
            return Response(data=sportData ,  status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)




