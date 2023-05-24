from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import UserSerializer
from .models import User


# Create your views here.
@api_view(['GET',])
@permission_classes([AllowAny,])
def get_users_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET',])
@permission_classes([AllowAny,])
def get_user_details(request, pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({
                    'failure': 'User account is not Available!',
                    'data': []
                },
                status=HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['success'] = 'User successfully created!'
            data['data'] = serializer.data
        else:
            data = serializer.errors
        return Response(data)
