from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.status import (
        HTTP_400_BAD_REQUEST,
        HTTP_404_NOT_FOUND,
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

@api_view(['GET',])
def get_users_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
@api_view(['GET',])
def user_detail(request, pk):
    if request.method == 'GET':
        try:
            users = User.objects.get(pk=pk)
            serializer = UserSerializer(users)
            return Response({
                'success': 'user details',
                'data':serializer.data
            })
        except User.DoesNotExist:
            return Response({
                'success': 'user not found',
                'data':[]
            }, HTTP_404_NOT_FOUND)



@api_view(['PUT', 'DELETE'])
def auth_user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({
            'failure': 'user is not found'
        }, status=HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': 'User successfully updated!',
                'data': serializer.data,
            })
        return Response({
            'failure': 'failed to update',
            'error': serializer.errors
        }, HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response({
            'success': 'account successfully deleted'
        })
