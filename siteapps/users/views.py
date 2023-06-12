from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from rest_framework.status import (
        HTTP_400_BAD_REQUEST,
        HTTP_404_NOT_FOUND,
        HTTP_409_CONFLICT,
        HTTP_401_UNAUTHORIZED,
        HTTP_200_OK,
        HTTP_201_CREATED,
    )
from .serializers import UserSerializer
from .models import User
from rest_framework.authtoken.views import ObtainAuthToken

class LogicView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = {}
            user = serializer.validated_data['user']
            user_detail = User.objects.get(username = user)
            serializeruser = UserSerializer(user_detail)

            token, created = Token.objects.get_or_create(user=user)

            data['success'] = "Login"
            data['data'] = serializeruser.data
            data['token'] = token.key
        # return  token.key,
            return Response(data, status=HTTP_200_OK)
logic_view = LogicView.as_view()

@permission_classes([IsAuthenticated,])
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        try:
            serializer = UserSerializer(data=request.data)

            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    'success': 'User successfully created!',
                    'data': serializer.data,
                    'token': Token.objects.get(user=user).key
                }, status=HTTP_201_CREATED)

            elif ValidationError:
                return Response({
                'failure': 'fail to create user',
                'error': serializer.errors,
            }, status=HTTP_401_UNAUTHORIZED)

            else:
                return Response({
                    'failure': 'fail to create user',
                    'error': serializer.errors
                }, status=HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response({
                'failure': 'user already exit! Consider changing the username or email.'
            }, status=HTTP_409_CONFLICT)


@api_view(['GET',])
def get_users_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response({
            'success': 'Users list',
            'data': serializer.data
        }, status=HTTP_200_OK)


@api_view(['GET',])
def user_detail(request, public_id):
    if request.method == 'GET':
        try:
            users = User.objects.get(public_id=public_id)
            serializer = UserSerializer(users)
            return Response({
                'success': 'User detail',
                'data':serializer.data
            }, status=HTTP_200_OK)

        # try to catch if the public id is not uuid4, but not working
        # except ValidationError or ValueError:
        #     return Response({
        #         'failure': 'Fail to parse url',
        #         'error': serializer.errors,
        #     }, status=HTTP_400_BAD_REQUEST)


        except User.DoesNotExist:
            return Response({
                'success': 'User not found',
                'data': {}
            }, status=HTTP_404_NOT_FOUND)



@api_view(['PUT', 'DELETE'])
def auth_user_detail(request, public_id):
    try:
        user = User.objects.get(public_id=public_id)

    except User.DoesNotExist:
        return Response({
            'success': 'User not found',
            'data': {},
        }, status=HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': 'User updated!',
                'data': serializer.data,
            })
        return Response({
            'failure': 'Fail to update',
            'error': serializer.errors,
        }, HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response({
            'success': 'User deleted',
            'data': {},
        }, status=HTTP_200_OK)
