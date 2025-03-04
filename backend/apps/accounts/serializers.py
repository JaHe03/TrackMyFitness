# serializers for the accounts app

from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
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
        password = validated_data.pop('password', None)
        # Create the user instance
        user = CustomUser.objects.create_user(**validated_data)

        # Set the password
        if password:
            user.set_password(password)
            user.save()

        # Return the user instance
        return user
        