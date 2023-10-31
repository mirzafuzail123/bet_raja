from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView
from cms.models import Site , App
from .serializers import *
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
class AllAppsListView(ListAPIView):
    queryset=App.objects.all()
    serializer_class=AppSerializer


# Ipl App lIst
class IplAppListView(ListAPIView):
    queryset=App.objects.filter(site__ipl=True)
    serializer_class=AppSerializer



# App Overview
class AppOverviewView(RetrieveAPIView):
    serializer_class=AppOverviewSerializer

    def get_object(self):
        slug_data=self.kwargs.get("slug")
        site=Site.objects.filter(slug=slug_data).first()
        app=site.app
        if app is not None:
            return app.appOverview
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


