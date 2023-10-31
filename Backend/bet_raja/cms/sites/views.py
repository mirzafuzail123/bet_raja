from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView
from cms.models import Site , SiteOverview
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class SiteListView(ListAPIView):
    queryset=Site.objects.all()
    serializer_class=SiteListSerializer


# Single Site List
class SingleSiteView(RetrieveAPIView):
    queryset=Site.objects.all()
    serializer_class=SingleSiteSerializer



# Create Site
class CreateSiteView(CreateAPIView):
    queryset=Site.objects.all()
    serializer_class=SiteListSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         # Valid data, save the object and return a success response.
    #         self.perform_create(serializer)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         print(serializer.errors)
    #         # Invalid data, return a bad request response with error details.
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Edit Site
class EditSiteView(UpdateAPIView):
    queryset=Site.objects.all()
    serializer_class=SiteListSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the object to update
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated object
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            # Invalid data, return a bad request response with error details.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Module : oVerview




# Site Overview
class SiteOverviewListView(ListAPIView):
    serializer_class=SiteOverviewListSerializer
    queryset=SiteOverview.objects.all()



# Single Overview
class SingleSiteOverviewView(RetrieveAPIView):
    serializer_class=SiteOverviewSerializer
    queryset=SiteOverview.objects.all()



# Create Site Overview
class CreateSiteOverviewView(CreateAPIView):
    serializer_class=SiteOverviewSerializer
    queryset=SiteOverview.objects.all()
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


# Edit Site Overview
class EditSiteOverviewView(UpdateAPIView):
    serializer_class=SiteOverviewSerializer
    queryset=SiteOverview.objects.all()






