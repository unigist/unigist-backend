from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
)

from siteapps.posts.serializers import PostSerializer

from .models import Post

# Create your views here.
@api_view(['GET'])
def get_post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({ 'data': serializer.data})

@api_view(['GET',])
def get_post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        serialiser = PostSerializer(post)
    except Post.DoesNotExist:
        return Response({
            'failure': 'post is not found',
        }, status=HTTP_404_NOT_FOUND)
    return Response({
        'data': serialiser.data
    })
