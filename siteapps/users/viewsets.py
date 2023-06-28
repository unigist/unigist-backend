from .models import User
from .serializers import UserSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)

class UserViewset(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.

        Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    # overriding the get_object to make use of the uuid4 instead of the id

    def get_object(self):
        obj = User.objects.get_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)

        return obj
