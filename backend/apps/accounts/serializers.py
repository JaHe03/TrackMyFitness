# serializers for the accounts app

from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'phone_number', 'unit', 'theme', 'age', 'weight', 'height', 'schedule', 'is_active', 'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }   

    def create(self, validated_data):
        # Extract password from validated data since we don't want to save it in plain text
        password = validated_data.pop('password')
        # Create the user instance
        user = CustomUser(**validated_data)

        user.set_password(password) #hash the password
        user.is_active = True
        user.save()
        # Return the user instance
        return user


# login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


