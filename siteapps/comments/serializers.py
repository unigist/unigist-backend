from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['public_id', 'content', 'author', 'post', 'created', 'edited', 'updated']
