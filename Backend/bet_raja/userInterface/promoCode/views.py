from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView 
from cms.models import Site , PromoCode
from .serializers import *
from rest_framework.response import Response
from rest_framework import status





# PromoCode 
class PromoCodeView(RetrieveAPIView):
    serializer_class=PromoCodeSerializer

    def get_object(self):
        slug_data=self.kwargs.get("slug")
        site=Site.objects.filter(slug=slug_data).first()
        promocode=site.sitePromoCode
        if promocode is not None:
            return promocode
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


