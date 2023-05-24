from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'created', 'is_active']
        extra_kwargs = {
            'password': { 'write_only': True }
        }
        # not needed since password is included in the fields
