from .models import Post
from .serializers import PostSerializer

from rest_framework import viewsets

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.manager.all()
    serializer_class = PostSerializer

    def get_object(self):
        obj = Post.manager.get_by_slug(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
