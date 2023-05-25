from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post
from siteapps.users.models import User

class PostSerializer(serializers.ModelSerializer):
    # telling django the type of relationship
    # slugrelatedfield represent the target of the relationship
    # here creating a post, users' username will be passed in
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='id'
    )
    def validate_author(self, value):
        """The validate_author method checks validation for the author field. Here, we want to make sure that the user creating the post is the same user as in the author field."""
        print("\n")
        # print(self.context['request'].user)
        print(value)
        print("\n")
        if self.context['user'] != value:
            raise ValidationError("You can't create a post for another nigga")
        return value
    class Meta:
        model = Post
        fields = '__all__'
