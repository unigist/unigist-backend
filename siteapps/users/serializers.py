from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'created', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        # not needed since password is included in the fields
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']

        user.set_password(password)
        user.save()
        return user
