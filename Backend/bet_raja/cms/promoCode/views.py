from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , RetrieveUpdateAPIView
from cms.models import Site 
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PromoCodeListView(ListAPIView):
    queryset=PromoCode.objects.all()
    serializer_class=PromoCodeListSerializer


# Single PromoCode List
class SinglePromoCodeView(RetrieveUpdateAPIView):
    queryset=PromoCode.objects.all()
    serializer_class=PromoCodeSerializer



# Create PromoCode
class CreatePromoCodeView(CreateAPIView):
    queryset=PromoCode.objects.all()
    serializer_class=PromoCodeSerializer


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















