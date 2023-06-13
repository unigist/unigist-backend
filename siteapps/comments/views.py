
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)

from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

@api_view(['GET',])
def comments_list(req):
    if req.method == 'GET':
            comments = Comment.comments.all()
            return Response(comments)
