from rest_framework.views import APIView

from .serializers import *
from cms.token import get_tokens_for_user
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

# Sending Token and Login Response
def AuthResponse(user):
    token=get_tokens_for_user(user=user)
    data={
        'access_token':token['access'],
        'refresh_token':token['refresh'],
        'username':user.username,
        'user_id':user.id,
    }
    return data


class LoginView(APIView):
    def post(self , request , format=None):
        data=request.data
        user=authenticate(username=data['username'] , password=data['password'])
        if user is not None:
            data=AuthResponse(user=user)
            response= Response(data=data, status=status.HTTP_200_OK)
            response.set_cookie(
                key="authToken" , 
                value=data["access_token"] ,
                httponly=True
            )
            print(response.cookies)
            return response
        return Response(status=status.HTTP_401_UNAUTHORIZED)


