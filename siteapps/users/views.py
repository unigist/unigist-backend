from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes

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
