from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.status import (
        HTTP_400_BAD_REQUEST,
    )
from .serializers import UserSerializer
from .models import User


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            print(serializer.data)
            data['success'] = 'User successfully created!'
            data['data'] = [serializer.data]
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

@api_view([])
def user_detail(request, pk):
    pass
