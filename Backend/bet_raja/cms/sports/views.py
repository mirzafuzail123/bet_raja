from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView
from cms.models import Sport
from .serializers import *
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
class SportsListView(ListAPIView):
    queryset=Sport.objects.all()
    serializer_class=SportsListSerializer


# Single Sports List
class SingleSportsView(RetrieveAPIView):
    queryset=Sport.objects.all()
    serializer_class=SingleSportsSerializer



# Create View
class CreateSportsView(CreateAPIView):
    queryset=Sport.objects.all()
    serializer_class=SportsListSerializer


# Create View
class EditSportsView(UpdateAPIView):
    queryset=Sport.objects.all()
    serializer_class=SportsListSerializer


