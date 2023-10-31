from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView , ListCreateAPIView ,RetrieveUpdateAPIView
from cms.models import Sport
from .serializers import *
from rest_framework.response import Response
from rest_framework import status




# List your views here.
class AppsListView(ListAPIView):
    queryset=App.objects.all()
    serializer_class=AppListSerializer


# Create
class CreateAppView(CreateAPIView):
    queryset=App.objects.all()
    serializer_class=AppsSerializer

    

# Single Apps List
class SingleAppsView(RetrieveUpdateAPIView):
    queryset=App.objects.all()
    serializer_class=AppsSerializer






# Module:App Overview

# List
class AppOverviewListView(ListAPIView):
    queryset=AppOverview.objects.all()
    serializer_class=AppOverviewListSerializer


# Create
class CreateAppOverviewView(CreateAPIView):
    queryset=AppOverview.objects.all()
    serializer_class=AppOverviewSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Valid data, save the object and return a success response.
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            # Invalid data, return a bad request response with error details.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Single
class SingleAppOverviewView(RetrieveUpdateAPIView):
    queryset=AppOverview.objects.all()
    serializer_class=AppOverviewSerializer






# # Create View
# class CreateAppsView(CreateAPIView):
#     queryset=Sport.objects.all()
#     serializer_class=AppsSerializer


# # Create View
# class EditAppsView(UpdateAPIView):
#     queryset=Sport.objects.all()
#     serializer_class=AppsSerializer


