from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
    HTTP_409_CONFLICT,
    HTTP_201_CREATED,
    HTTP_200_OK,
)

from siteapps.posts.serializers import PostSerializer

from .models import Post

# Create your views here.

@api_view(['GET',])
def get_post_detail(request, slug):
    """Get the details of a single post."""
    try:
        post = Post.articles.get(slug=slug)
        serializer = PostSerializer(post)
    except Post.DoesNotExist:
        return Response({
            'failure': 'post is not found',
        }, status=HTTP_404_NOT_FOUND)
    return Response({
        'data': serializer.data
    }, status=HTTP_200_OK)

@api_view(['GET',])
def get_articles_list(request):
    """
        Get all published post.
        if user is authenticated retrieve all post including:
            the published and drafted post
    """
    if (request.method == 'GET'):
        if request.user.is_authenticated:
            post = Post.articles.all()
            serializer = PostSerializer(post, many=True)
        else:
            post = Post.published.all()
            serializer = PostSerializer(post, many=True)

        return Response({
            'data': serializer.data
        }, status=HTTP_200_OK)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def auth_post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response({
            'failure': 'blog post does not exit'
        }, status=HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': 'post sucesfully updated',
                'data': serializer.data
            })
        return Response({
            'failure': 'post fail to update',
            'errors': serializer.errors,
        }, status=HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
            # still to see what error here
            serializer = PostSerializer(post, context={'user': request.user})
            post.delete()
            return Response({
                'success': 'post deleted successful'
            }, status=HTTP_200_OK)

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def create_post(request):
    if request.method == 'POST':
        try:
            serializer = PostSerializer(data=request.data, context={'user': request.user})
            if serializer.is_valid():
                serializer.save()

                return Response({
                    'success': 'Post successfully created!',
                    'data': serializer.data
                }, status=HTTP_201_CREATED)
            elif ValidationError:
                return Response({
                'failure': serializer.errors,
            }, status=HTTP_401_UNAUTHORIZED)
            else:
                return Response({
                    'failure': 'fail to create post',
                    'data': serializer.errors
                }, status=HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response({
                'failure': 'slug name already exit! Consider changing the title.'
            }, status=HTTP_409_CONFLICT)
